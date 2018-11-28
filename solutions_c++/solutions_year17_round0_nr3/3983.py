#include<iostream>
#include<algorithm>
#include<set>
#include<string>
#include<cmath>
#include <iomanip> 
#include<map>
#include<vector>
#define PB push_back
#define ALL(v) v.begin(),v.end()
#define REP(i,n) for(int i=0;i<n;++i)
#define REPD(i,n) for(int i=n;i>=0;--i)
#define FOR(i,j,k) for(int i=j;i<k;++i)
#define LL long long int
using namespace std;

LL getS (LL k,LL n)
{
   if(k==1) return n;
   LL h = (LL) log2(k);
     
   LL s = (LL) (n/h);
   return s;
}

void solve(int wc)
{
     LL n,k; cin>>n>>k;
     
     LL h = 0; if(k>1) h = (LL) log2(k);
     LL lfs = (LL) pow(2.0,(double)h);
     LL left = n - (lfs-1);
     LL bs = (LL) left / lfs;
     LL ups = left - (bs *lfs);
     LL idx = k - lfs;
     LL s = bs;
     if(idx<ups) ++s;
     
     LL l = s/(LL)2;
     LL r = s/(LL)2;
     if(s%2==0) --l;
     
     cout<<"Case #"<<(wc+1)<<": "<<max(l,r)<<" "<<min(l,r)<<endl;
}

int main(){
    int g; cin>>g;
    REP(w,g) solve(w);
    return 0;
}
