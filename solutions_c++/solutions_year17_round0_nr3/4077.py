#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
#define MAXN 1000005
int N,K;
bool alreadyFixed[MAXN];
vector<int> v;
struct Comp {
  bool operator()( const pair<int,pair<int,int> >& p1, const pair<int, pair<int,int> >& p2 ) {
        if(p1.first == p2.first) {
          return p1.second.first > p2.second.first;
        }
        else {
          return p1.first < p2.first;
        }
    }
};
priority_queue<pair<int,pair<int,int> >,vector<pair<int,pair<int,int> > >,Comp> Q;
int main() {
  freopen("C-small-2-attempt0.in","r",stdin);
  freopen("ans.txt","w",stdout);
  int T;
  cin >> T;
  for(int tt=1;tt<=T;tt++) {
     printf("Case #%d: ",tt);
     memset(alreadyFixed,false,sizeof alreadyFixed);
     cin >> N >> K;
     v.clear();
     v.push_back(0); v.push_back(N+1);
     while(!Q.empty()) Q.pop();
     Q.push(make_pair(N,make_pair(1,N)));
     while(!Q.empty()) {
          pair<int,pair<int,int> > pa = Q.top();
          Q.pop();
          int l = pa.second.first;
          int r = pa.second.second;
          int mid = (l+r)/2;
          v.push_back(mid);
          if(l < r) {
             Q.push(make_pair(mid-l,make_pair(l,mid-1)));
             Q.push(make_pair(r-mid,make_pair(mid+1,r)));
          }
     }
     int lastStall = v[K+1];
     for(int i=0;i<v.size();i++) {
        if(v[i] == lastStall) break;
        alreadyFixed[v[i]] = true;
     }
     int cntL = 0;
     int cntR = 0;
     int pos = lastStall;
     while(pos >= 0) {
        if(alreadyFixed[pos] == false) cntL++;
        else break;
        pos--;
     }
     pos = lastStall;
     while(pos <= N+1) {
          if(alreadyFixed[pos] == false) cntR++;
          else break;
          pos++;
     }
     cout << max(cntL,cntR)-1 << " " << min(cntL,cntR)-1 << endl;
  }
  return 0;
}
