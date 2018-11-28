#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
void ioinit()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
}
int n,p;
int main()
{
	ioinit();
	int T;
	cin>>T;
	int kase=1;
	while(cin>>n>>p)
	{
		vector<int> a;
		int ans=0;
		for(int i=0;i<n;i++)
		{
			int t;
			scanf("%d",&t);
			if(t%p==0) ans++;
			else a.push_back(t);
		}
		if(p==2)
		{
			ans+=(a.size()+1)/2;
		}
		else if(p==3)
		{
			int l=0,r=0;
			for(auto v:a)
			{
				if(v%3==1) l++;
				else r++;
			}
			ans+=min(l,r);
			int k=max(l-min(l,r),r-min(l,r));
			ans+=k/3;
			k-=k/3*3;
			if(k) ++ans;
		}
		else if(p==4)
		{
			int a1=0,a2=0,a3=0;
			for(auto v:a)
			{
				if(v%4==1) a1++;
				else if(v%4==2) a2++;
				else a3++;
			}
			int k=min(a1,a3);
			ans+=k;
			a1-=k;a3-=k;
			ans+=a2/2;
			a2-=a2/2*2;
			if(a1==0) a1=a3;
			if(a2==1&&a1>=2)
			{
				ans+=1;
				a1-=2;
				a2-=1;
			}
			ans+=a1/4;
			a1-=a1/4*4;
			if(a1||a2) ++ans;
		}
		printf("Case #%d: %d\n",kase++,ans);
	}
	return 0;
}
