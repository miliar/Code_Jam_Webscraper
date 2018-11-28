#include<bits/stdc++.h>
using namespace std;

int main()
{
	freopen("Input.txt","r",stdin);
	freopen("Output.out","w",stdout);
	int t,z=1;
	cin>>t;
	while(t--)
	{
		long long int n,k;
		cin>>n>>k;
		long long int arr[100005]={0};
		arr[0]=1;
		arr[n+1]=1;
		int pos,mleft=INT_MIN,mright=INT_MIN;
		while(k--)
		{
		mleft=INT_MIN;mright=INT_MIN;
		for(int i=1;i<=n;i++)
		{
			if(arr[i]==1)
				continue;
			int left=0,right=0;
			for(int j=i-1;j>=0;j--)
			{
				if(arr[j])
					break;
				left++;
			}
			for(int j=i+1;j<=n;j++)
			{
				if(arr[j])
					break;
				right++;
			}
			if(min(left,right)>min(mleft,mright))
			{
				mleft=left;
				mright=right;
				pos=i;
			}
			else if(min(left,right)==min(mleft,mright))
			{
				if(max(left,right)>max(mleft,mright))
				{
					mleft=left;
					mright=right;
					pos=i;	
				}
				else if(left>mleft)
				{
					mleft=left;
					mright=right;
					pos=i;

				}
			}
		}
		arr[pos]=1;
		}
		printf("Case #%d: ",z++);
		cout<<max(mleft,mright)<<" "<<min(mright,mleft)<<endl;
	}
	return 0;
}