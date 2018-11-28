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
		int l,i;
		cin>>s>>l;
		int len=s.length(),count=0;
		for(i=len-1;i>=l-1;i--)
		{
			if(s[i]=='-')
			{
				count++;
				for(int j=i;j>i-l;j--)
				{
					if(s[j]=='-')
					s[j]='+';
					else
					s[j]='-';
				}
			}
		}
		for(i=0;i<len;i++)
		if(s[i]=='-')
		count=-1;
		cout<<"Case #"<<t_case<<": ";
		if(count!=-1)
		cout<<count<<"\n";
		else
		cout<<"IMPOSSIBLE\n";
		
	}
	return 0;
}
