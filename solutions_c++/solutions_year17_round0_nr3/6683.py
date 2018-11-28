#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("in3.txt","r",stdin);
	freopen("out3.txt","w",stdout);
	long long int test;
	cin>>test;
	for(long long int t=1;t<=test;t++)
	{
		long long int n,k,i,j,p;
		cin>>n>>k;
		long long int arr[n+2][3];
		arr[0][0]=1;
		arr[n+1][0]=1;
		for(i=1;i<=n;i++)
		arr[i][0]=0;
		for(i=1;i<=k;i++)
		{
//			cout<<"jfbdj\n";
			long long int prev;
			prev=0;
			for(j=1;j<=n;j++)
			{
				arr[j][1]=prev;
				if(arr[j][0]==1)
				{
					prev=0;
				}
				else
				prev++;
			}
			prev=0;
			for(j=n;j>=1;j--)
			{
				arr[j][2]=prev;
				if(arr[j][0]==1)
				{
					prev=0;
				}
				else
				prev++;
			}
			long long int far=LLONG_MIN,idx;
			for(j=1;j<=n;j++)
			{
				if(arr[j][0]==0)
				{
					if(min(arr[j][1],arr[j][2])>far)
					{
						far=min(arr[j][1],arr[j][2]);
						idx=j;
					}
				}
			}
			long long int near=LLONG_MIN,idx2;
			for(j=1;j<=n;j++)
			{
				if((far==min(arr[j][1],arr[j][2]))&&(arr[j][0]==0))
				{
					if(max(arr[j][1],arr[j][2])>near)
					{
						near=max(arr[j][1],arr[j][2]);
						idx2=j;
					}
				}
			}
			arr[idx2][0]=1;
			p=idx2;
		}
		cout<<"Case #"<<t<<": "<<max(arr[p][1],arr[p][2])<<" "<<min(arr[p][1],arr[p][2])<<"\n";
	}
	return 0;
}
