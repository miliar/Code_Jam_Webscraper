#include<iostream>
#include<algorithm>
#include<string>
#include<math.h>

using namespace std;

void FlipString(string &S, int i, int K){
 for(int j = i; j < i + K; j++){
	if(S[j] == '+')
	  S[j] = '-';
	else
	  S[j] = '+';
      }
}
bool CheckHappy(string S){
  for(int i = 0; i < S.length(); i++) {
    if(S[i] == '-')
      return false;
  }
  return true;
}

int main() {
  freopen("input.in", "r", stdin);
  freopen("output.out", "w", stdout);
  long long int T;
  cin >> T;
  for(int z = 0; z < T; z++){
    string S;
    cin >> S;
    int K;
    cin >> K;
    int min = 0;
    for(int i = 0; i < S.length() && (i+K) <= S.length(); i++){
      if(S[i]=='-'){
	FlipString(S, i, K);
	min++;
      }
    }
    cout << "Case #" << z+1 << ": ";
    if(min>=0 && CheckHappy(S))
      cout << min << endl;
    else
      cout << "IMPOSSIBLE" << endl;
  }
  return 0;
}
