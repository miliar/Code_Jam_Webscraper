#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t,l=1;
	cin>>t;
	while(t--)
	{
		int i,j,n,k;
		double u,arr[200];
		cin>>n>>k;
		cin>>u;
		for(i=0;i<n;i++)
		cin>>arr[i];
		arr[n]=1.0000;
		sort(arr,arr+n);
		double last=arr[0],ans=1;
		for(i=1;i<=n;i++)
		{
			double req=(arr[i]-last)*i;
			if((u-req)>=0.000001)
			{
				u-=req;
				last=arr[i];
				for(int j=0;j<i;j++)
				arr[j]=arr[i];
			}
			else
			{
				double inc=u/i;
				u=0;
				for(int j=0;j<i;j++)
				arr[j]+=inc;
				break;
			}
		}
		for(i=0;i<n;i++){
		ans=ans*arr[i];}
		printf("Case #%d: %lf\n",l,ans);
		l++;
	}
	return 0;
}
