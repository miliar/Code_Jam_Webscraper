#include <bits/stdc++.h>
#define ll long long int
#define f first
#define s second
#define pl pair< pair<ll, ll>, pair<ll, ll> >

using namespace std;

int main() {
	int t,i; 
	cin>>t;
	ll n, k, ans,c,r;
	pl p;
	for(i=1; i<=t; i++)
	{
		cin>>n>>k;
		c=0;
		c = ((ll)ceil(log2(k+1)));
		c--;
		if(c==0)
		{
		   cout<<"Case #"<<i<<": "<<n/2<<" "<<(n-1)/2<<"\n";	
		}
		else
		{
			p.f.f = n/2;
			p.f.s = (n-1)/2;
			p.s.s =p.s.f= 1;
			r=c;
			while(r>1)
			{  
				
        	    pl q;
        	        if(p.f.f == p.f.s)
		       {
			   q.f.f = p.f.f/2;
			   q.f.s = (p.f.f-1)/2;
		     	}
		           else if(p.f.f%2 == 0)
		         {
			   q.f.f = p.f.f/2;
			   q.f.s = (p.f.f-1)/2;
			  
		       }
		     else 
		     {
			   q.f.f = p.f.s/2;
			   q.f.s = (p.f.s-1)/2;
			  
		     }    
		     
		     if(p.f.f == p.f.s)
		     {
		     	q.s.f = (p.s.f+p.s.s);
		     	q.s.s=q.s.f;
		     }
		     else if(p.f.f%2 == 0)
		     {
		     	 q.s.f = p.s.f;
			     q.s.s = p.s.f + 2*p.s.s;
		     }
		     else
		     {
		      q.s.s = p.s.s;
			  q.s.f = 2*p.s.f + p.s.s;
		     }
		     p=q;
		     r--;
	
			}
			
			if((k-(2<<(c-1)))<p.s.f)
			{
				ans = p.f.f;
				cout<<"Case #"<<i<<": "<<ans/2<<" "<<(ans-1)/2<<"\n";
			}
			else 
		    {
		    	ans = p.f.s;
		    	cout<<"Case #"<<i<<": "<<ans/2<<" "<<(ans-1)/2<<"\n";
		    }
	
		}
	}
	return 0;
}