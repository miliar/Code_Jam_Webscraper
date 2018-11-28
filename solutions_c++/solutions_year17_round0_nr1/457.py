#include <iostream>
#include <cmath>
#include <climits>
#include <cstdlib>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <cstdio>
#include <queue>
#include <cstring>

using namespace std;

typedef long long ll;

int main(void){
  int T, K;
  cin >> T;
  string S;
  for(int tt = 0; tt < T; ++tt) {
    cin >> S >> K;
    int flip = 0;
    for(int i = K; i <= S.size(); ++i) {
      if(S[i - K] == '-') {
        ++flip;
        for(int j = i - K; j < i; ++j) {
          S[j] = S[j] == '-' ? '+' : '-';
        }
      }
    }
    cout << "Case #" << tt+1 << ": ";
    if(S.find('-') != -1) {
      cout << "IMPOSSIBLE";
    }
    else {
      cout << flip;
    }
    cout << endl;
  }

  return 0;
}
