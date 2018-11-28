#include <bits/stdc++.h>
#define D(x...) fprintf(stderr, x)
#define PI 3.14159265358979323846264338328
using namespace std;
int T;
int main()
{ 
	freopen("infile.txt", "r", stdin); 
	scanf("%d ", &T);
	for(int t=1; t<=T; t++)
	{
		int N, K;
		double R[1005];
		double H[1005];
		double ans =0;
		scanf("%d %d", &N, &K);
		for(int n=0; n<N; n++)
		{
			int r, h;
			scanf("%d %d", &r, &h);
			H[n]  = (double)h*2*(double)r*PI; 
			R[n] = r;
		}
		for(int n=0; n<N; n++)
		{
			vector<double> V;
			for(int a=0; a<N; a++)
			{
				if(a!=n && R[a] <= R[n])
				{
					V.push_back(H[a]);
				}
			}
			double curans = (double)R[n]*(double)R[n]*PI;
			curans+=H[n];
			if(V.size()>=K-1)
			{
				sort(V.begin(), V.end());
				reverse(V.begin(), V.end());
				for(int k=0; k<K-1; k++)
				{
					curans+=V[k];
				}
			}
			ans = max(ans, curans);
		}
		printf("Case #%d: %.9f\n", t, ans);
	}
}