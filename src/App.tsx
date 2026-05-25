// src/App.tsx
import React, { useState, useEffect } from 'react';
import { Activity, Cpu, ShieldCheck, Zap, Sun, Sliders } from 'lucide-react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, Legend } from 'recharts';

export default function App() {
  const [hour, setHour] = useState<number>(12);
  const [day, setDay] = useState<number>(1); // 0 = Monday, 6 = Sunday
  const [prediction, setPrediction] = useState({
    predicted_energy: 28.5,
    status: 'NOMINAL',
    solar_offset: 45.0
  });

  // API से डेटा फेच करने का फंक्शन
  const fetchForecast = async () => {
    try {
      const response = await fetch('http://127.0.0.1:5000/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ hour, day }),
      });
      const data = await response.json();
      if (!data.error) {
        setPrediction(data);
      }
    } catch (err) {
      console.log("Backend server is offline, showing dummy interactive state.");
    }
  };

  useEffect(() => {
    fetchForecast();
  }, [hour, day]);

  // ग्राफ के लिए 24 घंटे का सिमुलेशन डेटा
  const chartData = [
    { hour: '00:00', Demand: 18, Forecast: 19, Solar: 0 },
    { hour: '04:00', Demand: 15, Forecast: 16, Solar: 0 },
    { hour: '08:00', Demand: 28, Forecast: 26, Solar: 15 },
    { hour: '12:00', Demand: 42, Forecast: 44, Solar: 48 },
    { hour: '16:00', Demand: 38, Forecast: 39, Solar: 25 },
    { hour: '20:00', Demand: 30, Forecast: 29, Solar: 0 },
  ];

  const daysOfWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'];

  return (
    <div className="min-h-screen bg-[#060b13] text-slate-100 font-sans p-6 selection:bg-cyan-500 selection:text-slate-900">
      
      {/* Top Navigation / Header */}
      <header className="flex flex-col sm:flex-row justify-between items-start sm:items-center border-b border-slate-800 pb-4 mb-6 gap-4">
        <div>
          <h1 className="text-2xl font-black tracking-wider text-cyan-400">NEXUS ENERGY AI</h1>
          <p className="text-xs text-slate-400 font-mono">GRID PREDICTIVE CORE // WORKSTATION_V3.5</p>
        </div>
        <div className="flex flex-wrap gap-3 text-xs bg-slate-900/60 p-2.5 rounded-lg border border-slate-800 font-mono">
          <span className="flex items-center gap-1.5 text-emerald-400">
            <ShieldCheck className="w-4 h-4"/> STATUS: {prediction.status}
          </span>
          <span className="text-slate-700">|</span>
          <span className="flex items-center gap-1.5 text-amber-400">
            <Sun className="w-4 h-4"/> GRID SOURCE: HYBRID
          </span>
        </div>
      </header>

      {/* Main Grid Workspace */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        
        {/* Left Section: Graphical Forecast Panel */}
        <div className="lg:col-span-2 bg-slate-900/30 border border-slate-800/80 rounded-xl p-6 backdrop-blur-sm">
          <div className="flex justify-between items-center mb-4">
            <h2 className="text-sm font-bold uppercase tracking-widest text-slate-400 flex items-center gap-2 font-mono">
              <Activity className="w-4 h-4 text-cyan-400" /> Demand Cycles & Photovoltaic Ingress
            </h2>
            <span className="text-[10px] text-slate-500 font-mono">REAL-TIME INFERENCE</span>
          </div>
          
          {/* Recharts Graphical Display */}
          <div className="h-72 w-full my-2">
            <ResponsiveContainer width="100%" height="100%">
              <LineChart data={chartData} margin={{ top: 10, right: 10, left: -20, bottom: 0 }}>
                <CartesianGrid strokeDasharray="3 3" stroke="#131c2e" />
                <XAxis dataKey="hour" stroke="#475569" style={{ fontSize: '11px', fontFamily: 'monospace' }} />
                <YAxis stroke="#475569" style={{ fontSize: '11px', fontFamily: 'monospace' }} />
                <Tooltip contentStyle={{ backgroundColor: '#0b1324', borderColor: '#1e293b', borderRadius: '8px', color: '#fff' }} />
                <Legend wrapperStyle={{ fontSize: '11px', fontFamily: 'monospace', paddingTop: '10px' }} />
                <Line type="monotone" dataKey="Forecast" stroke="#ef4444" strokeDasharray="4 4" strokeWidth={2} activeDot={{ r: 6 }} />
                <Line type="monotone" dataKey="Demand" stroke="#06b6d4" strokeWidth={2} />
                <Line type="monotone" dataKey="Solar" stroke="#10b981" strokeWidth={2} />
              </LineChart>
            </ResponsiveContainer>
          </div>

          {/* Virtual Simulators Control Station */}
          <div className="bg-slate-950/80 p-5 rounded-xl border border-slate-800/60 mt-6">
            <h3 className="text-xs font-bold text-cyan-400 uppercase tracking-wider mb-4 flex items-center gap-2 font-mono">
              <Sliders className="w-4 h-4"/> Simulation Parameter Controllers
            </h3>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div>
                <div className="flex justify-between text-xs font-mono mb-1.5">
                  <span className="text-slate-400">Target Hour:</span>
                  <span className="text-cyan-400 font-bold">{hour}:00 Hrs</span>
                </div>
                <input 
                  type="range" min="0" max="23" value={hour} 
                  onChange={(e) => setHour(parseInt(e.target.value))} 
                  className="w-full h-1.5 bg-slate-800 rounded-lg appearance-none cursor-pointer accent-cyan-400" 
                />
              </div>
              <div>
                <div className="flex justify-between text-xs font-mono mb-1.5">
                  <span className="text-slate-400">Day Vector:</span>
                  <span className="text-emerald-400 font-bold">{daysOfWeek[day]}</span>
                </div>
                <input 
                  type="range" min="0" max="6" value={day} 
                  onChange={(e) => setDay(parseInt(e.target.value))} 
                  className="w-full h-1.5 bg-slate-800 rounded-lg appearance-none cursor-pointer accent-emerald-400" 
                />
              </div>
            </div>
          </div>
        </div>

        {/* Right Section: Core ML Telemetry Metrics & Insights */}
        <div className="flex flex-col gap-6">
          
          {/* Metric Telemetry Grid */}
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-1 gap-4">
            
            {/* Box 1 */}
            <div className="bg-gradient-to-br from-slate-900/60 to-slate-900/20 p-5 rounded-xl border border-slate-800">
              <span className="text-xs text-slate-400 font-mono uppercase tracking-wider block">Neural Net Prediction</span>
              <div className="text-4xl font-black text-cyan-400 mt-2 flex items-baseline gap-1 font-mono tracking-tight">
                {prediction.predicted_energy} <span className="text-sm font-normal text-slate-500 uppercase">kW</span>
              </div>
              <p className="text-[10px] text-slate-500 mt-1 font-mono">Calculated via MLP Regressor Architecture</p>
            </div>

            {/* Box 2 */}
            <div className="bg-gradient-to-br from-slate-900/60 to-slate-900/20 p-5 rounded-xl border border-slate-800">
              <span className="text-xs text-slate-400 font-mono uppercase tracking-wider block">Solar Integration Efficiency</span>
              <div className="text-4xl font-black text-emerald-400 mt-2 flex items-baseline gap-1 font-mono tracking-tight">
                {prediction.solar_offset}% <span className="text-sm font-normal text-slate-500 uppercase">Offset</span>
              </div>
              <p className="text-[10px] text-slate-500 mt-1 font-mono">Live Photo-voltaic Grid Contribution</p>
            </div>

          </div>

          {/* AI Advisory Panel */}
          <div className="bg-slate-900/30 border border-slate-800/80 rounded-xl p-5 flex-1 flex flex-col justify-between backdrop-blur-sm">
            <div>
              <h2 className="text-xs font-bold uppercase tracking-widest text-amber-400 mb-3 flex items-center gap-1.5 font-mono">
                <Cpu className="w-4 h-4"/> AI Co-Pilot Smart Advisories
              </h2>
              <div className="text-xs text-slate-300 bg-slate-950/80 p-3 rounded-lg border-l-2 border-cyan-500 font-mono leading-relaxed mb-4">
                "Based on the temporal parameters selected (Hour: {hour}, Day: {day}), the system predicts a load metric of {prediction.predicted_energy} kW. {hour >= 10 && hour <= 15 ? 'High solar yields detected. Diverting excess storage capacity into server facility pre-cooling cells.' : 'Standard operational grid cycle running.'}"
              </div>
              
              <div className="space-y-2">
                <div className="text-xs bg-slate-950/40 p-3 rounded-lg border border-slate-800/60 flex justify-between items-center font-mono">
                  <div>
                    <p className="font-semibold text-cyan-400">Automated Peak-Shedding</p>
                    <p className="text-[10px] text-slate-500">Scheduled for optimization threshold</p>
                  </div>
                  <span className="text-xs font-bold text-emerald-400">ACTIVE</span>
                </div>
              </div>
            </div>

            <button className="w-full mt-6 bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-500 hover:to-teal-500 transition-all text-slate-950 font-extrabold py-3 px-4 rounded-xl text-xs tracking-widest uppercase flex items-center justify-center gap-2 shadow-lg shadow-emerald-950/20 font-mono">
              <Zap className="w-4 h-4 fill-slate-950"/> Trigger Grid Mitigation Loop
            </button>
          </div>

        </div>

      </div>
    </div>
  );
}