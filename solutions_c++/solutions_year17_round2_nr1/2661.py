#include<iostream>
#include<stdio.h>

using namespace std;

void solveOneProblem(int caseNum){
  int D, N;
  cin >> D >> N;
  double max = 0.0;

  for(int i = 0; i < N; i++){
    double K, S;
    cin >> K >> S;
    double t = (D - K) / S;
    if(t > max)
      max = t;
  }

  double time = D / max;

  printf("Case #%d: %.10f\n", caseNum, time);
}




int main(){
  int N;

  cin >> N;

  for(int i = 0; i < N; i++)
    solveOneProblem(i+1);
}

