#include <bits/stdc++.h>
using namespace std;

#define fo(i,s,t) for(int i = s; i <= t; ++ i)
#define fd(i,s,t) for(int i = s; i >= t; -- i)
const int maxn = 20;

int a[maxn], n, t;
char str[maxn];
bool ok;

int main()
{
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	scanf("%d",&t);
	fo(qwq,1,t)
	{
		scanf("%s",str+1);
		n = strlen(str+1);
		fo(i,1,n) a[i] = str[i]-'0';
		fo(i,1,n)
		{
			ok = true;
			fo(j,1,n-1) if(a[j]>a[j+1]) {ok = false; break;}
			if(ok) break;
			fo(j,1,n-1) if(a[j]>a[j+1]) 
			{
				-- a[j];
				fo(k,j+1,n) a[k] = 9;
				break;
			}
		}
		int l = 1;
		while(a[l]==0&&l<=n-1)++l;
		printf("Case #%d: ",qwq);
		fo(i,l,n) printf("%d",a[i]);
		puts("");
	}
	return 0;
}