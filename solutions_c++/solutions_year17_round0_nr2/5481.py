#include<bits/stdc++.h>
using namespace std;
int a[19]={10},b[19]={10};
int main()
{
	long long int n,f,k,t,p,c=0,hh,q,i,j;
	cin>>t;
	for(f=1;f<=t;f++)
	{
		cin>>n;
		while(n>0)
		{
			p=n;i=0;c=0;
			while(p>0)
			{
				q=p%10;
				a[i]=q;b[i]=q;
				p/=10;i++;
			
			}k=i;
			for(j=0;j<i;j++)
			{
				a[j]=b[k-1];
				k--;
			}
			
			sort(b,b+i);
			for(j=0;j<i;j++)
			{
				//cout<<"a[j]="<<a[j]<<endl;
				if(a[j]!=b[j])
				{
					c=1;
					break;
				}
			}
			for(j=0;j<i-1 && i>1;j++)
			{
				if(a[j]>a[j+1])
				{
			
					hh=pow(10,i-j-1);
				
					n=(n/hh);
					n=n*hh;
					break;
				}
			}
			if(c==0)
			{
				cout<<"Case #"<<f<<": "<<n<<endl;
				//cout<<"Case #"<<i<<": "<<d<<endl;
				
				break;	
			}
			n--;
		}
	}
}
