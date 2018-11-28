#include <bits/stdc++.h>
using namespace std;

#define EPS      1e-9
#define F        first
#define S        second
#define pi       acos(-1)
#define ll       long long
#define inf      0x3f3f3f3f
#define sz(x)    (int)x.size()
#define sc(x)    scanf("%d",&x)
#define all(x)   x.begin(),x.end()
#define rall(x)  x.rbegin(),x.rend()

int T;
int n,c,m;
int me[1010];
int cnt[1010];
int mxCnt;

bool fxx(int idx,int r){
  for(int i=1;i<idx;++i){
    if(cnt[i]<r){
      cnt[i]++;
      cnt[idx]--;
      return true;
    }
  }
  return false;  
}

int tmp[1010];
int prom(int r){
  for(int i=0;i<=1000;++i)tmp[i]=cnt[i];
  int pro=0;
  for(int i=1;i<=n;++i){
    if(cnt[i]<=r)continue;
    while(cnt[i]>r){
      //cout<<i<<" "<<cnt[i]<<"===>\n";
      if(fxx(i,r)){
        pro++;
        //cnt[i]--;
      }else{
        pro=10000;
        break;
      }
      //cout<<i<<" "<<cnt[i]<<"<===\n";
    }
  }
  for(int i=0;i<=1000;++i)cnt[i]=tmp[i];
  return pro;
}

int main() {
#ifndef ONLINE_JUDGE
  freopen("B-large.in", "r", stdin);
  freopen("out.txt", "w", stdout);
#endif
  sc(T);
  for(int C=1;C<=T;++C){
    sc(n),sc(c),sc(m);
    memset(me,0,sizeof me);
    memset(cnt,0,sizeof cnt);
    mxCnt=0;
    for(int i=0;i<m;++i){
      int p,b;
      sc(p),sc(b);
      cnt[p]++;
      me[b]++;
    }
    for(int i=1;i<=c;++i)
      mxCnt=max(mxCnt,me[i]);
    int l=mxCnt,r=1000,mid;
    while(l<r){
      mid=l+(r-l)/2;
      if(prom(mid)<=1000)r=mid;
      else l=mid+1;
    }
    printf("Case #%d: %d %d\n",C,l,prom(l));
  }
}



