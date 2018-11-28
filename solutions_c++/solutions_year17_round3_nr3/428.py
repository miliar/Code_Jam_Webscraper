#include <bits/stdc++.h>
#define D(x...) fprintf(stderr, x)
#define EPS 1E-8
using namespace std;
int T, N, K;
int main()
{ 
	freopen("infile.txt", "r", stdin);
	scanf("%d ", &T);
	for(int t=1; t<=T; t++)
	{  
		double C;
		double ans =1.0;
		scanf("%d %d %lf", &N, &K, &C);
		assert(N==K);
		vector<double> V; 
		for(int n=0; n<N; n++)
		{
			double x;
			scanf(" %lf", &x);
			V.push_back(x);
			ans*=x;
		}
		sort(V.begin(), V.end());
		reverse(V.begin(), V.end());
		for(int v=0; v<V.size(); v++)
		{
			double S =C;
			for(int a=v; a< V.size(); a++)
			{
				S+=V[a];
			}
			double avg = S/(V.size()-v);
			if(avg > 1) avg = 1;
			if(V[v] < avg-EPS)
			{
				double curans = 1;
				for(int a=0; a<v; a++)
				{
					curans*=V[a];
				}
				for(int a=v; a<V.size(); a++)
				{
					curans*=avg;
				}
				ans = max(ans, curans);
			}
		}
		printf("Case #%d: %.9lf\n", t, ans);
	}
}