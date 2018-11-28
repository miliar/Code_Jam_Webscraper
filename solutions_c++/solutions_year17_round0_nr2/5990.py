/*input

*/

#include <iostream>
#include <vector>
#include <string>
using namespace std;
#define endl "\n"
typedef long long int LL;
 
int main()
{
	ios_base:: sync_with_stdio(false); cin.tie(0);
	int t;
	cin>>t;
	for(int f=1;f<=t;f++)
	{
		string str;
		cin>>str;
		vector< int > mv;
		for(int i=0;i<str.length();i++)
		{
			mv.push_back(str[i]-'0');
		}
		for(int i=mv.size()-2;i>=0;i--)
		{
			if(mv[i]<=mv[i+1])
				continue;
			else
			{
				mv[i]-=1;
				for(int j = i+1;j<mv.size();j++)
					mv[j] = 9;
			}
		}
		cout<<"Case #"<<f<<": ";
		while(*mv.begin()==0)
			mv.erase(mv.begin());
		for(auto i:mv)
			cout<<i;
		cout<<endl;	
	}	
	return 0;
}
