#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>
using namespace std;

int ComputeMinFlips(string S, int K)
{
  int length = S.length(), minFlips = 0, sum = 0;
  int Change[length+1], A[length+1];
  memset(Change, 0, sizeof(int) * (length+1));
  memset(A, 0, sizeof(int) * (length+1));
  for(int i = 1; i <= length; ++i){
    switch(S.at(i-1)){
      case '+':
        A[i] = 1; break;
      case '-':
        A[i] = -1; break;
      default:
        break;
    }
  }
  for(int i = 1; i <= length; ++i){
    if(A[i] < 0){
      if(i+K-1 <= length){
        for(int j = i; j < i+K; ++j){
          A[j] = -A[j];
        }
        minFlips += 1;
      }
      else{
        minFlips = -1; break;
      }
    }

  }

  return minFlips;
}

void GetAnswer()
{
  int T, K, answer;
  string S;
  cin >> T;
  for(int i = 1; i <= T; ++i){
    cin >> S >> K;
    answer = ComputeMinFlips(S, K);
    if(answer >= 0)
      cout << "Case #" << i << ": " << answer << endl;
    else
      cout << "Case #" << i << ": IMPOSSIBLE" << endl;
  }
}

int main()
{
  GetAnswer();
  return 0;
}
