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

int main() {
  int T;
  cin >> T;
  cout.precision(12);
  FOR (test, 1, T+1) {
    ll n, k;
    cin >> n >> k;
    ll a = n;
    ll tab[4] =  {0,0,0,1}; // number of free intervals of size {a/2-1, a/2, a-1, a} respectively

    cout << "Case #" << test << ": ";	  
    for(;;) {
      //cout << '(' << a << ") " << tab[0] << " " << tab[1] << " " << tab[2] << " " << tab[3] << endl;
      if (tab[3] > 0) {
	if (k <= tab[3]) {
	  cout << a/2 << " " << (a-1)/2 << endl;
	  break;
	}
	else {
	  k -= tab[3];
	  tab[1] += tab[3];
	  tab[a%2] += tab[3];
	  tab[3] = 0;
	}
      }
      if (tab[2] > 0) {
	if (k <= tab[2]) {
	  cout << (a-1)/2 << " " << (a-2)/2 << endl;
	  break;
	}
	else {
	  k -= tab[2];
	  tab[0] += tab[2];
	  tab[a%2] += tab[2];
	  tab[2] = 0;
	}
      }
      tab[3] = tab[1];
      tab[2] = tab[0];
      tab[1] = tab[0] = 0;
      a /= 2;
    }
    
  }
  return 0;
}
