#include <bits/stdc++.h>
using namespace std;
#define rep(a,b,c) for(int a=b;a<c;++a)
#define repeq(a,b,c) for(int a=b;a<=c;++a)
#define debug(x) cerr<<(#x)<<": "<<x<<endl
typedef long long ll;

int main()
{
	ios::sync_with_stdio(false);
    cin.tie(NULL);
	int T;
	cin >> T;
	repeq(testcase,1,T)
	{
		int N, P;
		cin >> N >> P;
		int r[50];
		rep(i,0,N)
			cin >> r[i];
		vector<vector<int> > ing(N);
		rep(i,0,N)
		{
			ing[i].resize(P);
			rep(j,0,P)
				cin >> ing[i][j];
			sort(ing[i].begin(),ing[i].end());
		}
		vector<int> front(N,0);
		bool done = false;
		int count = 0;
		while(!done)
		{
			int minservings = 1e9;
			int choosen = -1;
			rep(i,0,N)
			{
				int x = ing[i][front[i]];
				int servings = (10*x)/(9*r[i]);
				if(servings<minservings)
				{
					minservings = servings;
					choosen = i;
				}
			}
			bool ok = true;
			if(minservings==0)
				ok = false;
			for(int i=0;ok && i<N;++i)
			{
				int x = ing[i][front[i]];
				if(10*x>11*minservings*r[i])
					ok = false;
			}
			if(ok)
			{
				++count;
				rep(i,0,N)
				{
					++front[i];
					if(front[i]==P)
						done = true;
				}
			}
			else
			{
				++front[choosen];
				if(front[choosen]==P)
					done = true;
			}			
		}
		printf("Case #%d: %d\n",testcase,count);
	}
	return 0;
}
