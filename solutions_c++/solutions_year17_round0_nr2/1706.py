#include <bits/stdc++.h>
using namespace std;

int main()
{
	ios_base::sync_with_stdio(false);
	freopen("input.txt","r",stdin); freopen("output.txt","w",stdout);
	int tc;
	cin>>tc;
	for(int tmp=1;tmp<=tc;tmp++)
	{
		string s;
		cin>>s;
		string ans;
		for(int temp=0;temp<s.size();temp++)
		{
			char next='9';
			for(int temp2=temp+1;temp2<s.size();temp2++)	if(s[temp2]!=s[temp])	{next=s[temp2];break;}
			//cout<<s[temp]<<" "<<next<<"\n";
			if(next>=s[temp])
			{
				ans+=s[temp];
			}
			else
			{
				ans+=int(s[temp])-1;
				for(int temp2=temp+1;temp2<s.size();temp2++)
				{
					ans+='9';
				}
				break;
			}
		}
		cout<<"Case #"<<tmp<<": "<<stoll(ans)<<"\n";
	}
}
