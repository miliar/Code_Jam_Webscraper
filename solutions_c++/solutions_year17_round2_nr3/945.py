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
#include <tuple>

#define FOR(i, a, b) for(int i=(a);i<=(b);i++)
#define FORD(i, a, b) for(int i=(a);i>=(b);i--)
#define REP(i, b) for(int i=0;i<(b);i++)
#define ll long long
#define nl printf("\n")
#define kon_type pair<ld, pair<int, pair<int, ll> > >

// M_PI SI TREBA ODLOZIT

using namespace std;

typedef long double ld;

int main(){
    //string m;
    int t;
    int q, n;
    cin>>t;
    for (int tt = 0; tt < t; tt++){
        cout<<"Case #"<<(tt+1)<<":";
        cin>>n>>q;
        vector<pair<int,int> > horses(n);
        vector<vector<int> > dist(n, vector<int>(n));
        int e,s, u, v;
        REP(i, n){
            cin>>e>>s;
            horses[i] = make_pair(e,s);
        }

        REP(i, n){
            REP(j, n){
                cin>>e;
                dist[i][j] = e;
            }
        }

        REP(i, q){
            cin>>u>>v;
            u--; v--;
            // ci bol kon i, v meste j
            vector<vector<bool> > vypusteny(n, vector<bool>(n, false));
            // ubehnuty cas, index_kona, index_mesta_kam, zostatok_drahy
            priority_queue<kon_type, vector<kon_type>, std::greater<kon_type> > kone;
            kon_type novy_kon = make_pair(0, make_pair(u, make_pair(u, horses[u].first)));
            kone.push(novy_kon);

            while(kone.size()){
                auto dobehnuty_kon = kone.top();
                kone.pop();
                auto kam_prisiel = dobehnuty_kon.second.second.first;
                auto kon_cislo = dobehnuty_kon.second.first;
                //cout<<kon_cislo<<" ";
                //cout<<kam_prisiel<<" ";
                //nl;
                if(kam_prisiel == v){
                    cout<<std::fixed    <<std::setprecision(12)<<" "<<dobehnuty_kon.first;
                    break;
                }
                if(vypusteny[kon_cislo][kam_prisiel]){
                    continue;
                }
                vypusteny[kon_cislo][kam_prisiel] = true;
                REP(j, n){
                    auto vzd = dist[kam_prisiel][j];
                    auto novy_ubehnuty_cas = dobehnuty_kon.first + (vzd/(ld)horses[kon_cislo].second);
                    auto zostatok_vzd = dobehnuty_kon.second.second.second - vzd;
                    if(vzd != -1 && zostatok_vzd >= 0 && !vypusteny[kon_cislo][j]){
                        novy_kon = make_pair(novy_ubehnuty_cas, make_pair(kon_cislo, make_pair(j, zostatok_vzd)));
                        kone.push(novy_kon);
                    }
                }
                if(!vypusteny[kam_prisiel][kam_prisiel]){
                   // cout<<"pushujem "<<kam_prisiel<<" "<<dobehnuty_kon.first <<endl;
                    novy_kon = make_pair(dobehnuty_kon.first, make_pair(kam_prisiel, make_pair(kam_prisiel, horses[kam_prisiel].first)));
                    kone.push(novy_kon);
                }
            }
        }
        cout<<endl;

    }
}