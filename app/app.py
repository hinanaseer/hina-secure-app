from flask import Flask, render_template, jsonify
import random

app = Flask(__name__, template_folder='templates')

@app.route('/api/metrics')
def get_metrics():
    return jsonify({
        "cluster_health": "Healthy",
        "kubernetes_version": "v1.34.7",
        "cpu_usage": f"{random.randint(40, 75)}%",
        "memory_usage": f"{random.randint(55, 80)}%",
        "gitops_status": "Synced",
        "last_deployment": "Just Now via Azure DevOps",
        "security_scan": "Passed (0 Critical, 0 High)",
        "saudi_region": "Riyadh (me-central-1)"
    })

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)