#include <algorithm>
#include <cmath>
#include <climits>
#include <cstring>
#include <cstdio>
#include <deque>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <map> //pair is also included in this library
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <unordered_map>
#include <vector>

#define REP(i, s, n) for(int i = (int)(s); i < (int)(n); i++)
#define fst first
#define snd second
#define MP make_pair //incase c++11 or later is not available

using namespace std;

typedef long long int ll;
typedef vector<int> VI;
typedef vector<ll> VL;
typedef pair<int, int> PII;
typedef pair<ll, ll> PLL;

//prefer define statement
//for reason that const int ver. of INF will raise a silly warning (unused variable)
#define INF (INT_MAX/3)
#define LIM_INF (INT_MAX)
//const int INF = INT_MAX/3;
#define PI = 3.14159265358979323846
/*------------------------------------------------------------------------------*/

void flip(string& S, int x, int K){
  REP(i, 0, K){
    if(S[x+i] == '+'){
      S[x+i] = '-';
    } else {
      S[x+i] = '+';
    }
  }
  return;
}

int main(){
  int T, K;
  string S;

  cin >> T;

  REP(i, 0, T){
    cin >> S >> K;
    int ans = 0;
    int len = S.length();

    REP(j, 0, S.length()-K+1){
      if(S[j] == '-'){
        flip(S, j, K);
        ans++;
      }
    }

    REP(j, 0, K){
      if(S[len-j] == '-'){
        ans = -1;
        break;
      }
    }
    
    if(ans >= 0){
      cout << "Case #" << i+1 << ": " << ans << endl;
    } else {
      cout << "Case #" << i+1 << ": IMPOSSIBLE" << endl;
    }
  }

  return 0;
}
