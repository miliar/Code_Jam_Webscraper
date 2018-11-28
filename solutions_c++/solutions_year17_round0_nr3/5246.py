#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define ll long long int

using namespace std;

int solve(ll x,ll a)
{
	if(a==1)
	return x;
	
	double p= log10(x)/log10(a);
	
	double s=0.50;
	int r=p+1;
	double d=r;
	
	double q=p+s;
	
	//cout<<"p="<<p<<"\n";
	
	//cout<<"s="<<s<<" d="<<d<<"\n";
	
	if(q>=d)
	return r;
	else
	return (int)p;
}


int main()
{
	 ll t,n,i,k,len,j,pos,maxm,it,c,p,q,x,prev,x1,r;
	
	cin>>t;
	
	string str;
	bool flag;
	
	x1=1;
	
	priority_queue<ll> pq;
	
	
	
	while(t--)
	{
		cin>>n>>k;
		
		cout<<"Case #"<<x1<<": ";
		
		while(!pq.empty())
		pq.pop();
		
		x=ceil(n/2.0);
		p=n;
		
		c=0;
		
		while(1)
		{
			c++;
			
			pq.push(x-1);
			pq.push(p-x);
			
			
			if(c==k || p==1)
			break;
			else
			{
			
			p=pq.top();
			pq.pop();
			
			x=ceil(p/2.0);
		}
			
			
		}
		
		r=x-1;
	  
	  
	  q=p-x;
	  
		
	/*	x=solve(n,k);
		
		
		j=ceil(x/2.0);
		
		p=j-1;
		q=x-j;*/
		
		
		
		cout<<max(r,q)<<" "<<min(r,q);
	
	cout<<"\n";
	
	x1++;
}

return 0;
}