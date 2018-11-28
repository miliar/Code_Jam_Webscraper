#include <bits/stdc++.h>
#define MAXN 10000

using namespace std;

typedef long long int ll;

bitset<MAXN+3> v;

int n, K;
int vmin[MAXN+2];
int vmax[MAXN+2];

void atualiza2(int node)
{
	int cont=0;
	for(int i=node; i>=0; i--)
	{
		if(v[i]==1)
		{
			vmin[node]=(cont-1);
			break;
		}
		else cont++;
	}
}

void atualiza(int node)
{
	int cont=0;
	if(v[node]==1)
	{
		vmin[node]=vmax[node]=0;
		return;
	}
	for(int i=node; i<(n+2); ++i)
	{
		if(v[i]==1)
		{
			vmax[node]=(cont-1);
			break;
		}
		else cont++;
	}
	return;
}

int main() {
	// freopen("c.in", "r", stdin);
	// freopen("c2.txt", "w", stdout);
	int t;
	int caso=1;
	int maximum=0;
	int minimum=0;
	scanf("%d", &t);
	while(t--)
	{
		scanf("%d", &n);
		scanf("%d", &K);
		if(K==1)
		{
			if(n%2==0)
				printf("Case #%d: %d %d\n",caso++, n/2, n/2-1);
			if(n%2==1)
				printf("Case #%d: %d %d\n",caso++, (n-1)/2, (n-1)/2);
			continue;
		}
		v[0]=1;
		v[n+1]=1;
		for(int i=1; i<=n; i++)
			v[i]=0;
		for(int i=1; i<=n; i++)
			atualiza(i), atualiza2(i);
		int rounds=K;
		for(int k=0; k<rounds; k++)
		{
			int resposta=0;
			maximum=0;
			minimum=0;
			for(int j=1; j<=n; j++)
			{
				if(min(vmin[j], vmax[j]) > minimum)
				{
					resposta=j;
					maximum=max(vmin[j], vmax[j]);
					minimum=min(vmin[j], vmax[j]);
				}
				else if(min(vmin[j], vmax[j]) == minimum)
				{
					if(max(vmin[j], vmax[j]) > maximum)
					{
						resposta=j;
						maximum=max(vmin[j], vmax[j]);
						minimum=min(vmin[j], vmax[j]);
					}
				}
			}
			if(minimum==0 && maximum==0) break;
			v[resposta]=1;
			for(int i=1; i<=n; i++)
				atualiza(i), atualiza2(i);
		}
		printf("Case #%d: %d %d\n",caso++, maximum, minimum);
	}
	return 0;
}
