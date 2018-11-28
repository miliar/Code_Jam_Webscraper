#include <bits/stdc++.h>

using namespace std;

int s[6];
char color[6] = {'R','O','Y','G','B','V'};
int N;

int main()
{
	freopen("Bs.in","r",stdin);
	freopen("Bs.out","w",stdout);
	int T;
	scanf("%d",&T);
	for (int _=1;_<=T;_++)
	{
		scanf("%d",&N);
		int M = 0;
		for (int i=0;i<6;i++)
		{
			scanf("%d",&s[i]);
			M = max(M,s[i]);
		}
		if (M > N/2)
		{
			printf("Case #%d: IMPOSSIBLE\n",_);
			continue;
		}
		string ans = "";
		int col;
		for (int i=0;i<6;i++)
		if (s[i] == M) col = i;
		int A,B;
		for (int i=0;i<6;i+=2)
		if (i!=col) A = i;
		B = 6-A-col;
		//printf("%d %d %d\n",col,A,B);
		//for (int i=0;i<6;i++)printf("%d %c\n",i,color[i]);
		int d = s[A] + s[B] - s[col];
		for (int i=0;i<s[col];i++)
		{
			ans += color[col];
			if (d)
			{
				d--;
				ans += color[A];
				ans += color[B];
				s[A]--;
				s[B]--;
			}
			else if (s[A]>s[B])
			{
				ans += color[A];
				s[A]--;
			}
			else
			{
				ans += color[B];
				s[B]--;
			}
		}
		printf("Case #%d: ",_);
		cout<<ans<<endl;
	}
}
