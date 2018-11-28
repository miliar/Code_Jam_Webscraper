/* Written BY
Aryan Kumar
ar412
*/

#include <bits/stdc++.h>
using namespace std;

int main()
{
	int t;
	cin>>t;
	for (int i = 1; i <= t; ++i)
	{
		string s;
		int k,count=0,flag=0;
		cin>>s>>k;
		cout<<"Case #"<<i<<": ";
		for (int j = 0; j < s.length(); ++j)
		{
			if(s.at(j)=='-' && j+k>s.length())
				{
//cout<<s.length()<<" "<<j<<" "<<k<<endl;
					flag=1;
					break;
				}
			if (s.at(j)=='-')
				{
					count++;
					for (int n = j; n < k+j; ++n)
					{
						if(s.at(n)=='+')
							s.at(n)='-';
						else
							s.at(n)='+';
					}
				}

		}

if(flag==0)
	cout<<count<<endl;
else cout<<"IMPOSSIBLE"<<endl;
		
	}

	return 0;
}	