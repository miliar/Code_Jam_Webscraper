#include <bits/stdc++.h>
 using namespace std;

#define ll long long int
#define pb push_back 
#define mp make_pair
#define ff first
#define ss second




int main() {
   ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
   ll n,b,i,j,k,z,x=0,y=0,p,l,T,m,ans=0,maxx = -1e18;
    double xx,yy;   
    cin>>T;
    bool g;
    char c;
    for(int t  =  1; t <= T; t++)
    {
    	cin>>n>>m;
    	char a[n][m];
    	for(i=0;i<n;i++)
    	{
    	  for(j=0 ;j < m ;j++)
    	  	cin>>a[i][j];
    	}
       
    	for(i = 0; i < n ;i++)
    	{   p = 0;
    		g = false;
    		for(j = 0; j < m; j++)
    		{
    			if(a[i][j] != '?')
    				{
    					for( k = p; k < j; k++)
    						a[i][k] = a[i][j];
    					g=true;
    					c = a[i][j];
    					p = j + 1;
    				}

    		}
    		if(a[i][m - 1] == '?')
    			{
    	    	if(g)
    			{
    				for( k = p; k < j; k++)
    					a[i][k] = c;
    			}
    			else if(i != 0)
    			{
    				for(j = p; j < m; j++)
    					a[i][j] = a[i - 1][j];
    			}
    		  }

    		

    	}

    	for(i = n - 2; i>=0; i--)
    	{
    		for( j = 0; j < m; j++)
    		{
                if(a[i][j] == '?')
                	a[i][j] = a[i + 1][j];
    		}
    	}

    	cout<<"Case #"<<t<<":"<<"\n";
    	for(i=0;i<n;i++)
    	{
    	  for(j=0 ;j < m ;j++)
    	  	cout<<a[i][j];
    	  cout<<"\n";
    	}
    }
   
 return 0;
}