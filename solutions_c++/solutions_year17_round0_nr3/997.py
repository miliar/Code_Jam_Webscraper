
#include "bits/stdc++.h"
#include "prettyprint.hpp"

using namespace std;

#define endl '\n'

#define si(x) scanf("%d",&x)
#define sl(x) scanf("%lld",&x)

#define all(x) x.begin(),x.end()
#define mp make_pair

#define ll long long
#define ld long double
#define pb push_back

#define MOD 1000000007

#define pi 2*acos(0)

#define fr first
#define se second

#define vi vector < int >
#define pii pair < int , int >
#define pll pair < ll , ll >

#define fast_io ios_base::sync_with_stdio(0);cin.tie(NULL)

#define LSB(x) x&-x
#define nb(x) __builtin_popcount(x)
int cntr = 0;
void solve(){
    cntr++;
    ll n,k;
    cin>>n>>k;
    ll a,b;
    ll n2 = 1;
    while(k>=n2){
	a = n/2;
	b = n-a-1;
	ll x = k&n2;
	n2<<=1;
	if(x==0)
	    n = a;
	else n = b;
    }
    cout<<"Case #"<<cntr<<": ";
    cout<<max(a,b)<<" "<<min(a,b)<<endl;
}
int main(){
    int t;
    cin>>t;
    for(int i=1;i<=t;i++){
	solve();
    }
    return 0;
}
