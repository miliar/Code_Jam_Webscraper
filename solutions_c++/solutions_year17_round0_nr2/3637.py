		/*masterwayne*/
#include<bits/stdc++.h>
using namespace std;
#define sc(x) scanf("%d",&x)
#define sc2(x,y) scanf("%d %d",&x,&y)
#define sc3(x,y,z) scanf("%d %d %d",&x,&y,&z)
#define pf(x) printf("%d",x)
#define pf2(x,y) printf("%d %d",x,y)
#define pf3(x,y,z) printf("%d %d %d",x,y,z)
#define fr(i,x,n) for(int i=x;i<n;i++)
#define fre(i,x,n) for(int i=x;i<=n;i++)
#define fb(i,x,n) for(int i=n-1;i>=x;i--)
#define fbe(i,x,n) for(int i=n;i>=x;i--)
#define pfn() printf("\n")
#define pfs() printf(" ")
#define pb push_back
#define f_in(st) freopen(st,"r",stdin)
#define f_out(st) freopen(st,"w",stdout)
#define mod 1000000007
void solve(string input,string output)
{
	f_in(input.c_str());
	f_out(output.c_str());
	int t;
	cin>>t;
	int c=1;
	string s;
	while(t--)
    {
    	cin>>s;
    	int n = s.length();
    	cout<<"Case #"<<c<<": ";
    	for(int k=0;k<n;k++)
    	{
    		for(int j=1;j<n;j++)
    		{
    			if(s[j-1]<=s[j])
    				continue;
    			else
    			{
    				s[j-1]--;
    				while(j<n)
    				{
    					s[j]='9';
    					j++;
    				}
    			}
    		}
    	}
    	c++;
    	for(int i=0;i<n;i++)
    	{
    		if(i==0 && s[i]=='0')
    		{
    			continue;
    		}
    		cout<<s[i];
    	}
    	cout<<endl;
    }
}
int main()
{
	solve("blarge.in","bout11.txt");
	return 0;
}