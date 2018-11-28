#include <bits/stdc++.h>

using namespace std;

struct horse
{
	int s;
	long double k;
	inline friend bool operator<(horse&x,horse&y)
	{
		return x.k<y.k;
	}
}h[1010],h1[1010];

int T;
int D,N;

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	
	scanf("%d",&T);
	for(int tt=1;tt<=T;tt++)
	{
		scanf("%d%d",&D,&N);

		for(int i=1;i<=N;i++)
		{
			int K;
			scanf("%d%d",&K,&h[i].s);
			h[i].k=(long double)K;
		}

		N++;
		h[N].k=(long double)D;h[N].s=0;
		int n=N;

		sort(h+1,h+N+1);

		long double time=(long double)0.0;
		long double ans=(long double)1e20;

		for(int i=1;i<N;i++)
		{
			if(n==1)break;

			long double m=(long double)1e10;

			for(int j=1;j<n;j++)
			{
				if(h[j].s>h[j+1].s)
					if((long double)(h[j+1].k-h[j].k)/(h[j].s-h[j+1].s)<m)
					{
						m=(long double)(h[j+1].k-h[j].k)/(h[j].s-h[j+1].s);
					}
			}
			for(int j=1;j<=n;j++)
				h[j].k+=(long double)m*h[j].s;
			time+=m;

			int nn=0;
			for(int j=1;j<=n;j++)
				if(j==n||h[j].k+(long double)1e-15<h[j+1].k)
					h1[++nn]=h[j];
			for(int j=1;j<=nn;j++)
				h[j]=h1[j];
			n=nn;

			ans=min(ans,(long double)h[1].k/time);
		}

		printf("Case #%d: %.10f\n",tt,(double)ans);
	}

	return 0;
}
/*
3
2525 1
2400 5
300 2
120 60
60 90
100 2
80 100
70 10
*/