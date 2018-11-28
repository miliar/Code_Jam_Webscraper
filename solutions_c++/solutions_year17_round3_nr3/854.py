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


//sort(tab.begin(), tab.end(), greater<int>());
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
    int N, K;
    cin >> N >> K;
    double U;
    vector<double> P(N);
    cin >> U;
    FOR(i,0,N) cin >> P[i];
    sort (all(P));
    FOR(i,0,N-1) {
      double delta = P[i+1]-P[i];
      double inc;
      bool end = false;
      if (U <= delta * (i+1)) {
	inc = U / ((double)(i+1));
	end = true;
      }
      else
	inc = delta;
      FOR(j,0,i+1) {
	P[j] += inc;
	U -= inc;
      }

      if (end) break;
    }
    FOR(i,0,N) P[i] += U/(double)N;
    
    double sol = 1;
    FOR(i,0,N) sol *= P[i]; 
    cout << "Case #" << test << ": " << sol << endl;
  }
  return 0;
}
