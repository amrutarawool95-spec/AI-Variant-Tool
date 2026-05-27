from flask import Flask, request, jsonify, render_template
import os
from variant_pipeline import parse_vcf, build_features, ensemble_predict, rank_variants

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    # Serves the front-end dashboard
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'vcf' not in request.files:
        return jsonify({"error": "No VCF file uploaded"}), 400
        
    vcf_file = request.files['vcf']
    hpo_terms = request.form.get('hpo_terms', '').split(',') # e.g., HP:0001250 [cite: 80]
    
    # Save file temporarily
    vcf_path = os.path.join(app.config['UPLOAD_FOLDER'], vcf_file.filename)
    vcf_file.save(vcf_path)
    
    # Run the pipeline based on the project architecture [cite: 81, 84, 85, 86]
    variants = parse_vcf(vcf_path)
    features = build_features(variants, hpo_terms) 
    scores = ensemble_predict(features) 
    top20 = rank_variants(variants, scores)[:20] 
    
    # Clean up
    os.remove(vcf_path)
    
    return jsonify(top20.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
