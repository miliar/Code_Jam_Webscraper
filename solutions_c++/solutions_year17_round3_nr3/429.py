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
        ld u;
        cin>>u;
        vector<ld > cores(n);
        REP(i, n){
            cin>>cores[i];
        }

        sort(cores.begin(), cores.end());
        int ncount = 0;
        ld last = 0;
        int i = 0;
        for (i; i < n; i++){
            if((cores[i] - last) * ncount <= u){
                u-=(cores[i] - last) * ncount;
            }
            else {
                break;
            }
            last = cores[i];
            ncount++;
        }
        if(i == n){
            if((1 - last) * n < u){
                u-=(cores[i] - last) * n;
            }
        }
        ld pridat = u/i;
        ld chance = 1;
        //cout<<pridat<<" "<<u<<" "<<i<<" "<<n<<endl;
        REP(j, i){
            cores[j] = last + pridat;
        }
        REP(j, n){
            if(cores[j] < 1){
                chance*= cores[j];
            }
        }

        cout<<std::fixed    <<std::setprecision(12)<<chance<<endl;
    }
}