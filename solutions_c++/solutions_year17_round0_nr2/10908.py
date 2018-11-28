#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main() {
	// your code goes here
	freopen("B-small-attempt1.in","r",stdin);
    freopen("out_put.out","w",stdout);
	ll t,n,i,j,x,y,r,m;
	cin>>t;
	j=1;
	while(t--)
	{
	    cin>>n;
	    x=n;
	    m=x%10;
	    x=x/10;
	    y=m;
	    i=1;
	    while(x!=0)
	    {
	       r=x%10;
	       if(r>m)
	       {
	           y=(r-1)*(pow(10,i))+pow(10,i)-1;
	           m=r-1;
	       }
	       else
	       {
	           y=r*pow(10,i)+y;
	           m=r;
	       }
	       i++;
	       x/=10;
	    }
	    cout<<"Case #"<<j<<": "<<y<<endl;
	    j++;
	}
	return 0;
}

