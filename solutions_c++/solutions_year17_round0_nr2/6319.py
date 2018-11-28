#include <iostream>
#include <fstream>
#include <stdio.h>
using namespace std;

string fill(string N, int index){
    for (int i = index; i < N.size(); ++i){
        N[i] = '9';
    }
    return N;
}

string check (string N){
    int length = N.size();
    for (int i = 0; i < length - 1; ++i){
        if (N[i] > N[i + 1]){
            for (int j = i; j >=0; --j){
                if (N[i] > '1'){
                    N[i] = N[i] - 1;
                    return check(fill(N,i+1));
                }
            }
            N.resize(length - 1);
            return fill(N,0);
        }
    }
    return N;
}

int main()
{
  int T;
  string N;
  ofstream output;
  ifstream input;
  input.open("input.in");
  output.open ("output.out");
  input >> T;
  for (int i = 0; i < T; ++i){
      input >> N;
      output << "Case #" << to_string(i + 1) << ": " << check(N) << endl;
  }
  output.close();
  input.close();
  return 0;
}
