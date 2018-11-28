#include <bits/stdc++.h>
#define pb push_back
#define sqr(x) (x)*(x)
#define sz(a) int(a.size())
#define reset(a,b) memset(a,b,sizeof(a))
#define oo 1000000007

using namespace std;

typedef pair<int,int> pii;
typedef long long ll;

int main(){
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int T;
    cin>>T;
    for(int tt=1; tt<=T; ++tt){
        cout<<"Case #"<<tt<<": ";
        ll n;
        cin>>n;
        stringstream ss;
        ss<<n;
        string s=ss.str();
        int i=0;
        while(i<sz(s)-1 && s[i+1]>=s[i]) ++i;
        if(i==sz(s)-1) cout<<s<<endl;
        else{
            int j=i;
            while(j>0 && s[j-1]>=s[j]) --j;
            --s[j];
            for(i=j+1; i<sz(s); ++i) s[i]='9';
            ll res=0;
            for(int i=0; i<sz(s); ++i) res=res*10+s[i]-'0';
            cout<<res<<endl;
        }
    }
}
