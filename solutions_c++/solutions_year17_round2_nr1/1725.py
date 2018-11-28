#include <bits/stdc++.h>

#define rep(i, n) for(ll i=0; i<n; i++)
#define all(x) x.begin(),x.end()
#define pb push_back
#define xx first
#define yy second
#define mp make_pair
#define mod 1000000007
#define st string
#define vi vector<int>
#define vs vector<st>
#define mii map<int,int>
#define pii pair<int,int>
#define vpii vector<pii>

typedef long long ll;
typedef unsigned long long ull;

using namespace std;

int main() {
	int t;
	cin>>t;
	for(int j = 0; j < t; j++) {
		ll d, n;
		cin>>d>>n;

		double maxTime = 0;
		
		double k, s, time = 0;
		rep(i, n) {
			cin>>k>>s;
			time = (d-k)/s;
			if(time > maxTime)
				maxTime = time;
		}

		printf("Case #%d: %.6f\n", j+1, (float)d/maxTime);
	}
	return 0;
}