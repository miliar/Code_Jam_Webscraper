#include<bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
using namespace std;
typedef long long ll;
int T,C,M,p,b,N,nr[1010];
vector<int> v[1010];

int calc(int R) {
  int ret = 0;
  int carry = 0;
  for(int i=N;i>=1;--i) {
    int s = v[i].size();
    if(s > R) {
      ret += (s - R);
      carry += (s - R);
    } else {
      if(s + carry <= R) {
        carry = 0;
      } else {
        carry = s + carry - R;
      }
    }
  }
  if(carry != 0) return -1;
  return ret;
}

int main() {
  cin.sync_with_stdio(false);
  cin>>T;
  for(int t=1;t<=T;++t) {
    cin>>N>>C>>M;
    for(int i=1;i<=C;++i) {
      nr[i] = 0;
    }
    for(int i=1;i<=N;++i) {
      v[i].clear();
    }
    for(int i=1;i<=M;++i) {
      cin>>p>>b;
      v[p].pb(b); 
      ++nr[b];
    }
    int st = 1;
    for(int i=1;i<=C;++i) {
      st = max(st, nr[i]);
    }
    int dr = max(st, M);
    int ret, num;
    while(st <= dr) {
      int mij = (st+dr)/2;
      int val = calc(mij);
      if(val != -1) {
        ret = mij;
        num = val;
        dr = mij - 1;
      } else {
        st = mij + 1;
      }
    }
    
    cout<<"Case #"<<t<<": "<<ret<<" "<<num<<"\n";
    
  }
  return 0;
}
