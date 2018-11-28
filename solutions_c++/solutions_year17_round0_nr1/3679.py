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
	while(c<=t)
	{
		string s;
		cin>>s;
		int k;
		cin>>k;
		int flag=1;
		int mini=0;
		for(int i=0;i<s.length();i++)
		{
			if(s[i]=='-')
			{
				if(i+k>s.length())
				{
				flag=0;
				break;
			    }
			    mini++;
			    for(int j=i;j<i+k;j++)
			    {
			    	if(s[j]=='-')
			    		s[j]='+';
			    	else
			    		s[j]='-';
			    }
			}
		}
		cout<<"Case #"<<c<<": ";
		if(!flag)
			cout<<"IMPOSSIBLE"<<endl;
		else
			cout<<mini<<endl;
		c++;
	}
}
int main()
{
	solve("alarge.in","alout.txt");
	return 0;
}