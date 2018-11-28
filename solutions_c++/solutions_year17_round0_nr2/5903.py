#include <bits/stdc++.h>
using namespace std;
int main()
{
	int T;
	string s;
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	cin>>T;
	for(int i=0; i<T; i++)
	{
		cin>>s;
		int index;
		int flag = 1;
		for(int j=1; j<s.length(); j++)
		{
			if(s[j] < s[j-1])
			{
				flag = 0;
				index = j - 1;
				break;
			}
		}
		cout<<"Case #"<<i+1<<": ";
		if(!flag)
		{
			while(index >= 0 && s[index] == s[index -1])
				index --;
			s[index] --;
			for(int j=index+1; j<s.length(); j++)
				s[j] = '9';
			int nonzero = 0;
			while(s[nonzero] == '0')
				nonzero ++;
			s = s.substr(nonzero, s.length() - nonzero);
		}
		cout<<s<<endl;
	}
	return 0;
}