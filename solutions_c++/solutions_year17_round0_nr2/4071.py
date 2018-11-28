#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main(){

  int T;
  cin >> T;

  for (int j = 0; j < T; j++){
    string N;

    cin >> N;

    int i = 0;

    int length = N.size();

    while (i < length-1 && N[i] <= N[i+1]){
      i++;
    }

    if (i < length-1){
      while (i != 0 && N[i] == N[i-1]){
        i--;
      }
      N[i] = N[i] - 1;
      i++;
      while (i < length){
        N[i] = '9';
        i++;
      }
    }
    if (N[0] == '0'){
      N = N.substr(1);
    }
    cout << "Case #" << j+1 <<": " << N << endl;
  }

  return 0;
}
