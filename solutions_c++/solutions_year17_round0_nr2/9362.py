#include<iostream>
#include<algorithm>
using namespace std;
long long int func(long long int a)
{
	long long int i,j,k;k=a%10;
	for(i=a/10;i>0;i/=10)
	{
		j=i%10;
		if(j>k)
		  return 0;
		k=j;  
	}
	return 1;
}
int main()
{
	long long int i,j,k,n,p=0,t;
	cin>>t;
	while(t--)
	{
		cin>>n;p++;
		while(!func(n))
		n--;
		cout<<"Case #"<<p<<": "<<n<<endl;
	}
}
