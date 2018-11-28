/* 
	author: Bhrigu Gupta
		aka “bhrigudov”
*/

#include <bits/stdc++.h>

using namespace std;

#define fo(i,a,b) for(i=a;i<b;i++)
#define rf(i,b,a) for(i=b; i>=a; i--)
#define tr(c, i) for(auto i= c.begin(); i!= c.end(); i++) 
#define pb push_back
#define mp make_pair
#define ub upper_bound
#define lb lower_bound
#define inp(str) getline(cin, str)
#define INF 1e11
#define MX 200002

typedef long long ll;
typedef vector<int> vi;

int main(int argc, char const *argv[])
{
	ios_base::sync_with_stdio(false); 

	int n, i, j, t, k, temp;
	int st[MX], D, v[MX];

	cin>>t;
	fo(k,1,t+1)
	{
		long double t, temp, ans;
		t = 0;

		cin>>D>>n;
		fo(i,1,n+1) {
			cin>>st[i]>>v[i];
			temp = ((long double)(D-st[i]))/v[i];
			t = max(t, temp);
		}

		ans = ((long double)D)/t;

		cout<<"Case #"<<k<<": "<<fixed<<setprecision(8)<<ans<<"\n";
	}

	return 0;
}