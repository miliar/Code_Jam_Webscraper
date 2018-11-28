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

  string ans = "";
  REP(t, 0, T){
    string s;
    cin >> s;
    int num = 0;
    bool dec = false;

    REP(i, 1, s.length()){
      int sa = s[i-1]-'0', sb = s[i]-'0';
      if(sa < sb){
        num = i;
      } else if(sa > sb){
        dec = true;
        break;
      }
    }

    if(dec){
      string ans = "";
      REP(i, 0, s.length()){
        if(i < num){
          ans += s[i];
        } else if(i == num){
          char tmp = s[i] - 1;
          if(tmp == '0' && num == 0){
            continue;
          }
          ans += tmp;
        } else {
          ans += '9';
        }
      }
      cout << "Case #" << t+1 << ": " << ans << endl;
    } else {
      cout << "Case #" << t+1 << ": " << s << endl;
    }
  }

  return 0;
}
