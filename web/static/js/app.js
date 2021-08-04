function buildPlot(stock) {
    var apiKey = "Kgs7EXs16ZFiVxjAADDw";
  
    var url = `https://www.quandl.com/api/v3/datasets/WIKI/${stock}.json?start_date=2016-10-01&end_date=2017-10-01&api_key=${apiKey}`;
  
    d3.json(url).then(function(data) {
  
      // Grab values from the response json object to build the plots
      var name = data.dataset.name;
      var stock = data.dataset.dataset_code;
      var startDate = data.dataset.start_date;
      var endDate = data.dataset.end_date;
      var dates = unpack(data.dataset.data, 0);
      var openingPrices = unpack(data.dataset.data, 1);
      var highPrices = unpack(data.dataset.data, 2);
      var lowPrices = unpack(data.dataset.data, 3);
      var closingPrices = unpack(data.dataset.data, 4);