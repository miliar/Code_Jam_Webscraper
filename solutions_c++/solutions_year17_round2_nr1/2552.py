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

void solve(int wc)
{
     int d,n; cin>>d>>n;
     vector<pair<int,int> > h(n);
     REP(i,n) {int a,b; cin>>a>>b; h[i]=make_pair(a,b);}
     //sort(ALL(h));
     //REP(i,n) cout<<h[i].first<<" "<<h[i].second<<endl;
     
     vector<double> ts(n);
     REP(i,n) ts[i] = ((double) d - (double)h[i].first)/(double)h[i].second;
   
    // REP(i,n) cout<<ts[i]<<endl;
     
     double tm = 0; REP(i,n) tm = max(tm,ts[i]);
     
     double v = (double)d /tm;
     
     cout<<"Case #"<<(wc+1)<<": "<<fixed<<setprecision(6)<<v<<endl;

}

int main(){
    int g; cin>>g;
    REP(w,g) solve(w);
    return 0;
}
