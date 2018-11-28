#include <iostream>

using namespace std;

void solve()
{
	string s;
	cin>>s;
	int n = s.size();
	s += '9';
	bool fl = false;
	while(!fl)
	{
		fl = true;
		for(int i=0; i<n; i++)
			if(!fl) s[i] = '9'; else
			if(s[i]>s[i+1]) {
				s[i]--;
				fl = false;
			}
	}
	fl = false;
	for(int i=0; i<n; i++)
		if(fl || s[i]>'0') 
			cout<<s[i], fl = true;
	cout<<endl;
}

int main()
{
	int T;
	cin>>T;
	for(int i=1; i<=T; i++) 
	    cout<<"Case #"<<i<<": ",
		solve();
	return 0;
}