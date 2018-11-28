#include <bits/stdc++.h>
using namespace std;
#define pb push_back
#define pi pair<ll,ll>
#define pii pair<pi, ll>
#define f first
#define s second
#define ll long long
#define rep(i,n) for(int i=0;i<n;i++)
#define fre freopen("in.txt","r",stdin)
int cnt = 1;
void print(string s) {
    cout << "Case #"<<cnt<<": "<<s<<"\n";
    cnt++;
}
void print(ll x) {
    cout << "Case #"<<cnt<<": "<<x<<"\n";
    cnt++;
}
bool tidy(vector<int>&S) {
    for(int i=1;i<S.size();i++) {
        if(S[i]<S[i-1]) return 0;
    }
    return 1;
}
ll num(vector<int>&S) {
    ll ret = 0;
    for(auto x:S) {
        ret*=10;
        ret+=x;
    }
    return ret;
}
int main() {
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    cin >> t;
    while(t--) {
        ll N;
        cin >> N;
        vector<int>dig;
        while(N) {
            dig.pb(N%10);
            N/=10;
        }
        reverse(dig.begin(),dig.end());
        ll ans = 0;
        if(tidy(dig)) {
            ans = num(dig);
        }
        vector<int>S;
        rep(i,dig.size()) {
            if(dig[i]) {
                int f = 1;
                S.pb(dig[i]-1);
                for(int j=i+1;j<dig.size();j++) S.pb(9),f++;
                if(tidy(S))
                    ans = max(ans,num(S));
                while(f--) S.pop_back();
            }
            if(S.size()!=0 and S.back() > dig[i]) break;
            S.pb(dig[i]);
        }
        print(ans);
    }
}
