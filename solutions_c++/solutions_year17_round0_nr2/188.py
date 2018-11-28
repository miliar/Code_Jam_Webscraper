#include<bits/stdc++.h>
using namespace std;

#define int long long

typedef vector<int>vint;
typedef pair<int,int>pint;
typedef vector<pint>vpint;
#define rep(i,n) for(int i=0;i<(n);i++)
#define reps(i,f,n) for(int i=(f);i<(n);i++)
#define all(v) (v).begin(),(v).end()
#define each(it,v) for(__typeof((v).begin()) it=(v).begin();it!=(v).end();it++)
#define pb push_back
#define fi first
#define se second
template<typename A,typename B>inline void chmin(A &a,B b){if(a>b)a=b;}
template<typename A,typename B>inline void chmax(A &a,B b){if(a<b)a=b;}

void solve(){
    string s;
    cin>>s;

    int p=-1;
    for(int i=0;i+1<s.size();i++){
        if(s[i]>s[i+1]){
            p=i;
            break;
        }
    }

    if(p==-1){
        cout<<s<<"\n";
        return;
    }

    while(p&&s[p-1]==s[p])p--;
    for(int i=p+1;i<s.size();i++)s[i]='9';
    s[p]--;

    stringstream ss(s);
    int d;
    ss>>d;
    cout<<d<<"\n";
}

signed main(){
    cin.tie(0);ios_base::sync_with_stdio(0);
    int T;
    cin>>T;
    rep(i,T){
        cout<<"Case #"<<i+1<<": ";
        solve();
    }
    return 0;
}
