#include <bits/stdc++.h>
#define mp make_pair
#define ft first
#define sd second
#define ue printf("what?\n");
#define pb push_back
#define pf push_front
#define oo 0x3F3F3F3F
#define OO 0x3F3F3F3F3F3F3F3F
#define EPS 1e-2
#define inf 1000000000000000LL
#define N 10005
#define pi acos(-1)
#define mod 1000000007

typedef long long ll;

using namespace std;

int main()
{
	int test, vis[300], caso = 1, n, m, i, j, k, t, l, r, u, d;
	string s[1000];
	scanf("%d", &test);
	while(test--)
	{
		memset(vis,0,sizeof vis);
		scanf("%d%d", &n, &m);
		for(i=0; i<n; i++)
			cin >> s[i];
		for(i=0; i<n; i++)
			for(j=0; j<m; j++)
			{
				if(s[i][j] == '?')
					continue;
				if(vis[s[i][j]])
					continue;
				vis[s[i][j]] = 1;
				l = j;
				for(k=j; k>=0; k--)
				{
					if(s[i][k] != '?' && s[i][k] != s[i][j])
						break;
					l = k;
				}
				r = j;
				for(k=j; k<m; k++)
				{
					if(s[i][k] != '?' && s[i][k] != s[i][j])
						break;
					r = k;
				}
				u = i;
				for(k=i; k>=0; k--)
				{
					bool ok = 1;
					for(t=l; t<=r; t++)
						if(s[k][t] != '?' && s[k][t] != s[i][j])
							ok = 0;
					if(!ok)
						break;
					u = k;
				}
				d = i;
				for(k=i; k<n; k++)
				{
					bool ok = 1;
					for(t=l; t<=r; t++)
						if(s[k][t] != '?' && s[k][t] != s[i][j])
							ok = 0;
					if(!ok)
						break;
					d = k;
				}
				for(k=u; k<=d; k++)
					for(t=l; t<=r; t++)
						s[k][t] = s[i][j];
			}
		printf("Case #%d:\n", caso++);
		for(i=0; i<n; i++)
		{
			for(j=0; j<m; j++)
				printf("%c", s[i][j]);
			printf("\n");
		}
	}
}
				
							
					
	
		
		
		
			
	
