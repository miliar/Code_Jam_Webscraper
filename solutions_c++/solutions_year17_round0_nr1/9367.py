#include <vector>
#include <algorithm>
#include <bitset>
#include <iostream>
using namespace std;


int main(int argc, char const *argv[])
{
	int t;
	int n = 0,k;
	cin >> t;
	while(t--)
	{
		string s;
		cin >> s >> k;
		string auxi = "";
		int ans = 0;
		for (int i = 0; i < s.size(); ++i)
		{
			auxi.push_back('+');
		}
		for (int i = 0; i < s.size(); i++)
		{
			//cout << i << endl;
			if (s[i] == '-' && (i + k) < s.size() + 1)
			{
				//cout << s << endl;
				for (int j = i; j < i + k; j++)
				{
					//cout << s[j]<< endl;
					if (s[j] == '-')	 
						s[j] = '+'; 
					else 
						s[j] = '-';
				}
				ans++;
			}
		}
//		cout <<"s = "<< s << endl;
			if (s == auxi)
		{
			cout << "Case #" << ++n << ": "; 
			cout << ans << endl;			
		}
		else 
			cout << "Case #" << ++n << ": IMPOSSIBLE" << endl; 
	}
	return 0;
}