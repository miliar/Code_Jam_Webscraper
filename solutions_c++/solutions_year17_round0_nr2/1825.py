#include "bits/stdc++.h"
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
#define rep(i,n) for(ll i=0;i<(ll)(n);i++)
#define all(a)  (a).begin(),(a).end()
#define pb emplace_back
#define INF (1e9+1)
//#define INF (1LL<<59)

string norm(string s){
    string ret = "";
    bool f = false;
    rep(i,s.size()){
        if(!f&&s[i]=='0')continue;
        f = true;
        ret+=s[i];
    }
    if(ret.size()==0)return "0";
    return ret;
}

int main(){
    int n;
    cin>>n;
    rep(t,n){
        string s;
        cin>>s;
        
        ll ans = 0;
        const auto eval = [](string s){
            rep(i,s.size()-1){
                if(s[i]>s[i+1])return false;
            }
            return true;
        };
        
        
        rep(i,s.size()){
            string t = s;
            if(t[i]==0)continue;
            t[i]--;
            for(int j=i+1;j<t.size();j++)t[j]='9';
            
            
            t = norm(t);
            if(eval(t)){
                ans = max(ans,stoll(t));
            }
        }
        if(eval(s))ans = max(ans,stoll(s));
        
        cout<<"Case #"<<t+1<<": ";
        cout<<ans<<endl;
    }
}