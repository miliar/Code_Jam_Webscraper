#include<bits/stdc++.h>
using namespace std;
typedef long long LL;
int len,a[50];
LL f[10][50];
LL dfs(int l,int last,bool flag)
{
	if (!flag&&f[last][len-l+1]!=-1) return f[last][len-l+1];
	if (l>len) return 1;
	int lim=9;
	if (flag) lim=a[l];
	LL ret=0;
	for (int o=last;o<=lim;o++) ret+=dfs(l+1,o,flag&&o==lim);
	if (!flag) f[last][len-l+1]=ret;
	return ret;
}
LL calc(LL n)
{
	if (!n) return 0;//
	int b[50];
	len=0;
	while (n)
	{
		b[len++]=n%10;
		n/=10;
	}
	len--;
	for (int i=0;i<=len;i++) a[i]=b[len-i];
	return dfs(0,0,1);
}
int main()
{
	//freopen("B.in","r",stdin);
	//freopen("B.out","w",stdout);
	memset(f,-1,sizeof(f));
	int T;
	cin>>T;
	for (int ca=1;ca<=T;ca++)
	{
		LL n;
		scanf("%I64d",&n);
		LL tot=calc(n);
		LL l=0,r=n,mid,ans;
		while (l<=r)
		{
			mid=(l+r)/2;
			if (calc(mid)<tot)
			{
				ans=mid;
				l=mid+1;
			}
			else r=mid-1;
		}
		ans++;
		printf("Case #%d: %I64d\n",ca,ans);
	}
	return 0;
	//fclose(stdin);fclose(stdout);
}
