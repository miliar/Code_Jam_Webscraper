#include <bits/stdc++.h>
#define lli long long int
#define pr pair<int, int> 
#define mk make_pair
#define pb push_back
using namespace std;

bool mycompare(const pr &a,const pr &b)
{
	return(a.first > b.first);
}

double calc(double D, vector<pr> v ,int N)
{
    double newdist,ttkn,sametime= 0;
    for(int i = 0; i<N ; i++)
	{
		newdist = D - v[i].first;
		ttkn = newdist/(double)v[i].second;
		if(ttkn >= sametime)
			sametime = ttkn;
	}
	return sametime;
}
int main()
{
	int T;
	scanf("%d",&T);
	int Case = 1;
	while(T--)
	{
		int N, D , k , tm;
		scanf("%d %d",&D,&N);	
		vector< pr >v;
		for(int i = 0 ; i < N;i++)
		{
			scanf("%d %d",&k,&tm);
			v.pb(mk(k,tm));
		}
		sort(v.begin(),v.end(),mycompare);
		double res  = D / (double)calc(D, v,N);
		printf("Case #%d: %.6f\n",Case, res);
		Case++;
	}
	return 0;
}

