#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define sc(a) scanf("%d",&a)
#define scl(a) scanf("%lld",&a)
#define pb(a) push_back(a)
typedef vector<int> vi;
int main()
{
	int t;
	sc(t);
	int tc=1;
	while(tc <= t)
	{
		string s;

		cin>>s;
		cout<<"Case #"<<tc++<<": ";
		
		string s2=s;

		int i=0;
		int n=s.length();

		while(i<n-1 && s[i]<=s[i+1])
			i++;

		int j=i+2;
		

		while(j<n)
			s[j++]='9';
		
		while(i>=0)
		{
			if(i<n-1 && s[i]>s[i+1])
			{
				s[i]--;
				s[i+1]='9';
			}
			i--;
		}

		j=0;
		while(j<n && s[j]=='0')
			j++;
		while(j < n)
			cout<<s[j++];
		cout<<endl;
	}
	return 0;
}