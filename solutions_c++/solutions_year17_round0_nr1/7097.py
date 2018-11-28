#include <iostream>
#include <string>

using namespace std;

int main()
{
	// your code goes here
	int t, k;
	string s;
	
	cin>>t;
	
	for(int tc = 1; tc <= t; ++tc)
	{
		cin>>s;
		
		cin>>k;
		
		int lb = s.size() - k;
		int cnt = 0;
		bool poss = true;
		
		for(int i=0; i<lb; ++i)
		{
			if(s[i] == '-')
			{
				++cnt;
				
				for(int j=i; j<i+k; ++j)
				{
					if(s[j] == '-')
						s[j] = '+';
					else
						s[j] = '-';
				}
			}
		}
		
		for(int k =lb+1; k<s.size(); ++k)
		{
			if(s[k] != s[k-1])
			{
				poss = false;
				break;
			}
		}
		
		cout<<"Case #"<<tc<<": ";
		
		if(poss)
		{
			if(s[s.size()-1] == '-')
			{
			  	++cnt;
			}
			
			cout<<cnt<<endl;
		}
		else
		{
			cout<<"IMPOSSIBLE"<<endl;
		}
		
	}
	
	return 0;
}