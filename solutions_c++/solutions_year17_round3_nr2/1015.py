#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <queue>
#include <stack>
#include <set>
#include <unordered_map>
#include <unordered_set>
#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define fillv(v,a) fill(v.begin(),v.end(),a)
#define EPS 1e-9
typedef long long ll;
typedef std::pair<int,int>pii;
typedef std::vector<int> vi;

using namespace std;

int Ac,Aj,start[100][2],et[100][2];
class Solution{
public:
  void solve(int t){
    if((Ac&&Aj)||Ac+Aj==1){printf("Case #%d: 2\n",t);return;}
    vector<pii>v;
    forn(i,Ac)v.push_back({start[i][0],et[i][0]});
    forn(i,Aj)v.push_back({start[i][1],et[i][1]});
    sort(v.begin(),v.end());
    int a=v[1].second-v[0].first,b=v[0].second+(1440-v[1].first),c=min(a,b);
    if(c<=720){printf("Case #%d: 2\n",t);return;}
    else {printf("Case #%d: 4\n",t);return;}
  }
};

int main(int argc, const char * argv[]) {
  int t;
  cin>>t;
  Solution sol;
  forn(i,t){
    cin>>Ac>>Aj;
    forn(i,Ac)cin>>start[i][0]>>et[i][0];
    forn(i,Aj)cin>>start[i][1]>>et[i][1];
    sol.solve(i+1);
    // fprintf(stderr, "Case #%d:\n", t + 1);
  }
}

