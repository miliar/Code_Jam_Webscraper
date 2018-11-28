// template.cpp : Defines the entry point for the console application.
//
#include <climits>
#include <cstdio>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <stack>
#include <queue>
#include <list>
#include <tuple>
#include <ctime>
#include <cassert>
#include <cstring>
using namespace std;


//type shortcuts
typedef long long ll;
typedef vector<ll> VI;
typedef long double DOUBLE;
typedef vector<DOUBLE> VD;
typedef vector<VD> VVD;


//constants
const DOUBLE EPS=1e-9;
const DOUBLE PI = atan(1) * 4;
const ll M = 1000000007;

//for-loop shortcut
#define rng(i,begin,end) for (ll i=begin;i<end;++i)


//scanf shortcuts
void scanll(ll &x) {ll r;scanf("%lld",&r);x=r;}
void scanstr(char *buf){scanf("%s",buf);}


char buf[1001];
int main()
{
    ll tn;
    scanll(tn);
    rng(ti,0,tn){
        ll k;
        scanstr(buf);scanll(k);
        ll n=strlen(buf);
        ll ans=0;
        rng(i,0,n-k+1){
            if (buf[i]=='-'){
                ans++;
                rng(j,i,i+k){
                    buf[j]=(buf[j]=='+')?'-':'+';
                }
            }
        }
        rng(i,n-k+1,n){
            if (buf[i]=='-') {ans=-1;break;}
        }
        printf("Case #%lld: ",ti+1);
        if (ans<0) printf("IMPOSSIBLE\n"); else printf("%lld\n",ans);
    }
    return 0;
}
