#include <iostream>
#include <iomanip>

using namespace std;

int nt,s[110],e[110],n,q;
long long a[110][110];
double dis[110][110];

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin >> nt;
	for (int _=1;_<=nt;_++)
	{
		cin >> n >> q;
		for (int i=1;i<=n;i++)
			cin >> e[i] >> s[i];
		for (int i=1;i<=n;i++)
			for (int j=1;j<=n;j++)
		{
			cin >> a[i][j];
			if (a[i][j]==-1) a[i][j]=1e18+7;
		}
		for (int k=1;k<=n;k++)
			for (int i=1;i<=n;i++)
				for (int j=1;j<=n;j++)
					a[i][j]=min(a[i][j],a[i][k]+a[k][j]);
		for (int i=1;i<=n;i++)
			for (int j=1;j<=n;j++)
				dis[i][j]=1e18;
		for (int i=1;i<=n;i++)
			for (int j=1;j<=n;j++)
				if (a[i][j]<=e[i]) dis[i][j]=(double)a[i][j]/(double)s[i];
		for (int k=1;k<=n;k++)
			for (int i=1;i<=n;i++)
				for (int j=1;j<=n;j++)
					dis[i][j]=min(dis[i][j],dis[i][k]+dis[k][j]);
		cout << "Case #" << _ << ": ";
		cout << setprecision(9);
		cout << fixed;
		for (int i=1;i<=q;i++)
		{
			int u,v;
			cin >> u >> v;
			cout << dis[u][v]<< " ";
		}
		cout << "\n";
	}
}