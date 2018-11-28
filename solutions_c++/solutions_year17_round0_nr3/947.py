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
        ll n,k;
        scanll(n);scanll(k);

        priority_queue<ll> hp;
        set<ll> inhp;
        map<ll,ll> v2c;

        hp.push(n);
        v2c[n]=1;
        inhp.insert(n);

        while (true){
            ll v=hp.top();
            ll newv=v/2;
            ll newv2=(v-1)/2;
            ll c=v2c[v];
            if (c>=k){
                printf("Case #%lld: %lld %lld\n",ti+1,newv,newv2);
                break;
            }
            k-=c;
            hp.pop();
            v2c.erase(v);
            inhp.erase(v);
            if (newv>0){
                if (inhp.find(newv)==inhp.end()) {
                    inhp.insert(newv);
                    hp.push(newv);
                }
                v2c[newv]+=c;
            }
            if (newv2>0){
                if (inhp.find(newv2)==inhp.end()){
                    inhp.insert(newv2);
                    hp.push(newv2);
                }
                v2c[newv2]+=c;
            }
        }

    }
    return 0;
}
