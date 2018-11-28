#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main(){

  int T;

  cin >> T;

  for (int n_case = 1; n_case <= T; n_case++){
    long long int D;
    cin >> D;

    int N;
    cin >> N;

    float highest = 0.0;


    for (int i = 0; i < N; i++){
      long long int K;
      cin >> K;
      int S;
      cin >> S;

      float current_time = (float)(D - K)/(S);

      if (current_time > highest)
        highest = current_time;

    }

    cout.precision(10);

    cout << "Case #" << n_case << ": " << fixed << float(D)/highest << endl;

  }

  return 0;
}
