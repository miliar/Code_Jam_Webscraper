#include<bits/stdc++.h>
using namespace std;

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int t; cin>>t;
	for (int j = 1;j<=t;j++)
	{
		string s; cin>>s;
		string ans;
		ans += s[0];
		for (int i = 1;i<s.size();i++)
		{
			if (s[i]>=ans[i-1]) ans += s[i];
			else
			{
				int j=i-1;
				while (j>0 && (ans[j-1] > ans[j]-1)) j--;
				ans[j]--;
				for (int x = j+1;x<=i-1;x++) ans[x] = '9';
				for (int x = i;x<s.size();x++) ans += '9';
				break;
			}
		}
		cout<<"Case #"<<j<<": ";
		int i = 0;
		while (ans[i]=='0') i++;
		while (i<ans.size()) { 
			cout<<ans[i]; i++; }
		cout<<endl;
	}
	return 0;
}
