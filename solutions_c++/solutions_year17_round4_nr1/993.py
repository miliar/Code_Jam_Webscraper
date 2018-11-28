#include<stdio.h>
#include<algorithm>
using namespace std;
int n, p, arr[110], cnt[5];
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int tt, T, i;
	scanf("%d", &T);
	for(tt=1; tt<=T; ++tt)
	{
		int ans=0;
		cnt[0]=cnt[1]=cnt[2]=cnt[3]=cnt[4]=0;
		scanf("%d", &n);
		scanf("%d", &p);
		for(i=1; i<=n; ++i)
		{
			scanf("%d", &arr[i]);
			arr[i]%=p;
			if(arr[i] == 0)
			{
				++ans;
				--i;
				--n;
				continue;
			}
			++cnt[arr[i]];
		}
		printf("Case #%d: ", tt);
		if(p==2)
		{
			ans+=(cnt[1]+1)/2;
		}
		else if(p==3)
		{
			if(cnt[1]>cnt[2])
			{
				ans += cnt[2];
				cnt[1] -= cnt[2];
				ans += (cnt[1]+2)/3;
			}
			else
			{
				ans += cnt[1];
				cnt[2] -= cnt[1];
				ans += (cnt[2]+2)/3;
			}
		}
		else
		{
			int x;
			if(cnt[1]>cnt[3])
			{
				ans += cnt[3];
				x = cnt[1]-cnt[3];
			}
			else
			{
				ans += cnt[1];
				x = cnt[3]-cnt[1];
			}
			ans += cnt[2]/2;
			int y = cnt[2]%2;
			if(y==1)
			{
				++ans;
				x -= 2;
			}
			if(x>0)
			{
				ans += (x+3)/4;
			}
		}
		printf("%d\n", ans);
	}
}
