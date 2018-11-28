#include <bits/stdc++.h>
#define endl '\n'
using namespace std;
typedef long long int ll;

main()
{
	ll t, num, cases=1;
	string str,aux;
	
	cin >> t;
	
	while(t--)
	{
		cin.ignore();
		cin >> str;
		
		ll cont = 1;
		for(ll i = 0; i < str.size()-1; i++)
		{
			if(str[i] > str[i+1])
			{
				str[i]--;
				for(ll j = i+1; j < str.size(); j++)
					str[j] = '9';
				i = -1;
			}
		}
		
		ll num = stoll(str);
		cout << "Case #" << cases++ << ": " << to_string(num) << endl;
	}
}
