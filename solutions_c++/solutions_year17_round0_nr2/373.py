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
    ll nb, nbcp;
    cin >> nb;
    nbcp = nb;
    vector<int> v;
    while(nb > 0) {
      v.pb((int) nb%10);
      nb /= 10;
    }
    int n = v.size(), i;
    for (i = n - 1; i >= 1; i --)
      if (v[i-1] < v[i])
	break;
    if (i == 0) {
      cout << "Case #" << test << ": " << nbcp << endl;
      continue;
    }
    for (; i < n - 1; i++)
      if (v[i] != v[i + 1])
	break;
    assert (v[i] != 0);
    v[i]--;
    for (i--; i >= 0; i--)
      v[i] = 9;

    ll sol = 0;
    for (i = n-1; i >= 0; i --) {
      sol *= 10LL;
      sol += v[i];
    }
    cout << "Case #" << test << ": " << sol << endl;
  }
  return 0;
}
