#include<bits/stdc++.h>
using namespace std;
pair<long long int,long long int>p1,p2;
int main()
{
	freopen("C-small-2-attempt0.in","r",stdin);
    freopen("g.txt","w",stdout);
	int t,f=0;
	cin>>t;

	while(t--)
	{
	   f++;
	   long long int n,m,k,s,t1,t2;
	   cin>>n>>m;
	   int p=log2(m);
	   if(n&1)
	   p1.first=(n-1)/2,p2.first=(n-1)/2;
	   else
	   {
	   	p1.first=n/2-1,p2.first=p1.first+1;
	   }
	   p1.second=1,p2.second=1;
	   for(int i=1;i<p;i++)
	   {
	   	int flag1=0,flag2=0;
	   	if(p1.first&1)
	   	{
	   		s=(p1.first-1)/2;
	   		p1.first=s;
			p1.second=p1.second*2;  
	   	}
		else
		{
			s=p1.first/2-1;
			p1.first=s;
	        t1=p1.second;
	        flag1=1;
			
		}
		if(p2.first&1)
		{
			p2.first=p2.first/2;
			p2.second=p2.second*2;
		}
		else
		{
			p2.first=p2.first/2;
			t2=p2.second;
			flag2=1;
		}
		if(flag1==1)
		p2.second+=t1;
		if(flag2==1)
		p1.second+=t2;
	   }
	   //cout<<p1.first<<" "<<p1.second<<" "<<p2.first<<" "<<p2.second<<endl;
	   long long int o=1;
	   for(int i=0;i<p;i++)
	   o=o*2;
	   long long int pos=m-o+1;
	   long long int lf;
	   lf=(p2.second>=pos)?p2.first:p1.first;
	   if(m==1)
	   lf=n;
	   if(lf&1)
	   cout<<"Case #"<<f<<": "<<lf/2<<" "<<lf/2<<endl;
	   else
	   cout<<"Case #"<<f<<": "<<lf/2<<" "<<lf/2-1<<endl;
	     
	   	
	}
	  	
	
		
}

