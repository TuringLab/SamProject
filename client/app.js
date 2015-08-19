var app = angular.module('NeuralNet',['ngResource']);

app.factory('Result',['$resource',Result]);
    
function Result($resource){
    return $resource('/results/:resultId');
};

app.controller('NeuralController',['$scope','Result',NeuralController]);

function NeuralController($scope,Result){
    $scope.result = Result.get({resultId:'id'});

};