#include<bits/stdc++.h>

using namespace std;

int n, m;
char mmap[25][26];
vector<pair<int,int>> v[26];
int mini[26], maxi[26], minj[26], maxj[26];

int main()
{
	int tcc;
	scanf("%d", &tcc);
	for(int tc = 1; tc <= tcc; tc++)
	{
		for(int i = 0; i < 26; i++)
			v[i].clear();

		scanf("%d %d", &n, &m);
		for(int i = 0; i < n; i++)
			scanf("%s", mmap[i]);

		for(int i = 0; i < n; i++)
			for(int j = 0; j < m; j++)
				if(mmap[i][j] != '?')
					v[mmap[i][j]-'A'].push_back({i, j});

		for(int k = 0; k < 26; k++)
		{
			mini[k] = minj[k] = 1e9+7;
			maxi[k] = maxj[k] = -1;

			for(auto it: v[k])
			{
				mini[k] = min(mini[k], it.first);
				minj[k] = min(minj[k], it.second);
				maxi[k] = max(maxi[k], it.first);
				maxj[k] = max(maxj[k], it.second);
			}
			if(!v[k].empty())
			{
				for(int i = mini[k]; i <= maxi[k]; i++)
					for(int j = minj[k]; j <= maxj[k]; j++)
						mmap[i][j] = 'A'+k;
			}
		}
		// up
		for(int k = 0; k < 26; k++)
		{
			if(v[k].empty())	continue;
			while(mini[k] > 0)
			{
				bool flag = true;
				for(int j = minj[k]; j <= maxj[k]; j++)
					if(mmap[mini[k]-1][j] != '?')
					{
						flag = false;
						break;
					}
				if(!flag)	break;
				mini[k]--;
				for(int j = minj[k]; j <= maxj[k]; j++)
					mmap[mini[k]][j] = 'A'+k;
			}
		}
		// down
		for(int k = 0; k < 26; k++)
		{
			if(v[k].empty())	continue;
			while(maxi[k]+1 < n)
			{
				bool flag = true;
				for(int j = minj[k]; j <= maxj[k]; j++)
					if(mmap[maxi[k]+1][j] != '?')
					{
						flag = false;
						break;
					}
				if(!flag)	break;
				maxi[k]++;
				for(int j = minj[k]; j <= maxj[k]; j++)
					mmap[maxi[k]][j] = 'A'+k;
			}
		}
		// left
		for(int k = 0; k < 26; k++)
		{
			if(v[k].empty())	continue;
			while(minj[k] > 0)
			{
				bool flag = true;
				for(int i = mini[k]; i <= maxi[k]; i++)
					if(mmap[i][minj[k]-1] != '?')
					{
						flag = false;
						break;
					}
				if(!flag)	break;
				minj[k]--;
				for(int i = mini[k]; i <= maxi[k]; i++)
					mmap[i][minj[k]] = 'A'+k;
			}
		}
		// right
		for(int k = 0; k < 26; k++)
		{
			if(v[k].empty())	continue;
			while(maxj[k]+1 < m)
			{
				bool flag = true;
				for(int i = mini[k]; i <= maxi[k]; i++)
					if(mmap[i][maxj[k]+1] != '?')
					{
						flag = false;
						break;
					}
				if(!flag)	break;
				maxj[k]++;
				for(int i = mini[k]; i <= maxi[k]; i++)
					mmap[i][maxj[k]] = 'A'+k;
			}
		}

		printf("Case #%d:\n", tc);
		for(int i = 0; i < n; i++)
		{
			for(int j = 0; j < m; j++)
				printf("%c", mmap[i][j]);
			printf("\n");
		}
	}
    return 0;
}
