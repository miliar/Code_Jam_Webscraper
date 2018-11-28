#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string.h>
#include <strings.h>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
#include <iostream>
#include <sstream>
#include <iomanip>
#include <math.h>
#include <cmath>
#include <map>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <iomanip>
#include <cmath>
#include <ctime>
#include <climits>
#include <assert.h>

using namespace std;


typedef vector<int> vi; 
typedef vector<vi> vvi; 
typedef pair<int,int> ii; 
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> int2;
typedef pair<float, float> float2;
typedef pair<ull, ull> ull2;

#define sz(a) int((a).size()) 
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define tr(s,i) for ( __typeof((s).begin()) i = ((s).begin())   ; i != (s).end(); ++i)  
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end()) 
#define mp(a,b) make_pair(a,b)
#define del(s,x) do {__typeof((s).begin()) abcde=(s).find(x); if(abcde !=(s).end()) s.erase(abcde); } while(0);
#define del2(s,x) do {__typeof((s).begin()) abcde=find(all(s),x); if(abcde !=(s).end()) s.erase(abcde); } while(0);

#define FOR(i,a,b) for(int i=int(a); i<int(b); ++i)



//#define test(a,b) (test[a][b] == '?' || test[a]
int main() {
  int T;
  cin >> T;
  cout.precision(12);
  FOR (test, 1, T+1) {
    int R, C;
    cin >> R >> C;
    vector<string> Gs(R,"");
    FOR(i,0,R) cin >> Gs[i];
    cout << "Case #" << test << ": " << endl;
    
    FOR(i,0,R) {
      char f = ' ';
      FOR(j,0,C) if (Gs[i][j] != '?') { f = Gs[i][j]; break; } 
      if (f != ' ') {
	FOR(j,0,C) {
	  if (Gs[i][j] == '?')
	    Gs[i][j] = f;
	  else
	    f = Gs[i][j];
	}
      }
    }
    // FOR(i,0,R) cout << Gs[i] << endl;
    //cout << endl;

    FOR(j,0,C) {
      char f = ' ';
      FOR(i,0,R) if (Gs[i][j] != '?') { f = Gs[i][j]; break; }
      assert (f != ' ');
      FOR(i,0,R) {
	if (Gs[i][j] == '?')
	  Gs[i][j] = f;
	else
	  f = Gs[i][j];
      }
      
    }
    FOR(i,0,R) cout << Gs[i] << endl;
  }
  return 0;
}
