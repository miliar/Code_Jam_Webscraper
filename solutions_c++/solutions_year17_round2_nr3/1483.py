#include <iostream>
#include <algorithm>
#include <iomanip>

#define INF 1000000000000ll

using namespace std;

void solve(int t)
{
	int n,q;
	cin >> n >> q;
	long long e[n],s[n],d[n][n],u[n],v[n];
	double mat[n][n];
	for (int i=0; i<n; i++)
		cin >> e[i] >> s[i];
	for (int i=0; i<n; i++)
		for (int j=0; j<n; j++)
			cin >> d[i][j];

	for (int k=0; k < n; k++)
		for (int i=0; i < n; i++)
			if (d[i][k] > 0)
				for (int j=0; j < n; j++)
					if (d[k][j] > 0)
						if (d[i][j] == -1 || (d[i][j] > d[i][k]+d[k][j]))
							d[i][j]=d[i][k]+d[k][j];

	for (int i=0; i < n; i++)
		if (d[i][i]>0) d[i][i]=0;

/*
	for (int i=0; i<n; i++)
	{
		for (int j=0; j<n; j++)
			cout << d[i][j] << " ";
		cout << endl;
	}
*/

	for (int i=0; i<q; i++)
		cin >> u[i] >> v[i];

	for (int i=0; i<n; i++)
		for (int j=0; j<n; j++)
			mat[i][j]=INF;

	for (int i=0; i<n; i++)
	{
		for (int j=0; j<n; j++)
		{
			double t=(double)d[i][j]/s[i];
			if (d[i][j]!=-1 && e[i]>=d[i][j] && mat[i][j]>t)
				mat[i][j]=t;
		}
	}

/*
	for (int i=0; i<n; i++)
	{
		for (int j=0; j<n; j++)
			cout << mat[i][j] << " ";
		cout << endl;
	}
*/

	for (int k=0; k < n; k++)
		for (int i=0; i < n; i++)
			if (mat[i][k] > 0)
				for (int j=0; j < n; j++)
					if (mat[k][j] > 0)
						if (mat[i][j] == 0 || (mat[i][j] > mat[i][k]+mat[k][j]))
							mat[i][j]=mat[i][k]+mat[k][j];

	for (int i=0; i < n; i++) mat[i][i]=0;

	for (int i=0; i<n; i++)
		for (int j=0; j<n; j++)
			if (mat[i][j]==INF) mat[i][j]=-1;
/*
	for (int i=0; i<n; i++)
	{
		for (int j=0; j<n; j++)
			cout << mat[i][j] << " ";
		cout << endl;
	}
*/
//	cout << endl << u[0] << " " << v[0] << endl;

	cout << "Case #" << t << ": ";
	cout << setprecision(7);
	for (int i=0; i<q; i++)
		cout << mat[u[i]-1][v[i]-1] << " ";
	cout << endl;

}

int main()
{
	int t;
	cin >> t;

	for (int i=1; i<=t; i++)
		solve(i);

//	solve(1);
}
