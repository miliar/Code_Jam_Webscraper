#include <string>
#include <sstream>
#include <vector>
#include <iostream>
#include <stack>
#include <queue>
#include <array>
#include <algorithm>
#include <cmath>
#include <complex>
#include <map>
#include <cassert>
#include <functional>
#include <stdarg.h>
#include <iomanip>

#define FOR(i, a, b) for(int i=(a);i<=(b);i++)
#define FORD(i, a, b) for(int i=(a);i>=(b);i--)
#define REP(i, b) for(int i=0;i<(b);i++)
#define ll long long
#define nl printf("\n")

// M_PI SI TREBA ODLOZIT

using namespace std;

typedef long double ld;

int main(){
    //string m;
    int t;
    ll n, k;
    cin>>t;
    for (int tt = 0; tt < t; tt++){
        cout<<"Case #"<<(tt+1)<<": ";
        cin>>n>>k;
        ld max_time = 0;
        ll ri, hi;
        vector<pair<ll, ll> > pancs;
        REP(i, n){
            cin>>ri>>hi;
            pancs.push_back(make_pair(ri,hi));
        }

        ll best_sucet = 0;

        REP(spodok, n){
            ll sucet = 0;
            ll k2 = k;

            priority_queue<ll> to_delete;

            REP(i,n){
                if(i != spodok && pancs[i].first <= pancs[spodok].first){
                    sucet += pancs[i].first * pancs[i].second;
                    to_delete.push(-(pancs[i].first * pancs[i].second));
                }
            }

            while(to_delete.size() > k - 1){
                sucet+=to_delete.top();
                to_delete.pop();
            }

            if(to_delete.size() == k - 1){
                sucet*=2;
                sucet+=pancs[spodok].first*pancs[spodok].first;
                sucet+=pancs[spodok].first*pancs[spodok].second*2;
                best_sucet = max(sucet, best_sucet);
                //cout<<sucet<<endl;
            }
        }

        cout<<std::fixed    <<std::setprecision(12)<<best_sucet * M_PI<<endl;
    }
}