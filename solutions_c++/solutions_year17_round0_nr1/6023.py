/*input
3
---+-++- 3
+++++ 4
-+-+- 4
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
		int cnt=0;
		string str;
		int n;
		cin>>str>>n;
		for(int i=0;i<str.length();++i)
		{
			if(str[i]=='+')
				continue;
			else
			{
				if((i+n-1)>=str.length())
					break;
				else
					{
						for (int j = 0; j < n; ++j)
						{
							str[j+i]=='+'?str[j+i]='-':str[j+i]='+';
							/* code */
						}
						//cout<<str<<endl;
						cnt++;
					}
			}
		}
		int flag=0;
		for (int i = 0; i < str.length(); ++i)
		{
			/* code */
			if(str[i]=='-')
			{
				flag=1;
				break;
			}
		}
		if(flag==0)
			cout<<"Case #"<<f<<": "<<cnt<<endl;
		else
			cout<<"Case #"<<f<<": "<<"IMPOSSIBLE"<<endl;
	}	
	return 0;
}
