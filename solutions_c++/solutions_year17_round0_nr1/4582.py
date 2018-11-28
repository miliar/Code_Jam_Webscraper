/*input
3
---+-++- 3
+++++ 4
+-+ 2
*/
#include <bits/stdc++.h>

using namespace std;

int main(int argc, char const *argv[])
{
	ios_base::sync_with_stdio(false);
	int test, z;
	cin>>test;
	for(z = 1; z <= test; z++)
	{
		cout<<"Case #"<<z<<": ";
		string s;
		int k;
		int cnt = 0;
		int notPossible = 0;
		cin>>s;
		cin>>k;
		int i, j;
		for(i = 0; i < s.length(); i++)
		{
			if(s[i] == '-')
			{
				cnt++;
				for(j = i; j < i+k ; j++)
				{
					if( j >= s.length() )
					{
						notPossible = 1;
						break;
					}
					s[j] == '-'? s[j] = '+': s[j] = '-';
				}
			}
			if(notPossible)
				break;
		}
		if(notPossible)
			cout<<"IMPOSSIBLE"<<endl;
		else
			cout<<cnt<<endl;
	}
	return 0;
}