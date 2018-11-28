#include<bits/stdc++.h>

using namespace std;

typedef struct{
	int start, speed;
} kuda;

kuda daftar[1200];

bool cmp(kuda a, kuda b)
{
	return a.start > b.start;
}

int main()
{
	int T;
	cin>>T;
	
	int D,N;
	for(int tc=1;tc<=T;tc++)
	{
		cin>>D>>N;
		for(int i=0;i<N;i++)
		{
			scanf("%d%d",&daftar[i].start,&daftar[i].speed);
		}
		sort(daftar,daftar+N,cmp);
		double ans = 0;
		for(int i=0;i<N;i++)
		{
			double x = (double)(D - daftar[i].start)/(double)daftar[i].speed;
			if(x>ans) ans = x;
		}
		printf("Case #%d: %.6lf\n", tc, (double)D/ans);
	}

	return 0;
}
