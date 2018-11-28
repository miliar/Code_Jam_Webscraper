using namespace std;

#include<bits/stdc++.h>

#define ll long long


int main(void)
{
    ///ios::sync_with_stdio(false);
    ///cin.tie(NULL);
    ///cout.tie(NULL);
    map<char, char> rev = {{'+','-'}, {'-','+'}};

    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);

    ll T, N;
    cin>>T;

    for(int iter=1; iter<=T; iter++){
        string str;
        cin>>str>>N;
        bool key = true;
        ll ans = 0, idx = 0, n = str.size();

        while(idx<n){
            while(idx<n && str[idx]=='+') idx++;
            if(idx>=n) break;

            ll lim = idx + N;
            if(lim>n){key = false; break; }
            else ans++;

            for(int j=idx; j<lim; j++) str[j] = rev[str[j]];
            ///cout<<idx<<" : "<<str<<"\n";
        }

        if(key) cout<<"Case #"<<iter<<": "<<ans<<"\n";
        else cout<<"Case #"<<iter<<": IMPOSSIBLE\n";
    }

return 0;
}
