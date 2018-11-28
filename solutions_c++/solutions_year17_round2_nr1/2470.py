#include <bits/stdc++.h>
using namespace std;

#define ll long long int
#define INF 0x3F3F3F3F
#define pii pair<int,int>
#define pll pair<long long int, long long int>
#define mp make_pair
#define pb push_back
#define vi vector<int>
#define vll vector<long long int>
#define vpii vector<pair<int,int> >
#define PI acos(-1.0)

int main(){
	//freopen("","r",stdin);
	//freopen("","w",stdout);
	int tc;
	cin >> tc;
	for(int kase=1; kase<=tc; kase++){
		int n,d;
		cin >> d >> n;
		vpii horses(n);
		vector<double> time;
		for(int i=0; i<n ;i++)
			cin >> horses[i].first >> horses[i].second;
		sort(horses.begin(),horses.end());
		
		for(int i=0; i<(int)horses.size() && horses[i].first<d; i++)
			time.pb(1.0*(d-horses[i].first)/horses[i].second);
			
		double maxTime = -1;
		for(int i=0; i<(int)time.size(); i++)
			maxTime = max(maxTime,time[i]);

		printf("Case #%d: %.7lf\n", kase, d/maxTime);	
		
	}
	
	return 0;
}
