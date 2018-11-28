#include <iostream>
#include <string>
using namespace std;

int main()
{
	int t, k;
	string s;

	cin >> t;

	for(int tc=1; tc<=t; ++tc)
	{
		cin >> s;
		cin >> k;
		
		int n = s.length(), i;
		int flips = 0;
		for(i=n-1; i-(k-1)>=0; --i)
		{
			if(s[i] == '-')
			{
				++flips;
				for(int j=i-(k-1); j <=i; ++j)
					s[j] = ((s[j] == '-') ? '+' : '-');
			}
		}

		// check if all '+'
		for(i=0; i<n; ++i)
		{
			if(s[i] == '-')
				break;
		}

		cout << "Case #"<< tc <<": ";

		if(i == n)
			cout << flips << endl;
		else
			cout <<"IMPOSSIBLE\n";
	}
	
	return 0;
}