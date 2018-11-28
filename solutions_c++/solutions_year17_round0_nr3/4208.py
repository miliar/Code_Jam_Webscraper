#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
#include <limits>
#include <cmath>


using namespace std;

int main(){

  int T;

  cin >> T;

  for (int i = 0; i < T; i++){
    long long int N, K;

    cin >> N;
    cin >> K;

    int M = 0;
    while (!(pow(2,M)-1 < K && K <= pow(2,M+1)-1)){
      M++;
    }

    long long int res = N - (pow(2,M)-1);
    long long int mod = res / pow(2,M);
    long long int rem = res - mod*pow(2,M);
    long long int lenght = mod;

    if (K - (pow(2,M)-1) <= rem){
      lenght++;
    }

    if (lenght % 2 == 0){
      cout << "Case #" << i+1 << ": " << lenght/2 << " " << lenght/2-1 << endl;
    }
    else{
      cout << "Case #" << i+1 << ": " << (lenght-1)/2 << " " << (lenght-1)/2 << endl;
    }

  }

  return 0;
}
