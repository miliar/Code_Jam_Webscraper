#include <iostream>
#include <set>
#include <cstdio>
using namespace std;
int main(void)
{
	freopen("input_file_name.in","r",stdin);
	freopen("output.out","w",stdout);
	int t;
	cin>>t;
	int c=1;
	while(t--)
	{
		int tries=0;
		string s;
		int k;
		cin>>s>>k;
		for(int i=s.size()-1;i>=k-1;i--)
		{
			if(s[i]=='+')continue;
			else
			{
				tries++;
				for(int j=0;j<k;j++)
				{
					if(s[i-j]=='+')s[i-j]='-';
					else s[i-j]='+';
 
				}
			}
		}
		std::size_t found ;
		//cout<<s<<endl;
		found=s.find('-');
		if(found!=std::string::npos)cout<<"Case #"<<c++<<": "<<"IMPOSSIBLE"<<endl;
		else cout<<"Case #"<<c++<<": "<<tries<<endl;
	}
	return 0;
}