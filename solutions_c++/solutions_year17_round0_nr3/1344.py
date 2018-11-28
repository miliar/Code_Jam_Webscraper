#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

int main()
{
    freopen("C-large.in","r",stdin);
    freopen("BathLarge.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int I = 1 ; I <= t ; I++){
        ll n,k;
        cin >> n >> k;
        set<ll> s;
        map<ll,ll> m;
        s.insert(-n);
        m[n] = 1;
        while(k && s.size()){
            ll x = (*s.begin()) * -1;
            s.erase(s.begin());
            ll cnt = m[x];
            if(cnt >= k){
                printf("Case #%d: ",I);
                if(x%2 == 0){
                    cout << x/2 << " " << x/2-1 << "\n";
                }else{
                    cout << x/2 << " " << x/2 << "\n";
                }
                break;
            }else{
                k -= cnt;
                m[x] = 0;
                if(x%2 == 0){
                    m[x/2] += cnt;
                    s.insert(-1*(x/2));
                    if((x/2)-1 > 0)
                        m[x/2-1]+=cnt , s.insert(-1*(x/2-1));
                }else{
                    if(x/2 > 0){
                        m[x/2] += 2* cnt;
                        s.insert(-1 * (x/2));
                    }
                }
            }
        }
    }
    return 0;
}


