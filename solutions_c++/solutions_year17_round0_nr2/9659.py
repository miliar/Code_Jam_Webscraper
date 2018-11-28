#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>

using namespace std;

bool isTidy(int n)
{
	stringstream ss;
	ss<<n;
	string s;
	ss>>s;
	for(int i = 1; i < s.size(); i++)
	{
		if(s[i] < s[i-1])
		{
			return false;
		}
	}
	return true;
}
main()
{
	int t;
	freopen("input.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin>>t;
	//cout<<t<<endl;
	for(int cases = 1; cases <= t; cases++)
	{
		int n;
		cin>>n;
		do
		{
			if(isTidy(n))
			{
				break;
			}
			//cout<<n<<endl;
		}while(n--);
		cout<<"Case #" << cases << ": "<< n <<endl;
	}
}
