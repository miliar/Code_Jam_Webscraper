#include <iostream>
#include <string>
using namespace std;


//0 1 2 3 4 5 k=2,size=6
//		^
bool check(const string &s,const int &k)
{
	for(int i = s.size()-k; i < s.size(); i++)
		if(s[i] == '-') return false;
	return true;
}

int main()
{
	int T;
	string s;
	cin>>T;

	for(int t = 1, k, ans=0; t <= T ; t++, ans=0)
	{
		cin>>s>>k;
		//cout<<s<<' '<<k<<endl;
		for(int i = 0;i <= (s.size()-k); i++)
			if(s[i] == '-')
			{
				for(int j = i; j < (i+k); j++)
					if(s[j] == '-') s[j] = '+';
					else s[j] = '-';
				
				//cout<<s<<endl;
				ans++;
			}

		cout<<"Case #"<<t<<": ";
		if(check(s,k)) cout<<ans<<endl;
		else cout<<"IMPOSSIBLE"<<endl;
	}

	return 0;
}
/*
3
---+-++- 3
++++-++-
+++++---*/