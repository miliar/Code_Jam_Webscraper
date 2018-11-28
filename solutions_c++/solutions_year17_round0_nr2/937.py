#include <bits/stdc++.h>
using namespace std;
int cas;
int T;
using ll=long long;
/////////////////////////////////////////////////////

const int N=25;
// ll a[N];
vector<ll> a;


int main(){

    for(cin>>T; T--; ){
        printf("Case #%d: ", ++cas);
        /////////////////////////////////////
        ll n;
        cin >> n;
        a.clear();
        for(ll x=n; x; a.push_back(x%10), x/=10);
        reverse(a.begin(), a.end());
        ll res=0;

        for(int i=0; i<=a.size(); i++)
            if((i<a.size() && a[i]) || i==a.size()){
                bool f=true;
                for(int j=1; j<i; j++)
                    if(a[j]<a[j-1]){
                        f=false;
                        break;
                    }

                if(i>0 && i<a.size() && a[i]-1<a[i-1])
                    f=false;

                if(f){
                    ll t=0;
                    for(int j=0; j<a.size(); j++){
                        t*=10;
                        if(j==i)
                            t+=a[j]-1;
                        else if(j<i)
                            t+=a[j];
                        else t+=9;
                    }
                    res=max(res, t);
                }
            }
        cout << res << endl;
    }
    return 0;
}