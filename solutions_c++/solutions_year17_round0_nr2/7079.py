#include <iostream>
#include <string>

using namespace std;

int main()
{
	int t;
	cin>>t;
	
	for(int tc = 1; tc <= t; ++tc)
	{
		string s;
		cin>>s;
		int len = s.size();
		
		int ti = len;
		
		for(int i = len-2; i >= 0; --i)
		{
				if(s[i] > s[i+1])
				{
					s[i] = (char) ((int)(s[i]) - 1);
					ti = i+1;
				}
		}
		
		cout<<"Case #"<<tc<<": ";
		
		if(s[0] != '0')
		{
			cout<<s[0];
		}
		
		for(int i = 1; i<ti; ++i)
		{
			cout<<s[i];
		}
		
		for(int i = ti; i<len; ++i)
		{
			cout<<"9";
		}
		
		cout<<endl;
		
		
	}
	return 0;
}