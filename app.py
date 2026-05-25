# app.py
from flask import Flask, request, jsonify, render_template_string
from flask_cors import CORS
import joblib
import numpy as np

app = Flask(__name__)
CORS(app)

# Critical Kernel Initialization
try:
    model = joblib.load('energy_forecast_model.pkl')
    print("🚀 Neural Network Inference Core loaded successfully!")
except Exception as e:
    print("❌ Critical System Failure: Model weight vectors missing. Run train.py first.")

# High-Fidelity Enterprise Analytics Dashboard UI Template (Matches Images Exactly)
HYPER_DASHBOARD_UI = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NEXUS ENERGY AI // ENTERPRISE GRID TELEMETRY</title>
    <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
    <script src="https://unpkg.com/lucide@latest"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        body { background-color: #04080f; }
        .cyber-grid { background-image: linear-gradient(#0c1524 1px, transparent 1px), linear-gradient(90deg, #0c1524 1px, transparent 1px); background-size: 20px 20px; }
    </style>
</head>
<body class="cyber-grid text-slate-100 min-h-screen font-sans p-6">

    <header class="max-w-7xl mx-auto flex flex-col md:flex-row justify-between items-start md:items-center border-b border-slate-800/80 pb-5 mb-8 gap-4">
        <div>
            <div class="flex items-center gap-2">
                <div class="w-2.5 h-2.5 bg-cyan-400 rounded-full animate-pulse"></div>
                <h1 class="text-2xl font-black tracking-widest text-cyan-400 font-mono">NEXUS ENERGY AI</h1>
            </div>
            <p class="text-xs text-slate-500 font-mono mt-0.5">GRID PREDICTIVE CONTROL STATION v4.2 // PRODUCTION ENGINE</p>
        </div>
        <div class="flex gap-4 text-xs bg-slate-900/60 p-3 rounded-xl border border-slate-800/80 font-mono shadow-inner shadow-cyan-950/10">
            <span class="flex items-center gap-1.5 text-emerald-400"><i data-lucide="shield-check" class="w-4 h-4"></i> STATUS: TELEMETRY NOMINAL</span>
            <span class="text-slate-700">|</span>
            <span class="flex items-center gap-1.5 text-amber-400"><i data-lucide="sun" class="w-4 h-4"></i> GRID OFFSET: MULTI-SOURCE</span>
        </div>
    </header>

    <main class="max-w-7xl mx-auto grid grid-cols-1 lg:grid-cols-3 gap-6">
        
        <div class="lg:col-span-2 space-y-6">
            
            <div class="bg-slate-950/40 border border-slate-800/90 rounded-2xl p-6 backdrop-blur-md">
                <div class="flex justify-between items-center mb-6">
                    <h2 class="text-sm font-bold uppercase tracking-widest text-slate-400 flex items-center gap-2 font-mono">
                        <i data-lucide="activity" class="text-cyan-400 w-4 h-4"></i> Demand Cycles & Photovoltaic Ingress
                    </h2>
                    <span class="text-[10px] text-slate-500 font-mono bg-slate-900 px-2 py-0.5 rounded border border-slate-800">LIVE FEED</span>
                </div>
                <div class="w-full relative h-72">
                    <canvas id="telemetryChart"></canvas>
                </div>
            </div>

            <div class="bg-slate-950/60 border border-slate-800/90 rounded-2xl p-6 backdrop-blur-md">
                <h3 class="text-xs font-bold text-cyan-400 uppercase tracking-widest mb-5 flex items-center gap-2 font-mono">
                    <i data-lucide="sliders" class="w-4 h-4"></i> Interactive Control Parameters Simulation
                </h3>
                <form id="forecastForm" class="grid grid-cols-1 sm:grid-cols-2 gap-6">
                    <div>
                        <label class="block text-xs font-mono text-slate-400 mb-2 uppercase tracking-wider">Target Operational Hour</label>
                        <select id="hour" class="w-full bg-slate-900 border border-slate-700/60 p-3 rounded-xl font-mono text-sm text-cyan-300 focus:outline-none focus:border-cyan-400">
                            </select>
                    </div>
                    <div>
                        <label class="block text-xs font-mono text-slate-400 mb-2 uppercase tracking-wider">Target Temporal Vector</label>
                        <select id="day" class="w-full bg-slate-900 border border-slate-700/60 p-3 rounded-xl font-mono text-sm text-emerald-400 focus:outline-none focus:border-emerald-400">
                            <option value="0">Monday (Operational Baseline)</option>
                            <option value="1">Tuesday (Peak Business Load)</option>
                            <option value="2">Wednesday (Mid-Week Maintenance)</option>
                            <option value="3">Thursday (High Production Vector)</option>
                            <option value="4">Friday (Weekend Descent Profile)</option>
                            <option value="5">Saturday (Low System Latency)</option>
                            <option value="6">Sunday (Minimum Safe Grid Capacity)</option>
                        </select>
                    </div>
                    <button type="submit" class="sm:col-span-2 w-full bg-gradient-to-r from-cyan-500 to-blue-600 hover:from-cyan-400 hover:to-blue-500 transition-all font-mono font-bold text-slate-950 p-4 rounded-xl text-xs uppercase tracking-widest flex items-center justify-center gap-2 shadow-lg shadow-cyan-950/30 cursor-pointer">
                        <i data-lucide="cpu" class="w-4 h-4"></i> Run Micro-Grid Forecast Inferences
                    </button>
                </form>
            </div>

        </div>

        <div class="space-y-6">
            
            <div class="bg-gradient-to-b from-slate-900/60 to-slate-950/20 border border-slate-800/80 p-5 rounded-2xl">
                <span class="text-xs text-slate-500 font-mono uppercase tracking-wider block">Neural Network Core Forecast</span>
                <div class="text-4xl font-black text-cyan-400 mt-2 flex items-baseline gap-1 font-mono tracking-tight">
                    <span id="predictedValue">--.--</span> <span class="text-xs font-normal text-slate-500 uppercase">kW/h</span>
                </div>
                <p class="text-[10px] text-slate-500 mt-1 font-mono">Statistical Inference generated via MLP Activation Layers</p>
            </div>

            <div class="bg-gradient-to-b from-slate-900/60 to-slate-950/20 border border-slate-800/80 p-5 rounded-2xl">
                <span class="text-xs text-slate-500 font-mono uppercase tracking-wider block">Renewable Photovoltaic Yield</span>
                <div class="text-4xl font-black text-emerald-400 mt-2 flex items-baseline gap-1 font-mono tracking-tight">
                    <span id="solarValue">--.-</span> <span class="text-xs font-normal text-slate-500 uppercase">% Offset</span>
                </div>
                <p class="text-[10px] text-slate-500 mt-1 font-mono">Dynamic eco-buffer calculation mapping solar vector ingestion</p>
            </div>

            <div class="bg-slate-900/20 border border-slate-800/90 rounded-2xl p-6 flex flex-col justify-between backdrop-blur-md min-h-[260px]">
                <div>
                    <h4 class="text-xs font-bold uppercase tracking-widest text-amber-400 mb-3.5 flex items-center gap-1.5 font-mono">
                        <i data-lucide="zap" class="w-4 h-4 fill-amber-400"></i> AI Co-Pilot Mitigation System
                    </h4>
                    <div id="advisoryText" class="text-xs text-slate-300 bg-slate-950/90 p-3.5 rounded-xl border border-slate-800/60 font-mono leading-relaxed shadow-inner">
                        Awaiting micro-grid optimization parameter matrices. Adjust simulation vectors and fire inference loop engine.
                    </div>
                </div>

                <div class="mt-4 pt-4 border-t border-slate-800/80 flex justify-between items-center text-xs font-mono">
                    <div>
                        <p class="font-semibold text-cyan-400" id="strategyTitle">System Baseline Logic</p>
                        <p class="text-[10px] text-slate-500">Autonomous loop control state</p>
                    </div>
                    <span id="statusTag" class="text-[10px] font-bold px-2.5 py-1 bg-slate-900 rounded border border-slate-800 text-slate-400">STANDBY</span>
                </div>
            </div>

        </div>

    </main>

    <script>
        // Init Lucide Dynamic Icon Sets
        lucide.createIcons();

        // Dynamically build selection data option matrices
        const hourSelect = document.getElementById('hour');
        for (let i = 0; i < 24; i++) {
            let opt = document.createElement('option');
            opt.value = i;
            opt.text = (i < 10 ? '0' + i : i) + ':00 Hours Baseline';
            if (i === 12) opt.selected = true;
            hourSelect.appendChild(opt);
        }

        // Initialize Advanced Chart.js Graphing Space mapping Image 2 visuals
        const ctx = document.getElementById('telemetryChart').getContext('2d');
        const telemetryChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: ['00:00', '04:00', '08:00', '12:00', '16:00', '20:00'],
                datasets: [
                    { label: 'AI Forecasting Target', data: [19, 16, 26, 44, 39, 29], borderColor: '#ef4444', borderDash: [5, 5], borderWidth: 2, tension: 0.3, pointRadius: 0 },
                    { label: 'Actual MicroGrid Load', data: [18, 15, 28, 42, 38, 30], borderColor: '#06b6d4', borderWidth: 2.5, tension: 0.3, pointRadius: 3, backgroundColor: 'rgba(6, 182, 212, 0.04)', fill: true },
                    { label: 'Photovoltaic Solar Yield', data: [0, 0, 15, 48, 25, 0], borderColor: '#10b981', borderWidth: 2, tension: 0.3, pointRadius: 0 }
                ]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: { legend: { labels: { color: '#64748b', font: { family: 'monospace', size: 10 } } } },
                scales: {
                    x: { grid: { color: '#111e36' }, ticks: { color: '#475569', font: { family: 'monospace' } } },
                    y: { grid: { color: '#111e36' }, ticks: { color: '#475569', font: { family: 'monospace' } } }
                }
            }
        });

        // Form event listener parsing asynchronous fetch payloads to backend API
        document.getElementById('forecastForm').addEventListener('submit', async (e) => {
            e.preventDefault();
            const hourValue = document.getElementById('hour').value;
            const dayValue = document.getElementById('day').value;

            try {
                const response = await fetch('/predict', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ hour: parseInt(hourValue), day: parseInt(dayValue) })
                });
                const telemetryData = await response.json();

                // Live inject parameters inside HTML target vectors
                document.getElementById('predictedValue').innerText = telemetryData.predicted_energy;
                document.getElementById('solarValue').innerText = telemetryData.solar_offset;
                
                const statusTag = document.getElementById('statusTag');
                const advisoryText = document.getElementById('advisoryText');
                const strategyTitle = document.getElementById('strategyTitle');

                if (telemetryData.status === 'HIGH GRID DEMAND VEC') {
                    statusTag.className = "text-[10px] font-bold px-2.5 py-1 bg-red-950/40 border border-red-800 text-red-400 rounded animate-pulse";
                    statusTag.innerText = "CRITICAL PEAK";
                    strategyTitle.innerText = "Automated Load Shedding Loop";
                    advisoryText.innerText = `[ALERT] Critical grid load detected at ${hourValue}:00 Hrs. Total prediction vector surged to ${telemetryData.predicted_energy} kW/h. AI recommendation engine has scheduled a load-shedding protocol for primary industrial cooling cells to minimize localized peak-tariff pricing metrics.`;
                } else {
                    statusTag.className = "text-[10px] font-bold px-2.5 py-1 bg-emerald-950/40 border border-emerald-800 text-emerald-400 rounded";
                    statusTag.innerText = "STABLE GRID";
                    strategyTitle.innerText = "Solar Buffer Optimizing";
                    advisoryText.innerText = `[NOMINAL] Smart Grid running within safety margins. Predicted capacity stabilized at ${telemetryData.predicted_energy} kW/h. Active solar generation yield is maintaining an efficiency offset of ${telemetryData.solar_offset}%. No emergency automation mitigation steps are required.`;
                }

            } catch (err) {
                alert('Critical Exception: Failed connection pipeline interface link with Python micro-core.');
            }
        });
    </script>
</body>
</html>
"""

@app.route('/', methods=['GET'])
def render_terminal_dashboard():
    return render_template_string(HYPER_DASHBOARD_UI)

@app.route('/predict', methods=['POST'])
def micro_inference_endpoint():
    try:
        payload = request.get_json()
        hour = int(payload.get('hour', 12))
        day = int(payload.get('day', 0))
        
        # Model vector extraction
        features = np.array([[hour, day]])
        prediction = model.predict(features)[0]
        
        # Micro calculations imitating environmental photovoltaic yield (solar curves)
        solar_yield_curve = max(0, 55.4 - (abs(hour - 13) * 4.8))
        
        return jsonify({
            'predicted_energy': round(float(prediction), 2),
            'solar_offset': round(float(solar_yield_curve), 1),
            'status': 'HIGH GRID DEMAND VEC' if prediction >= 38.5 else 'NOMINAL CAPACITY OPERATION'
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(port=5000, debug=True)