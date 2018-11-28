#include<bits/stdc++.h>
using namespace std;

typedef long long lld;

int main()
{
	freopen("in3.txt","r",stdin);
    freopen("out3.txt","w",stdout);
	
	lld t;
	cin>>t;
	
    for(lld tc=1;tc<=t;tc++)
   {
	   lld n,k;
	   cin>>n>>k;
	   lld mn=0,mx=0;
	   
	   while(1)
	   {
			if(k==n)
			{
				mn=mx=0;
				break;
			}
			if(k==1)
			{
				if(n%2==0)
				{
					mx=n/2;
					mn=(n/2)-1;
				}
				else
				{
					mn=mx=n/2;
				}
				break;		
			}
			
		k--;
		if(n%2)
		{
			if(k%2)
            {
                n = n/2;
            	k = k/2 + 1;
            }
            else
            {
                n = n/2;
                k = k/2;
            }
		}
		else
		{
			if(k%2)
            {
                k = k/2 + 1;
                n = n/2;
            }
            else
            {
                k = k/2;
                n = n/2 - 1;
            }
		}
	}
		cout<<"Case #"<<tc<<": "<<mx<<" "<<mn<<"\n";
	}
	
}
