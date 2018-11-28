#include<bits/stdc++.h>
#include<iostream>
#define ll long long int
#define pb push_back
#define mp make_pair
#define start() int t;cin>>t;while(t--)
#define mod 1000000007
using namespace std;
int main()
{
	  //freopen("C-large.in","r",stdin);
	  //freopen("shhh.txt","w",stdout);
	 ll e1=0,e2=0;
	 ll count1=0,num1=0,t1=0,tc1=0;
     ll count2=0,num2=0,t2=0,tc2=0;
	
	int f=0;
   /* int t;
    cin>>t;
    while(t--)*/
    start()
	{
		
		ll n,k;
		cin>>n>>k;
			ll p=1,q=0,s=0,r=0,sum=0;
		ll c1=0,c2=0;
		map<ll,ll>m;
		for(int k=0;k<64;k++)
		{
		  m[k]++;
		  	
		}
		while((p-1)<k)
		{
			q=p;
			p*=2;
			if(p/2!=q)
			break;
			c1++;
		}
		c1--;
		r=k-q+1;
	//	cout<<c1<<" "<<r<<" "<<q;
		
		sum=n;
		if(k!=1)
		{	
			if(n%2==0)
			{
				num1=n/2-1;
				count1=1;
				num2=n/2;
				count2=1;
			}
			else
			{
				num1=n/2;
				count1=1;
				num2=n/2;
				count2=1;
			}
			 for(int j=1;j<c1;j++)
			{
				if(num1%2==0)
				{
					t1=num1/2-1;
					num1=t1;
					tc1=count1;
					e1=1;
				}
				else
				{
					t1=num1/2;
					num1=t1;
					count1=2*count1;
				}	
				if(num2%2==0)
				{
					t2=num2/2-1;
					num2=t2+1;
					e2=1;
					tc2=count2;
				}
				else
				{
					t2=num2/2;
					num2=t2;
					count2=2*count2;
				}
				
				if(e1)
				{
					count2+=tc1;
				}
				if(e2)
				{
					count1+=tc2;
				}
				e1=0;
				e2=0;	
			}
			
			if(r>count2)
			sum=num1;
			else
			sum=num2;
		}
		
		ll d=sum;
		if(d%2==0){
			f++;
		 cout<<"Case #"<<f<<": "<<d/2<<" "<<d/2-1<<"\n";
	}
		 else{
		 	f++;
		 cout<<"Case #"<<f<<": "<<d/2<<" "<<d/2<<"\n";}
		
	}
}
