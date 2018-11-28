#include<bits/stdc++.h>
#define NINF INT_MIN 
#define INF INT_MAX
#define ull unsigned long long
#define ld long double
#define ll long long
#define M 1000000009
#define REM 4
#define N 100005
#define pll pair<ll,ll>
#define pb(x) push_back(x)
#define mset(a) memset(a,0,sizeof(a))
#define sc(x)  scanf("%c",&x)
#define si(a)  scanf("%d",&a)
#define sl(a) scanf("%lld",&a)
#define f(i,n) for(i=0;i<n;i++)
#define foi(i,j,k) for(i=j;i<k;i++)
#define mll map<ll,ll>
#define foe(i,j,k) for(i=j;i<=k;i++)
 
#define dbg(x) cout<<#x<<"="<<x<<endl;
using namespace std;

 
int main()
{
	int t,l,i,j,x,k,flag,flag1,cs=1;;
	string str,s;
	char ch;
	cin>>t;
	while(t--)
	{
		cin>>str;
		l=str.length();
		flag=0;flag1=0;
		for(i=1;i<l;i++)
			if(str[i]<str[i-1]){flag=1;break;}
		if(flag==1)
		{
			for(j=i-1;j>=0;j--)
				if(str[j]!='0' && str[j]!='1'){flag1=1;break;}
			if(flag1==1)
			{
				// dbg(str[j]);
				ch=str[j];
				x=ch-'0';
				x--;
				str[j]=char('0'+x);
				for(k=j+1;k<l;k++)str[k]='9';

				
				k=j-1;
				while(k>=0)
				{
					if(str[k]>str[k+1])
					{
						str[k+1]='9';
						ch=str[k];
						x=ch-'0';
						x--;
						str[k]=char('0'+x);
						k--;
					}
					else break;
				}
			}
	    	else
	    	{
	    		str="";
	    		for (int i = 0; i < l-1; ++i)
	    		{
	    			str+="9";
	    		}
	    	}
		}
		
			cout<<"Case #"<<cs<<": "<<str<<endl;
			cs++;
	}
	
	return 0;
}