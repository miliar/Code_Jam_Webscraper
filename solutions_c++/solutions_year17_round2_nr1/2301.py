#include "bits/stdc++.h"

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
    double d;
    int n;
    cin>>d>>n;
    vector < pii > A;
    double tmax = 0;
    for(int i=0;i<n;i++){
	int k,s;
	cin>>k>>s;
	A.pb(pii(k,s));
	double t1 = d - k;
	t1 /= (s*1.0);
	tmax = max(tmax,t1);
    }
    double ans = d/tmax;
    cout<<"Case #"<<cntr<<": ";
    printf("%.12lf\n",ans);
}
int main(){
    int t;
    cin>>t;
    while(t--){
	solve();
    }
    return 0;
}
