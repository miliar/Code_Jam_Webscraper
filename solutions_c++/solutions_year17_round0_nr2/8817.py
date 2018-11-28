#include<bits/stdc++.h>
using namespace std;
long long int max(long long int a,long long int b)
{
	if(a>b)
		return a;
	else
		return b;
}
int check(long long int n)
{
	long long int n1=n,d=n1%10,flag=0;
	n1=n1/10;
	while(n1>0)
	{
		if(n1%10>d)
			return 0;
		d=n1%10;
		n1/=10;
	}
	return 1;
}
int main()
{
	freopen("Input.txt","r",stdin);
	freopen("Output.out","w",stdout);
	int t,z=1;
	cin>>t;
	//cout<<"212";
	while(t--)
	{
		long long int n,n1,n2,d,k=10,flag=0,mul=1,ans=INT_MIN;
		cin>>n;
		n1=n;
		d=n1%10;
		n1=n1/10;
		while(n1)
		{
			//cout<<": "<<n1<<endl;
			if(n1%10>d)
				flag=1;
			if(n1%10>=d)
			{
			//	cout<<": "<<n1<<endl;
				n2=n1;
				mul=k;
				int p=check(n2*mul-1);
				if(p)
				{	
					ans=max(n2*mul-1,ans);
				}
			}
			k=k*10;
			d=n1%10;
			n1/=10;
		}
		//cout<<flag<<endl;
		//cout<<n2<<endl;
		printf("Case #%d: ",z++);
		if(flag==0)
			cout<<n<<endl;
		else
			cout<<(n2*mul-1)<<endl;
	}
	return 0;
}