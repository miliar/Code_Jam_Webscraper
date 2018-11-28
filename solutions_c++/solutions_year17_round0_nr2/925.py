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
        ll n;scanll(n);
        VI d;
        while(n>0){
            d.push_back(n%10);
            n/=10;
        }
        ll l=d.size();
        VI x(l);
        ll st=0;
        ll last=0;
        rng(i,0,l){
            ll ii=l-1-i;
            if (st==1){
                x[ii]=9;
            }else if (d[ii]>=last){
                x[ii]=d[ii];
                last=d[ii];
            }else{
                //make |x[l-1]..x[ii+1]| < |d[l-1]..d[ii+1]|
                ll j=ii+1;
                while(true){
                    assert(x[j]>0);
                    x[j]--;
                    if (j==l-1) break;
                    if (x[j+1]<=x[j]) break;
                    x[j]=9;
                    j++;
                }
                x[ii]=9;
                st=1;
            }
        }
        ll ans=0;
        rng(i,0,l){
            ll ii=l-1-i;
            ans=ans*10+x[ii];
        }
        printf("Case #%lld: %lld\n",ti+1,ans);
    }
    return 0;
}
