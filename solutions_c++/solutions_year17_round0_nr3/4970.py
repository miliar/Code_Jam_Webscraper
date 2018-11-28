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

int main(){
  int T;
  cin >> T;

  REP(t, 0, T){
    ll N, K;
    cin >> N >> K;
    priority_queue<ll> que;
    que.push(N);
    ll mi = 0, mx = 0;
    REP(i, 0, K){
      ll x = que.top(); que.pop();
      if(x == 1){
        mi = mx = 0;
        break;
      }
      if(x % 2 == 0){
        mi = x / 2 - 1;
        mx = x / 2;
      } else {
        mi = mx = x / 2;
      }
      que.push(mx);
      que.push(mi);
    }
    cout << "Case #" << t+1 << ": " << mx << " " << mi << endl;
  }

  return 0;
}
