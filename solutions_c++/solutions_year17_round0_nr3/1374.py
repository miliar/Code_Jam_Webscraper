#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
typedef unsigned long long int ull;
#define inf 100000000000000000
set<ll>st;
map<ll,ll>my;
set<ll>::reverse_iterator rit;

int main()
{
   freopen("0in.txt","r",stdin);
   freopen("0out.txt","w",stdout);
	int tcase,t,i,j;
	ll n,k,w,tmp,a,b,x;
	
	scanf("%d",&tcase);
	for(t=1;t<=tcase;t++)
	{
		st.clear();
		my.clear();
		
		cin>>n>>k;
		st.insert(n);
		my[n]++;
		while(k>0)
		{
		   rit = st.rbegin();
		   w = *rit;
		   st.erase(*rit);
		   if(k>my[w])
		   {
		   	x = min(k,my[w]);
		   	  k-=my[w];
		   	  my[w] = 0;
		   	  if(w%2==0)
		   	  {
		   	    tmp = w/2;
				a = tmp;
				b = tmp-1;  
				if(a>0){
				
				st.insert(a);
				my[a]+=x;
			    
				}
				if(b>0)
				{
					st.insert(b);
				    my[b]+=x;
				}
			  }
			  else
			  {
			  	tmp = w/2;
			  	a = b = tmp;
			  	if(a>0){
				
				st.insert(a);
				my[a]+=x;
			    
				}
				if(b>0)
				{
					st.insert(b);
				    my[b]+=x;
				}
			  }
		   }
		   else
		   {
		   	   k-=my[w];
		   	   tmp= w;
		   	   if(tmp%2==0)
		   	   {
		   	      a = tmp/2;
				  b = max(0LL,a-1);	 	
			   }
			   else
			   {
			   	 a = b = tmp/2;
			   }
		   }
		   
		}
		printf("Case #%d: %lld %lld\n",t,a,b);
	}
}

