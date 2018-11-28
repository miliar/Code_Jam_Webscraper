#include <bits/stdc++.h>
using namespace std;

#define cr(x) cerr<<#x<<"= "<<x<<'\n'
#define int long long

typedef pair <int, int > pii;

int32_t main()
{
	ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
	int t;
	cin>>t;
	for(int tcnt=1;tcnt<=t;tcnt++)
	{
		string s;
		cin>>s;
		int n=(int)s.size(), lst=0;
		for(int i=1;i<n;i++)
		{
			if(s[i]<s[i-1])
			{
				s[lst]--;
				for(int j=lst+1;j<n;j++)
					s[j]='9';
				break;
			}
			if(s[i]>s[i-1]) lst=i;
		}
		cout<<"Case #"<<tcnt<<": ";
		bool b=0;
		for(int i=0;i<n;i++)
		{
			if(s[i]!='0'||b)
				cout<<s[i], b=1;
		}
		cout<<'\n';
	}
}
