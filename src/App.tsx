import React from 'react';
import { EnpyreDisplay, EnpyreEditor, EnpyreProvider, usePyodide } from 'enpyre';

const Example: React.FC = () => {
  const { runCode } = usePyodide();

  return (
    <div style={{display: 'flex'}}>
      <div>
        <EnpyreDisplay />
        <EnpyreEditor />
        <button onClick={runCode}>Run Code</button>
      </div>
      <div style={{ padding: 10 }}>
        <h1>Examples code to run</h1>
        <p>Copy and paste some code from here: <a href="https://github.com/Enpyre/engine/tree/main/src/examples" target="_blank">Examples Code</a></p>
      </div>
    </div>
  );
}

const App: React.FC = () => {
  return (
    <EnpyreProvider>
      <Example />
    </EnpyreProvider>
  );
}

export default App;
