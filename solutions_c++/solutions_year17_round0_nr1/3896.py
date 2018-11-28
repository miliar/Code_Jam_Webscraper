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
#define LL long long
using namespace std;

void solve(int wc)
{
     string s; cin>>s;
     int p; cin>>p;
     int ret = 0;
     
     vector<int> c(s.size());
     REP(i,s.size()) if(s[i]=='+') c[i]=1; else c[i]=0;
     int n = c.size();
     REP(i,n)
     {
        if(c[i]==0 ) 
        {
                   if(n-i<p)
                   {
                          cout<<"Case #"<<(wc+1)<<": IMPOSSIBLE"<<endl;;
                          return;
                   }

                   ++ret;
                   FOR(j,i,i+p) if(c[j]==0) c[j]=1;else c[j]=0;
        }
        
     }
     
     cout<<"Case #"<<(wc+1)<<": "<<ret<<endl;
}

int main(){
 
    int g; cin>>g;
    REP(w,g) solve(w);
    return 0;
}
