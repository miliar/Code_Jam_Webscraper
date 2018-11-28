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
#include <set>
#include <iomanip>

#define FOR(i, a, b) for(int i=(a);i<=(b);i++)
#define FORD(i, a, b) for(int i=(a);i>=(b);i--)
#define REP(i, b) for(int i=0;i<(b);i++)
#define ll long long
#define nl printf("\n")
#define pb push_back
#define ff first
#define ss second
#define mp make_pair
const char en='\n';

//debug
#define debug 0
#define dbg(x) if(debug) cout<<#x<<"="<<(x)<<endl;

using namespace std;

template <class T, class U>
ostream& operator<<(ostream& out, const pair<T, U>&par) {
    out<<par.ff<<" "<<par.ss<<en;
    return out;
}
template <class T>
ostream& operator<<(ostream& out, const vector<T>& v) {
    REP(i, v.size()){if(i) out<<" ";cout<<v[i];}
    return out;
}

typedef long double ld;

int main(){
    //string m;
    ll t;
    ll n, k, d, m, c;
    ll a, b, h, w, p;
    cin>>t;
    for (int tt = 0; tt < t; tt++){
        cout<<"Case #"<<(tt+1)<<": ";
        cin>>n>>p;

        vector<int> pocty(4);

        REP(i,n){
            cin>>a;
            pocty[(p-a%p)%p]++;
        }

        ll odp = 0;
        odp+=pocty[0];

        if(p == 2){
            odp+=pocty[1]/2 + pocty[1]%2;
        }
        else if(p == 3){
            a = min(pocty[1], pocty[2]);
            odp+=a;
            pocty[1]-=a;
            pocty[2]-=a;

            odp+=pocty[1]/3 + (pocty[1]%3 > 0 ? 1 : 0);
            odp+=pocty[2]/3 + (pocty[2]%3 > 0 ? 1 : 0);
        }
        else if(p==4){
            a = min(pocty[1], pocty[3]);
            odp+=a;
            pocty[1]-=a;
            pocty[3]-=a;
            odp += pocty[2]/2;
            pocty[2]=pocty[2]%2;

            a = max(pocty[1], pocty[3]);
            if(pocty[2] == 1 && a >= 2){
               odp++;
                a-=2;
                pocty[2]--;
            }

            odp+=a/4;
            a%=4;

            if(pocty[2]>0 || a>0) odp++;
        }

        cout<<odp<<endl;
    }
}