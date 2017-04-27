const express = require('express');

let app = express();

app.get('/ping', (req, res) => {
    res.json('pong');
});

app.listen(3000);

module.exports = app;