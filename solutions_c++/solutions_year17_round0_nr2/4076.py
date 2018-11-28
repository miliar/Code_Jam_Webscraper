#include <bits/stdc++.h>
using namespace std;
#define mod 1000000007
#define INF 1000000000
#define LINF 1000000000000000000  
typedef long long 		ll;
typedef vector<int>		vi;
typedef pair<int, int>		ii;
typedef vector<ii>		vii;
typedef set<int>		si;
typedef map<string, int>	msi;
#define REP(i, a, b)  for (int i = int(a); i <= int(b); i++)
#define TRvi(c, it)  for (vi::iterator it = (c).begin(); it != (c).end(); it++)
#define TRvii(c, it)  for (vii::iterator it = (c).begin(); it != (c).end(); it++)
#define TRmsi(c, it)  for (msi::iterator it = (c).begin(); it != (c).end(); it++)
#define pb push_back
#define mk make_pair
int main()
{
	ios_base::sync_with_stdio(false);
	int t,t_case;
	cin>>t;
	REP(t_case,1,t)
	{
		string s;
		cin>>s;
		int flag=0,len=s.length()-1,i;
		i=len;
		long long ans=0,temp=1,ans2=0;
		while(i!=-1)
		{
			temp*=10;
			if(i!=0)
			{
				ans2+=(9*temp)/10;
			}
			if(i==0 && s[i]>='2')
			{
				ans2+=((int)(s[i]-'1')*temp)/10;
			}	
			i--;
		}
	//	cout<<ans2;
		while(flag==0)
		{
			flag=1;
			for(i=len-1;i>=0;i--)
			{
				if(s[i+1]<s[i])
				{
					s[i+1]='9';
					if(s[i]=='0')
					{
						s[i]='9';
						int j=len;
						while(j!=i)
						{
							s[j]='9';
							j--;
						}
						j=i;
						while(s[j]=='0')
						{
							s[j]='9';
							j--;
						}
						s[j]--;
					}
					s[i]--;
					flag=0;
				}
			}
		}
		i=len;
		temp=1;
		while(i!=-1)
		{
			ans+=temp*(int)(s[i]-'0');
			temp*=10;
			i--;
		}
		cout<<"Case #"<<t_case<<": "<<max(ans,ans2)<<"\n";
		
	}
	return 0;
}
