#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{

	 freopen("/home/krishna/Downloads/B-small-attempt0.in","r",stdin);
    freopen("/home/krishna/Desktop/c++/qual2.out","w",stdout);
	 long long int n,t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		cin>>n;
		 long long int f=0,m,k=9,q;m=n;
		while(f==0)
		{
			unsigned long long int h=0,o;
			k=9;
			m=n;
			q=m;
			while(m!=0)
			{
				o=m%10;
				if(o<=k)
				{k=o;
				m=m/10;}
				else{
				h=1;
				m=0;}
				
			}
			if(h==1)
			n--;
			if(n==0||h==0)
			f=1;
		
		}
	cout<<"Case #"<<i<<": "<<q<<endl; 
		
	}
return 0;

}
