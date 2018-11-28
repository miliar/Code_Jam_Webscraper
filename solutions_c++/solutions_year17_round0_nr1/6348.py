#include<bits/stdc++.h>

using namespace std;

int main() {
	freopen("in.txt","r",stdin);
	freopen("out.txt","wb",stdout);
	int t,n,k;
	int test = 1;
	scanf("%d",&t);
	char a[100002];
	bool b[100002];
	while(t--)
	{
		bool flag = false;
		scanf("%s",a);
		getchar();
		scanf("%d",&k);

		n = strlen(a);

		memset(b,0,sizeof b);
		int s = 0;
		int ans = 0;
		for(int i = 0;i < n;i++)
		{
			if(b[i])
				s = 1 - s;
			if((s == 0 && a[i]=='-') || (s == 1 && a[i]=='+'))
			{
				b[min(n,i+k)]=1;
				++ans;
				s = 1 - s;
				if(n-i < k)
				{
					flag = true;
					break;
				}
			}
		}

		if(flag == false)
		{
			printf("Case #");
			printf("%d",test);
			printf(": ");

			printf("%d\n",ans);
		}
		else
		{
			printf("Case #");
			printf("%d",test);
			printf(": ");

			printf("IMPOSSIBLE\n");
		}

		test++;
	}
	return 0;
}
