#include <bits/stdc++.h>
using namespace std;

typedef int64_t ll;
typedef vector<ll> vi;
typedef vector<bool> vb;
typedef vector<vi> vvi;
typedef pair<ll, ll> ii;
typedef vector<ii> vii;
typedef vector<vii> vvii;
typedef set<ii> sii;
typedef queue<ll> q;

#define FOR(i,n) for(i=0;i<n;i++)
#define all(a) a.begin(), a.end()
#define endl '\n'
#define pb push_back
#define mp make_pair
#define F first
#define S second



int main(){

	#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	#endif

    ll t,D,N,i,j,c;

    cin>>t;
    c = t;
    while(t--){
        cin>>D>>N;
        ll k,s;
        float ans=-1;
        FOR(i,N){
            cin>>k>>s;
            if(ans == -1)
                ans = float(D*s)/float(D-k);
            else
                ans = min(ans, float(D*s)/float(D-k));
        }
        cout<<"Case #"<<(c-t)<<": ";
        cout<<fixed<<setprecision(9)<<ans<<endl;
    }

    
	return 0;	
}