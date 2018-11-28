#include <bits/stdc++.h>

using namespace std;

#define pb push_back
#define mp make_pair
#define rep(i,s,n) for(int i = (s); (n) > i; i++)
#define REP(i,n) rep(i,0,n)

typedef long long int ll;
typedef vector< pair<int,int> > vii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<long long int> vll;
typedef pair<int,int> pii;

const ll INF= ll (1e18);
const int MOD= 1e9+7;

int main()
{


	int t;
	cin>>t;
	REP(cc, t) {
		int n, d;
		cin>>d>>n;

		vector<float> tt(n);

		REP(i, n) {
			int k, s;
			cin>>k>>s;

			tt[i] = (double)(d - k) / s;
		}
		sort(tt.begin(),tt.end(), greater<float>());
		printf("Case #%d: %lf\n", cc+1, (double)((float)d/tt[0]));
	}





}
