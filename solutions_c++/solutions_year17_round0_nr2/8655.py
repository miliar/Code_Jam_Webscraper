#include<bits/stdc++.h>
using namespace std;
long long int pos(long long int num,long long int n)
{
//	cout<<"n="<<n<<"\n";
	if(n==0)
	return 0;
	long long int rem=1;
	for(long long int i=1;i<=n;i++)
	{
		rem=rem*10;
	}
	rem=rem/10;
	long long int temp=num/(rem);
	long long int temp2=0;
	long long int k=1;
	for(long long int i=1;i<=n;i++)
	{
		temp2=temp2+temp*(rem/k);
		k=k*10;
	}
//	cout<<temp2<<"\n";
	if(temp2>num)
	{
		return n;
	}
	else
	{
		return pos(num%rem,n-1);
	}
}
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	long long int test;
	cin>>test;
	for(long long int t=1;t<=test;t++)
	{
		long long int num;
		cin>>num;
		long long int temp=num,n=0;
		while(temp>0)
		{
			temp=temp/10;
			n++;
		}
	//	cout<<"--"<<pos(num,n);
		long long int fail=n-pos(num,n)+1;
		long long int rem=1;
		for(long long int i=1;i<=n;i++)
		{
			rem=rem*10;
		}
		rem=rem/10;
		long long int k=rem;
		long long int i;
		long long int number=0;
		for(i=1;i<=n;i++)
		{
			if(i<fail)
			{
//				cout<<(num/k)%10;
				number=number+(num/k)%10*k;
//				cout<<k<<" ";
				k=k/10;
			}
			if(i==fail)
			{
				long long int out=((num/k)%10)-1;
//				cout<<(long long int)out;
				number=number+out*k;
//				cout<<k<<" ";
				k=k/10;	
			}
			if(i>fail)
			{
//				cout<<k<<" ";
//				cout<<"9";
				number=number+9*k;
				k=k/10;
			}
		}
		cout<<"Case #"<<t<<": "<<number<<"\n";
	}
	return 0;
}
