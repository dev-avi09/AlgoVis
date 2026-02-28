let steps = [];
let currentStep = 0;
let isPlaying = false;

function generateRandom() {
    const arr = [];
    for (let i = 0; i < 10; i++) {
        arr.push(Math.floor(Math.random() * 100) + 1);
    }
    document.getElementById('arrayInput').value = arr.join(',');
}

function renderBars(array, comparingIndices = []) {
    const container = document.getElementById('barsContainer');
    container.innerHTML = '';
    const max = Math.max(...array);

    array.forEach((value, index) => {
        const bar = document.createElement('div');
        bar.classList.add('bar');
        bar.style.height = `${(value / max) * 350}px`;
        bar.textContent = value;

        if (comparingIndices.includes(index)) {
            bar.classList.add('comparing');
        }

        container.appendChild(bar);
    });
}

async function startVisualization() {
    const input = document.getElementById('arrayInput').value;
    const algorithm = document.getElementById('algorithmSelect').value;

    if (!input) {
        alert('Please enter an array or click Random Array!');
        return;
    }

    const array = input.split(',').map(Number);

    const response = await fetch('/sort', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ array, algorithm })
    });

    const data = await response.json();
    steps = data.steps;

    document.getElementById('stepInfo').textContent = `Steps: ${steps.length}`;

    for (let i = 0; i < steps.length; i++) {
        renderBars(steps[i]);
        document.getElementById('stepInfo').textContent = `Step: ${i + 1} / ${steps.length}`;
        await sleep(300);
    }

    // Mark all as sorted
    const bars = document.querySelectorAll('.bar');
    bars.forEach(bar => bar.classList.add('sorted'));
}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}