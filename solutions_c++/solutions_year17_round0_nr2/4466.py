#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("j2.txt","w",stdout);
	int t,t1;
	cin>>t;
	t1=t;
	while(t--)
	{
		
		long long int n,n1=0;
		int i,l,k=19,j,z,mm=0;
		cin>>n;
		int a[20]={0};
		
		cout<<"Case #"<<t1-t<<": ";
		while(n>0)
		{
			a[k]=n%10;
			n=n/10;
			k--;
		}
		for(i=19;i>0;i--)
		{
			if(a[i]>=a[i-1])
			continue;
			else
			{
				a[i-1]--;
				for(j=i;j<=19;j++)
				a[j]=9;
			}
		}
		i=0;
		while(a[i]==0)
		i++;
		for(;i<=19;i++)
		cout<<a[i];
		cout<<endl;
	}
	
}
