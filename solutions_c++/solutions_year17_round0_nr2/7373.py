#include<bits/stdc++.h>
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
	long long int i,j,k,n,p=0,t,l,r;
	cin>>t;
	while(t--)
	{
		cin>>n;p++;k=0;l=1;r=0;
		while(!func(n))
		{
		   	k++;n=n-l;
		   	if(k==10)
		   	{
		   		k=0;l=l*10;r++;
				n=n-n%((long long int)pow(10,r))+pow(10,r)-1;
			   }
		}
		cout<<"Case #"<<p<<": "<<n<<endl;
	}
}
