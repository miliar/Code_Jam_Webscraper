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

bool isTidy(LL x)
{
     
     int last = 10;
     while(x>0){
                 int next = x%10;
                 if(next>last) return false;
                 last = next;
                 x/=10;
                }
     
     return true;
}

void solve(int wc)
{
     string s;cin>>s;
     cout<<"Case #"<<(wc+1)<<": ";
     vector<int> ret;
     
     REP(i,s.size())
     {
        int next = s[i]-'0';
        if(i==0 || next>=ret[ret.size()-1]) ret.PB(next);
        else
        {
            int idx = ret.size()-1;
            while(idx>=0)
            {
               ret[idx]--;
               if(idx>0 && ret[idx-1]>ret[idx]) --idx;
               else break;
            }
            
            if(ret[idx]==0)
            {
               REP(j,s.size()-1) cout<<9; cout<<endl; return;
            }
            else 
            { 
               REP(j,idx+1) cout<<ret[j];
               FOR(j,idx+1,s.size()) cout<<9; cout<<endl; return;
            }
        }
     }
     REP(i,ret.size()) cout<<ret[i];
      cout<<endl;
}

int main(){
    int g; cin>>g;
    REP(w,g) solve(w);
    return 0;
}
