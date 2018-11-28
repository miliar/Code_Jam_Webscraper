#include <iostream>
using namespace std;
int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);

	int T, no=0;
	cin>>T;
	while(T--)
	{
		string s;
		cin>>s;
		int p=-1;
		for(int i=0;i+1<s.size();i++)
			if(s[i]>s[i+1])
			{
				p=i;
				break;
			}
		if(p!=-1)
		{
			while(p>0 && s[p]==s[p-1]) p--;
			s[p]--;
			for(int i=p+1;i<s.size();i++)
				s[i]='9';
		}
		cout<<"Case #"<<++no<<": "<<stoll(s)<<'\n';
	}
}