#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
int main(void)
{
	int a;
	FILE* fp = fopen("Output.txt", "w+");
	scanf("%d", &a);
	for(int x=0;x<a;x++)
	{
		int n, p, r[100], sel[100][100] = {0}, cnt = 0, temp;
		vector<int> q[100];
		double nx[100][100][2];
		scanf("%d%d", &n, &p);
		for(int i=0;i<n;i++)
			scanf("%d", &r[i]);
		for(int i=0;i<n;i++)
			for(int j=0;j<p;j++)
			{
				scanf("%d", &temp);
				q[i].push_back(temp);
			}
		for(int i=0;i<n;i++)
			sort(q[i].begin(), q[i].end());
		for(int i=0;i<n;i++)
			for(int j=0;j<p;j++)
			{
				nx[i][j][0] = ceil(q[i][j]*10.0/11/r[i]);
				nx[i][j][1] = floor(q[i][j]*10.0/9/r[i]);
			}
		for(int i=0;i<p;i++)
		{
			int seltemp[100] = {0}, bnd[2] = {0};
			bool tr = 1;
			if(nx[0][i][0]>nx[0][i][1]) continue;
			else 
			{
				seltemp[0] = i+1;
				bnd[0] = (int) nx[0][i][0];
				bnd[1] = (int) nx[0][i][1];
			}
			for(int j=1;j<n;j++)
			{
				for(int k=0;k<p;k++)
				{
					if(sel[j][k]) continue;
					if(max(bnd[0], (int)nx[j][k][0])>min(bnd[1], (int)nx[j][k][1])) continue;
					else
					{
						seltemp[j] = k+1;
						bnd[0] = max(bnd[0], (int)nx[j][k][0]);
						bnd[1] = min(bnd[1], (int)nx[j][k][1]);
						break;
					}
				}
				if(!seltemp[j])
				{
					tr = 0;
					break;
				}
			}
			if(tr)
			{
				for(int j=0;j<n;j++)
					sel[j][seltemp[j]-1] = 1;
				cnt++;
			}
		}
		printf("Case #%d: %d\n", x+1, cnt);
		fprintf(fp, "Case #%d: %d\n", x+1, cnt);
	}
	return 0;
}
