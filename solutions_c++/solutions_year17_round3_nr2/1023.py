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
    int ac, aj;
    int sum[2]; sum[0] = sum[1] = 0;
    cin >> ac >> aj;
    vector<pair<int, pair<int, int> > >v;
    FOR(i,0,ac) {
      int a, b;
      cin >> a >> b;
      v.pb (make_pair(a, make_pair(b, 0)));
      sum[0] += b-a;
    }
    FOR(i,0,aj) {
      int a, b;
      cin >> a >> b;
      v.pb (make_pair(a, make_pair(b, 1)));
      sum[1] += b-a;
    }
    sort(all(v));
    int freeEqual[2];freeEqual[0] = freeEqual[1] = 0;
    int freeDiff = 0;
    int prevTime = - (1440 - v[v.size() - 1].second.first);
    int prevId = v[v.size() - 1].second.second;
    int nbChange = 0;
    vector<int> durEqual[2];
    FOR(i,0,ac+aj) {
      int time = v[i].first - prevTime;
      int id = v[i].second.second;
      if (prevId == id) {
	freeEqual[id] += time;
	durEqual[id].pb(time);
      }
      else {
	freeDiff += v[i].first - prevTime;
	nbChange ++;
      }
      prevTime = v[i].second.first;
      prevId = id;
    }
    //cout << sum[0] << " " << sum[1] << " " << freeEqual[0] << " " << freeEqual[1] << " " << freeDiff  << " " << nbChange << endl;
    sort(all(durEqual[0]), greater<int>());
    sort(all(durEqual[1]), greater<int>());
    int idmin = (((sum[0] + freeEqual[0]) < (sum[1] + freeEqual[1])) ? 0 : 1);
    int summin = sum[idmin] + freeEqual[idmin];
    
    summin += freeDiff;

    for (int i = 0; (i < durEqual[1-idmin].size()) && (summin < 720); i++) {
      summin += durEqual[1-idmin][i];
      nbChange += 2;
    }
    
    assert (summin >= 720);
    cout << "Case #" << test << ": " << nbChange << endl;
  }
  return 0;
}
