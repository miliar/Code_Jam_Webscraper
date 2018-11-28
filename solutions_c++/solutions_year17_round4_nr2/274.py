#include <bits/stdc++.h>
using namespace std;

typedef pair<int,int> ii;

int mat[1000][1000];
int hcnt[1000];

int main()
{
	int t;
	cin >> t;

	for(int cn=1; cn<=t; cn++)
	{
		int n,c,m;
		cin >> n >> c >> m;


		for(int i=0; i<n; i++)
			for(int j=0; j<c; j++)
				mat[i][j] = 0;
		for(int i=0; i<m; i++)
		{
			int a,b;
			cin >> a >> b;
			mat[a-1][b-1]++;
		}

		int cmax = 0;
		for(int i=0; i<c; i++)
		{
			int curr = 0;
			for(int j=0; j<n; j++)
				curr += mat[j][i];
			cmax = max(cmax,curr);
		}
		for(int i=0; i<n; i++)
		{
			int curr = 0;
			for(int j=0; j<c; j++)
				curr += mat[i][j];
			hcnt[i] = curr;
		}

		int low = cmax;
		int high = 1000;

		while(low!=high)
		{
			int mid = (low+high)/2;

			//check if it works at this level
			int excess = 0;
			for(int i=0; i<n; i++)
			{
				excess += mid-hcnt[i];
				if(excess<0)
					break;
			}

			if(excess<0)
				low = mid+1;
			else
				high = mid;
		}

		int total = 0;
		for(int i=0; i<n; i++)
			total += max(hcnt[i]-low,0);

		cout << "Case #" << cn << ": " << low << " " << total << endl;
	}
}