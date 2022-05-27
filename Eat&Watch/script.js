var movieTitleEl = document.querySelector("#movie-title");
var recipeUrl =
  "https://api.spoonacular.com/recipes/random?apiKey=f999bb7189a34392a1a531b4ec949828";

// to initialize the select dropdown menu for movie (needed for materialize)
$(document).ready(function () {
  $("select").formSelect();
});

// to initialize the fav btns (needed for materialize)
$(document).ready(function () {
  $(".fixed-action-btn").floatingActionButton();
});

// to generate a random movie genre
var getMovieGenres = function () {
  var apiUrl =
    "https://api.themoviedb.org/3/genre/movie/list?api_key=4a2daec3e9790c72eaaf5273d699af37&language=en-US";

  fetch(apiUrl)
    .then(function (response) {
      if (response.ok) {
        return response.json();
      }
    })
    .then(function (data) {
      // console.log(data);
      var randomGenre =
        data.genres[Math.floor(Math.random() * data.genres.length)];
      // console.log(randomGenre.name);
    });
};

// to create an array from the user's selected genre(s)
$("#movie-form").submit(function (event) {
  var selectedGenres = $("#genres-form").val();
  movieByGenre(selectedGenres);
  event.preventDefault();
});

// function to get a random movie from the user's selected genre(s)
var movieByGenre = function (genreIds) {
  // to make selectedGenres array into a string in order to add to url
  var genresString = genreIds.toString();
  // console.log(genresString);

  // API URL to discover movie list by genre
  var discoverApiUrl =
    "https://api.themoviedb.org/3/discover/movie?api_key=4a2daec3e9790c72eaaf5273d699af37&language=en-US&with_genres=" +
    genresString;

  fetch(discoverApiUrl)
    .then(function (response) {
      return response.json();
    })
    .then(function (data) {
      // console.log(data);
      // to retrieve a random movie from the selected genre(s)
      var randomMovie =
        data.results[Math.floor(Math.random() * data.results.length)];

      displayMovieTitle(randomMovie.title);
      displayMovieImage(randomMovie.poster_path);
    });
};

// append movie title to page
function displayMovieTitle(title) {
  $("#movie-title").html("");
  var movieTitle = $("<p>").text(title);
  $("#movie-title").append(movieTitle);
}

// append movie img to page
function displayMovieImage(img) {
  $("#movie-poster").html("");
  var moviePosterUrl = "https://image.tmdb.org/t/p/original/" + img;
  console.log(moviePosterUrl);
  var movieTag = $("<img>").attr("src", moviePosterUrl);
  $("#movie-poster").append(movieTag);
}

// 4a2daec3e9790c72eaaf5273d699af37

$("#food-form").submit(function (event) {
  findRecipe();
  event.preventDefault();
});

function findRecipe() {
  var tempUrl = recipeUrl;
  if ($("#food").text != "") {
    tempUrl = tempUrl + "&number=1&tags=" + $("#food").val();
  }
  fetch(tempUrl)
    .then(function (response) {
      return response.json();
    })
    .then(function (data) {
      getRecipeImg(data.recipes[0].id);
      displayRecipeName(data.recipes[0].title);
    });
}

function getRecipeImg(num) {
  $("#food-pic").html("");
  var recipeImgUrl =
    "https://spoonacular.com/recipeImages/" + num + "-480x360.jpg";
  var imgTag = $("<img>").attr("src", recipeImgUrl);
  $("#food-pic").append(imgTag);
}

function displayRecipeName(name) {
  $("#recipe-name").html("");
  var recipeName = $("<p>").text(name);
  $("#recipe-name").append(recipeName);
}

