#include <bits/stdc++.h>
#define ll long long int
#define pb push_back
#define f first
#define s second
#define mp make_pair
#define max 200005           
#define num 5000000
#define fastio ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0)
using namespace std;

int main() {
        fastio;
	int t,i;
	cin>>t;
	for(i=1;i<=t;i++)
	{
		char ch[29];
		int l,a[29],k,m;
		cin>>ch;
		l=strlen(ch);
		for(k=0;k<l;k++)
		{
		    a[k]=ch[k]-'0';
		    
		}
	    for(k=0;k<l-1;k++)
	    {
	        if(a[k]>a[k+1])
	        {
	            a[k]=a[k]-1;
	            for(m=k+1;m<l;m++)
	            {
	                a[m]=9;
	            }
	            if(k>0)
	            {
	                for(m=k-1;m>=0;m--)
	                {
	                    if(a[m]>a[m+1])
	                     {
	                         a[m]--;
	                         a[m+1]=9;
	                     }
	                }
	            }
	        }
	    }
		int c=0;
		cout<<"Case #"<<i<<": ";
		for(k=0;k<l;k++)
		{
		    if(a[k]==0 && c==0)
		     continue;
		    else
		     {
		         cout<<a[k];
		         c++;
		     }
		     
		}
		cout<<'\n';
		
		
	}
	return 0;
}