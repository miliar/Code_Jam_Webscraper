// Dont hack this or I hack ur mama
#include <iostream>
#include <cstdio>
#include <vector>
#include <queue>
#include <map>
#include <string>
#include <algorithm>
#include <set>
#include <cmath>
#define ll long long 
#define ull unsigned long long
#define pb push_back
#define mp make_pair
#define EPS (1e-9)
using namespace std;

////////////// END OF TEMPLATE
int T,N;
vector < pair < int , int > > horse;
int D;
double eps = 1e-6;
void solve();
void read()
{
	
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	cin >> T;
	for(int i = 0 ; i < T; i++)
	{
		horse.clear();
		cin >> D >> N;
		for(int j = 0 ; j < N; j++)
		{
			pair < int , int > z;
			cin >> z.first >> z.second;
			horse.pb(z);

		}
		printf("Case #%d: ",i+1);
		solve();
	}
}
void solve()
{
	sort(horse.begin(),horse.end());
	double lastTime[1100];
	for(int i = 0 ; i < 1100; i++) lastTime[i] = 0.00000000;
	for(int i = N-1; i>=0; i--)
	{
		//cout << i << endl;
		if( i == N-1)
		{
			lastTime[i] = (D - horse[i].first) * 1.0 / (horse[i].second * 1.0);
		}else{
			double meeting = (D - horse[i].first) * 1.0 / (horse[i].second * 1.0);
			int j;
			for(j = i + 1; j < N; j++)
			{
				if(horse[i].second > horse[j].second) break;
			}
			if( j == N)
			{
				lastTime[i] = meeting;
				continue;
			}	
			meeting = ((horse[j].first - horse[i].first)*1.0)/((horse[i].second - horse[j].second)*1.0);
			//cout << j << 'x' << meeting << endl;
			if(meeting > lastTime[j])
			{
				lastTime[i] = (D - horse[i].first) * 1.0 / (horse[i].second * 1.0);		
			}else{
				lastTime[i] = lastTime[j];
			}
		}
		//cout << i << ' ' << lastTime[i] << endl; 
	}
	
	printf("%.6lf\n",(D*1.0)/lastTime[0]);
}

int main()
{
	std::ios::sync_with_stdio(false);
	read();
	return 0;
}
