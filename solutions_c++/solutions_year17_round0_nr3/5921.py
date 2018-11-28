#include <bits/stdc++.h>
using namespace std;

int main() {
    int t,q;
    long long int n,k,l,maxd,i,dist,ls,rs,pos;
	cin>>t;
    for(q=1;q<=t;q++)
	{
	    cin>>n>>k;
	    if(n==k)
	    {
	        ls=0;
	        rs=0;
	    }
	    else
	    {
	    bool a[n+2];
	    memset(a,0,sizeof(a));
	    a[0]=a[n+1]=1;
	    while(k--)
	    {
	        l=0;
	        maxd=1;
	        for(i=1;i<=n+1;i++)
	        {
	            if(a[i]==1)
	            {
	                dist=i-l;
	                if(dist>maxd)
	                {
	                    maxd=dist;
	                    pos=l+maxd/2;
	                    ls=pos-l-1;
	                    rs=i-pos-1;
	                }
	                l=i;
	            }
	        }
	        a[pos]=1;
	    }
	    }
        cout<<"Case #"<<q<<": "<<max(ls,rs)<<' '<<min(ls,rs)<<endl;
	}
	return 0;
}
