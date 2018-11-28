#include<bits/stdc++.h>
using namespace std;

int check(long long int n)
{
	int xold=n%10;
	while(n>0){
		int xnew=n%10;
		if(xold<xnew)
			return 0;
		n=n/10;
		xold=xnew;
	}
	return 1;
}

int main()
{
	long long int t,t1,n;
	cin>>t1;
	for(int t=t1;t<=t1;t++){
		cin>>n;
		long long int i;
		for(i=n;i>=0;i--){
		if(n>=1 && n<=9)
			{cout<<"Case #t: "<<n<<endl;break;}
		else 
		{
			if(check(i)==1)
			{	cout<<i<<endl;break;}
		}
		}
		
	}
return 0;
}
