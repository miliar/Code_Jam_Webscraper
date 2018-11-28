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
    int D, N;
    cin >> D >> N;
    vector<PII> hs = vector<PII>(N);
    REP(n, 0, N){
      PII tmp;
      cin >> tmp.fst >> tmp.snd;
      hs[n] = tmp;
    }

    double min = -1;
    REP(i, 0, N){
      double tmp = ((double)D - hs[i].fst) / (double)hs[i].snd;
      if(min < tmp){
        min = tmp;
      }
    }
    cout << "Case #" << t+1 << ": " << fixed << setprecision(9) << D / min << endl;
  }
  
  return 0;
}
