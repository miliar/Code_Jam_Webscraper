#include <iostream>
using namespace std;

string flip(string s,int i,int k){
	for (int j = i; j < i + k; ++j)
	{

		if(s[j]==43)s[j]='-';
		else if(s[j]==45)s[j]='+';

	}
	return s;
}

int main()
{
	int t;
	cin>>t;
	int t_t = t;
	while(t--)
	{
		cout<<"Case #"<<(t_t - t)<<": ";
		int k,flip_count=0;
		string s;
		cin>>s>>k;

		bool done = 1;
		for (int i = 0; i < s.size(); ++i)
		{
			if(s[i]==45){
				done = 0;
			}
		}
		if (done)
		{
			cout<<0<<endl;
			continue;
		}

		if(k>s.size()){
			cout<<"IMPOSSIBLE"<<endl;
		    continue;
		}
		int sz = s.size();
		for (int i = 0; i < sz - k + 1; ++i)
		{
			if(s[i]==45){
				flip_count++;
				s=flip(s,i,k);
				// cout<<s<<endl;
			}
		}
		done = 0;
		for (int i = 0; i < s.size() && !done; ++i)
		{
			if(s[i]==45){
				cout<<"IMPOSSIBLE"<<endl;
				done = 1;
			}
		}
		if(!done)cout<<flip_count<<endl;

	}
	return 0;
}