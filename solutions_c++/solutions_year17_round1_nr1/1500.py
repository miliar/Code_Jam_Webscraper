#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <cstring>
#include <fstream>
#define ll long long int
using namespace std;
const double _pi = acos(-1.0);
char ar[30][30];
int main()
{
    //freopen("in.txt", "r", stdin);
	//freopen("out.txt", "w", stdout);
	int t;
	scanf("%d\n", &t);
	int c = 1;
	while(t--)
	{
		int n, m;
		scanf("%d %d\n", &n, &m);
		vector<int> ar2(n, 0);
		for(int i = 0; i < n; i++)
		{
			for(int j = 0; j < m; j++)
			{
				scanf("%c", &ar[i][j]);
				if(ar[i][j] != '?') ar2[i] = 1;
			}
			scanf("\n");
		}
		for(int i = 0; i < n; i++)
		{
			for(int j = 0; j < m; j++)
			{
				if(ar[i][j] != '?')
				{
					int k = j-1, k2 = j+1, k3 = i-1, k4 = i+1;
					while(k >= 0 && ar[i][k] == '?')
					{
						ar[i][k] = ar[i][j];
						k--;
					}
					while(k2 < m && ar[i][k2] == '?')
					{
						ar[i][k2] = ar[i][j];
						k2++;
					}
					while(k3 >= 0 && ar2[k3] == 0)
					{
						for(int l = k+1; l < k2; l++) ar[k3][l] = ar[i][j];
						k3--;
					}
					while(k4 < n && ar2[k4] == 0)
					{
						for(int l = k+1; l < k2; l++) ar[k4][l] = ar[i][j];
						k4++;
					}
				}
			}
		}
		printf("Case #%d:\n", c);
		for(int i = 0; i < n; i++)
		{
			for(int j = 0; j < m; j++)
			{
				printf("%c", ar[i][j]);
			}
			printf("\n");
		}
		c++;
	}
    return 0;
}
