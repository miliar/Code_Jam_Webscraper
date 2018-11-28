#include <bits/stdc++.h>
#define ll long long
#define mp make_pair
#define PI 3.1413916333897931384616433831
#define MOD 1000000007
#define MOD1 1000000009
#define bas 19
#define bas1 19
using namespace std;
int main()
{
    freopen("in","r",stdin);
    freopen("outp","w",stdout);
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    ll t ;
    cin>>t;

    ll n , k ;
    for(int u = 1 ; u <= t ; u++){
        cin>>n>>k;
        vector<pair<ll,ll> > a ;
        ll need = k ;
        ll left = 0;
        ll right = 0 ;
        a.push_back(mp(n,1));
        bool done = true;

        while(true){
         ll in = 0 ;
        ll ma = -1 ;
            for(int j = 0 ; j < a.size() ; j++){
                if(a[j].first > ma && a[j].second > 0){
                    ma = a[j].first;
                    in = j ;
                }
            }
            if(need <= a[in].second){
                done = false;
                if(a[in].first % 2 == 1){
                    left = a[in].first / 2 ;
                    right = a[in].first / 2 ;
                }else {
                    right = a[in].first/2 ;
                    left = a[in].first/2 - 1;
                }
                break;
            }else {
                need -= a[in].second;

                if(a[in].first % 2 == 1){
                    bool here = true;
                    for(int l = 0 ; l < a.size() ; l++){
                        if(a[l].first == a[in].first / 2){
                            a[l].second += a[in].second * 2 ;
                            a[in].second = 0 ;
                            here = false;
                            break;
                        }
                    }
                    if(here){
                        a.push_back(mp(a[in].first / 2 , a[in].second * 2));
                        a[in].second = 0 ;
                    }
                }else {

                    ll lef = a[in].first /2 ;
                    ll ri = a[in].first / 2 - 1 ;
                    bool here = true;
                    for(int l = 0 ; l < a.size() ; l++){
                        if(a[l].first == lef){
                            a[l].second += a[in].second;
                            here = false;
                            break;
                        }
                    }
                    if(here){
                        a.push_back(mp(lef, a[in].second));
                    }
                    here = true;
                    for(int l = 0 ; l < a.size() ; l++){
                        if(a[l].first == ri){
                            a[l].second += a[in].second;
                            here = false;
                            break;
                        }
                    }
                    if(here){
                        a.push_back(mp(ri, a[in].second));
                    }
                    a[in].second = 0 ;
                }

            }
        }
        cout<<"Case #"<<u<<": "<<max(left,right)<<" "<<min(left,right)<<endl;
    }

}
