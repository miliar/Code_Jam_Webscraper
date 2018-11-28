//Indomie, Mie dari Indonesia
#include <bits/stdc++.h>
using namespace std;
#define fi first
#define se second
#define mp make_pair
typedef long double LD;
typedef long long LL;
const LL INF=1000000000000LL;
const LD INFLD=1000000000000.0;
int tc,matriks[105][105],nodes,kecepatan[105],maksjarak[105],q;
LL jarak[105][105];
LD totalwaktu[105][105];
vector<pair<int,LD>> node[105];
void isijarak(){
	for(int i=1;i<=nodes;i++)
	{
		for(int j=1;j<=nodes;j++)
		{
			if(matriks[i][j]==-1)
				jarak[i][j]=INF;
			else
				jarak[i][j]=matriks[i][j];
		}
		jarak[i][i]=0;
	}
	for(int k=1;k<=nodes;k++)
		for(int j=1;j<=nodes;j++)
			for(int i=1;i<=nodes;i++)
				jarak[j][i]=min(jarak[j][i],jarak[j][k]+jarak[k][i]);
}
void buat_graph(){
	for(int i=1;i<=nodes;i++)
		node[i].clear();
	for(int i=1;i<=nodes;i++)
	{
		for(int j=1;j<=nodes;j++)
		{
			totalwaktu[i][j]=INFLD;
			if(i==j)
				continue;
			if(maksjarak[i]<jarak[i][j])
				continue;
			totalwaktu[i][j]=LD(jarak[i][j])/LD(kecepatan[i]);
		}
		totalwaktu[i][i]=0;
	}
}
void isi_waktu(){
	for(int k=1;k<=nodes;k++)
		for(int j=1;j<=nodes;j++)
			for(int i=1;i<=nodes;i++)
				totalwaktu[j][i]=min(totalwaktu[j][i],totalwaktu[j][k]+totalwaktu[k][i]);
}
int main()
{
	freopen("PonyBig.in","r",stdin);
	freopen("PonyBig.out","w",stdout);
	scanf("%d",&tc);
	for(int test=1;test<=tc;test++)
	{
		scanf("%d%d",&nodes,&q);
		for(int i=1;i<=nodes;i++)
			scanf("%d%d",&maksjarak[i],&kecepatan[i]);
		for(int i=1;i<=nodes;i++)
		{
			for(int j=1;j<=nodes;j++)
			{
				scanf("%d",&matriks[i][j]);
			}
		}
		isijarak();
		buat_graph();
		isi_waktu();
		printf("Case #%d: ",test);
		for(int i=1;i<=q;i++)
		{
			int u,v;
			scanf("%d%d",&u,&v);
			cout<<fixed<<setprecision(10)<<totalwaktu[u][v];
			if(i==q)
				cout<<endl;
			else
				cout<<" ";
		}
	}
}
