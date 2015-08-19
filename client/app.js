var app = angular.module('NeuralNet',['ngResource']);

app.factory('Result',['$resource',Result]);
    
function Result($resource){
    return $resource('/results/:resultId');
};

app.controller('NeuralController',['$scope','Result',NeuralController]);

function NeuralController($scope,Result){
    $scope.result = Result.get({resultId:'id'});
    
    $scope.results = Result.query().$promise.then(function(){
        console.log('loaded');
    },function(error){
        console.log(error);
    })

    var result = new Result();
    result.name = 'hello';
    result.$save().then(function(){
        console.log('saved');
    },function(error){
        console.log(error);
    })
};