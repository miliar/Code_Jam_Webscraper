#include <bits/stdc++.h>
using namespace std;
#define ll unsigned long long int 
int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	int T;
	cin>>T;
	for(int qq=1;qq<=T;qq++)
	{
		ll ans = -1,N;
		cin>>N;
		string s = to_string(N);
		string t = s;
		sort(t.begin(), t.end());
		if(t==s) ans = N;
		else
		{
			int len = s.length();
			if(s[0]=='9') 
			{
				s[0]='8';
				for(int i=1;i<len;i++) s[i]='9';
			}
			else 
			{
				s[len-1]='9';
				if(s[len-2]!='0') s[len-2]--;
				for(int i=len-2;i>=1;i--)
				{
					if(s[i]=='0') 
					{
						s[i]='9';
						if(s[i-1]!='0')	s[i-1]--;
					}
					else
					{
						if(s[i]>=s[i-1]) continue;
						else s[i]--,i++;
					}
				}
			}
			ans = stoull(s);
		}
		printf("Case #%d: %I64d\n",qq,ans);
	}
	return 0;
}