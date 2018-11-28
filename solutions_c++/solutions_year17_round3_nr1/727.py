
/* 
Take yourself as work in progress.
-Bhai
*/

#include<bits/stdc++.h>
using namespace std;

#define M 1000000007
#define LL long long
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define VI vector<int>
#define SZ(a) int(a.size())
#define TR(c, it) for(typeof((c).begin()) it=(c).begin(); it!=(c).end(); it++ )
#define SET(a, b) memset(a, b, sizeof(a))

const int MAXN = 1000000;
pair<int, int> RH[MAXN+5];
set<double> s;

int N, K;

int main()
{
	ios_base::sync_with_stdio(0);
	int t;
	cin >> t;
	int  nahoy = 1;
	while(t--)
	{
		cin >> N >> K;
		s.clear();
		for(int i=0; i<N; i++)
			cin >> RH[i].F >> RH[i].S;
		
		sort(RH, RH+N);
		double ans = 0, now = 0;
		for(int i=0; i<K; i++)
		{
			//cout << RH[i].F << " " << RH[i].S << endl;
			s.insert(2.0 * double(RH[i].F) * double(RH[i].S));
			now += 2.0 * double(RH[i].F) * double(RH[i].S);
		}
		//cout << now << endl;
		now += double(RH[K-1].F)*double(RH[K-1].F);
		ans = now;

		//cout << ans << endl;
		double todel;
		for(int i=K; i<N; i++)
		{
			todel = *(s.begin());
			s.erase(s.begin());
			s.insert(2.0 * double(RH[i].F) * double(RH[i].S));
			//cout << todel << endl;
			now -= todel;
			now += 2.0 * double( RH[i].F) * double(RH[i].S);
			now += double(RH[i].F)*double(RH[i].F) - double(RH[i-1].F)*double(RH[i-1].F);
			//cout << now << endl;
			ans = max(ans, now);
		}
		//cout << ans << endl;
		//cout << ans * M_PI << endl;
		printf("Case #%d: %.14lf\n", nahoy, ans*M_PI);
		nahoy++;
	}
	return 0;
}
