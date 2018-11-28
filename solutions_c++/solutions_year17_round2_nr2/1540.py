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

int maxi (int tab[3], int old, int pref) {
  int imax = -1;
  FOR(i,0,3) {
    if (i != old) {
      if ((imax == -1) || (tab[i] > tab[imax]) || (tab[i] == tab[imax] && (i == pref)))
	imax = i;
    }
  }
  return imax;
}

int toChar (int i) {
  if (i == 0) return 'R';
  if (i == 1) return 'Y';
  return 'B';
}
int toInt (char c) {
  if (c == 'R') return 0;
  if (c == 'Y') return 1;
  return 2;
}

int main() {
  int T;
  cin >> T;
  cout.precision(12);
  FOR (test, 1, T+1) {
    int N, R, O, Y, G, B, V;
    cin >> N >> R >> O >> Y >> G >> B >> V;
    int tab[3] = {R, Y, B};
    string s = "";

    int m = maxi(tab, -1, -1);
    assert (tab[m] != 0);
    tab[m]--;
    s += toChar(m);
    
    bool bad = false;
    FOR(i,1,N) {
      int m = maxi(tab, toInt(s[i-1]), toInt(s[0]));
      if (tab[m] == 0) {
	bad = true;
	break;
      }
      tab[m]--;
      s += toChar(m);
    }
    if (s[N-1] == s[0]) bad = true;
    //cout << s << endl;
    cout << "Case #" << test << ": ";
    if (bad) cout << "IMPOSSIBLE" << endl;
    else cout << s << endl;
  }
  return 0;
}
