#include <iostream>
#include <fstream>
using namespace std;



string flip(string S,int K){
    int N = S.size();
    int count = 0;
    for (int i = 0; i < N; ++i){
        if (S[i] == '-'){
            if (i + K < N){
                count++;
                for (int j = i; j < i + K; ++j){
                    S[j] = (S[j] == '+')? '-' : '+';
                }
            } else {
                for (int j = N - K; j < N; ++j){
                    if (S[j] == '+'){
                        return "IMPOSSIBLE";
                    }
                }
                return to_string(count + 1);
            }
        }
    }
    return to_string(count);
}

int main()
{
  int T;
  string S;
  int K;
  ofstream output;
  ifstream input;
  input.open("input.in");
  output.open ("output");
  input >> T;
  for (int i = 0; i < T; ++i){
      input >> S >> K;
      output << "Case #" + to_string(i + 1) + ": " + flip(S,K) << endl;
  }
  output.close();
  input.close();
  return 0;
}
