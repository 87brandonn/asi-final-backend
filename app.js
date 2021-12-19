const express = require('express');
const path = require('path');
var bodyParser = require('body-parser');
const PythonShell = require('python-shell').PythonShell;
const app = express();
const cors = require('cors');
app.use(
  cors({
    origin: ['http://localhost:3001', 'https://asi-final.web.app']
  })
);
app.use(bodyParser.json());
const port = 5000;

app.post('/', (req, res) => {
  const text = req.body.text;
  const __dirname = path.resolve();
  const filePath = path.join(__dirname, '/python.py');
  PythonShell.run(
    `${filePath}`,
    {
      args: [text]
    },
    (err, data) => {
      if (err) throw err;
      res.send(data);
    }
  );
});

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`);
});