
#include <bits/stdc++.h>

using namespace std;
long long o;



int main()
{
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++)
	{

		cout <<"Case #"<<t <<": ";
		string s;
		cin >> s;
	
	   while(1)
	   {
	   	int flag = 1;
	   	for(long long i = 0; i < s.length ()-1; i++)
	   	{
	   		if (s[i] > s[i+1] )
	   		{
	   			flag = 0;
	   			break;
	   		} 

	   	}
	   	if (flag )
	   	{
	   		o = stoll(s, NULL);
			cout << o << endl;
			break;

	   	}
		for(long long i = 0; i < s.length()-1; i++)
		{
			if (s[i] > s[i+1])
			{
				for(long long j = i; j >= 0; j--)
				{
					if (s[j] != '0')
					{
						s[j]--;
						for(long long k = j+1; k < s.length(); k++)
							s[k] = '9';
						break;
					}
				}
			}
		}
	  }
	

	
	}
	return 0;
}