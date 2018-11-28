#include<iostream>
#include<cstdio>
#include<string>

using namespace std;

void getTidy(string &s){
	int ssize=s.size();
	for(int i=ssize-1; i>0; i--)
	{
		if(s[i]<s[i-1])
		{
			s[i-1]--;
			for(int j=i; j<ssize; j++)
				s[j]='9';
		}
	}
	if(s[0]=='0')
		s.erase(s.begin());
}


int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("Blres.out", "w", stdout);
	int T;
	cin>>T;
	string s;
	for(int t=1; t<=T; t++)
	{
		cin>>s;
		if(s.size()!=1)
			getTidy(s);
		cout<<"Case #"<<t<<": "<<s<<endl;
	}

	return 0;
}
