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


int main()
{
    ll tn;scanll(tn);
    rng(ti,0,tn){
        ll n;scanll(n);
        ll q;scanll(q);
        VI e(n);
        VI s(n);
        rng(i,0,n){
            scanll(e[i]);
            scanll(s[i]);
        }
        vector<vector<ll>> d(n,vector<ll>(n,-1));
        rng(i,0,n){
            rng(j,0,n){
                scanll(d[i][j]);
            }
        }

        VI accdis(n);
        accdis[0]=0;
        rng(i,1,n){
            accdis[i]=accdis[i-1]+d[i-1][i];
        }

        VI u(q);
        VI v(q);
        rng(i,0,q){
            scanll(u[i]);--u[i];
            scanll(v[i]);--v[i];
        }
        vector<double> ans(q);
        rng(i,0,q){
            vector<vector<double>> f(n,vector<double>(n,10000000000000));
            f[0][0]=0;
            rng(j,1,n){
                if (e[j-1]>=d[j-1][j]){
                    //f[j][j-1]=f[j-1][*]+d/s[j-1];
                    rng(k,0,n){
                        f[j][j-1]=min(f[j][j-1],f[j-1][k]+((double)d[j-1][j])/s[j-1]);
                    }
                }
                rng(k,0,n){
                    if (k==j-1) continue;
                    ll diskj=(k>=j)?10000000000000:(accdis[j]-accdis[k]);
                    if (e[k]<diskj) continue;
                    f[j][k]=min(f[j][k],f[j-1][k]+((double)d[j-1][j])/s[k]);
                }
            }
            double bst=f[n-1][0];
            rng(j,1,n){
                bst=min(bst,f[n-1][j]);
            }
            ans[i]=bst;
        }
        cout.precision(9);
        cout<<"Case #"<<(ti+1)<<":";
        rng(i,0,q){
            cout<<" "<<fixed<<ans[i];
        }cout<<endl;

    }
    return 0;
}
