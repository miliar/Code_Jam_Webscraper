#include<bits/stdc++.h>

using namespace std;

typedef struct{
	long long r, ha;
} panc;

//const double PI = atan(1.0)*4;
const double PI = 3.14159265358979323846264338327950288;
panc li[2000];

bool pertamax(panc a, panc b)
{
	if(a.r != b.r) return (a.r < b.r);
	else return (a.ha < b.ha);
}

bool cmp(panc a, panc b)
{
	return (a.ha < b.ha);
}

int main()
{
	int T;
	cin>>T;
	
	int N,K;
	int ra,he;
	for(int tc=1;tc<=T;tc++)
	{
		cin>>N>>K;
		for(int i=0;i<N;i++)
		{
			cin>>ra>>he;
			long long vertArea = ra;
			vertArea = vertArea*2*he;
			li[i].r = ra;
			li[i].ha = vertArea;
		}
		sort(li, li+N, pertamax);
		
		long long ans = 0;
		for(int i=K-1;i<N;i++)
		{
			long long temp = li[i].r*li[i].r + li[i].ha;
			if(i>0) sort(li,li+i,cmp);
			for(int j=i-1;j>=0 && j>i-K;j--)
			{
				temp += li[j].ha;
			}
			if(temp > ans) ans = temp;
		}
		printf("Case #%d: %.6lf\n", tc, (double)ans*PI);
	}
	

	return 0;
}
