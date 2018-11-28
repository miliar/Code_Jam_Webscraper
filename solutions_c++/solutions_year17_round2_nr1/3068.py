#include <bits/stdc++.h>

#define ll long long int

#define pb push_back
#define mp make_pair
#define F first
#define S second

#define DEBUG(x) cout << '>' << #x << ':' << x << endl;
#define REP(i,n) for(ll i=0;i<(n);i++)
#define FOR(i,a,b) for(ll i=(a);i<=(b);i++)
#define FORD(i,a,b) for(ll i=(a);i>=(b);i--)
#define all(v) (v).begin(),(v).end()

using namespace std;
///////////////////////////////////////////////////////

long double t,d,n;
long double pos[1010];
long double speed[1010];

int main()
{
    std::ios::sync_with_stdio(false);
    cin.tie(0);

    cin>>t;
    FOR(z,1,t){
    	cin>>d>>n;

    	FOR(i,1,n){
    		cin>>pos[i]>>speed[i];
    	}

    	long double max_time=-1;

    	FOR(i,1,n){
    		if(max_time<(d-pos[i])/speed[i]){
    			max_time = (d-pos[i])/speed[i];
    		}
    	}

    	cout<<"Case #"<<z<<": "<<setprecision(6)<<fixed<<(d*1.0)/max_time<<endl;
    }
}
