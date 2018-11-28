#include <bits/stdc++.h>
using namespace std;



int main()
{
	int T; cin >> T;
	for(int t = 1; t <= T; t++)
	{
		string s; int K;
		cin >> s >> K;
		
		int r = 0;
		for(int i = 0; i <= int(s.size()) - K; i++)
		{
			if(s[i] == '-')
			{
				r++;
				for(int j = i; j < i + K; j++)
					s[j] = s[j] == '+' ? '-' : '+';
			}
		}
		bool imp = false;
		for(int i = 0; i < int(s.size()); i++)
			if(s[i] == '-')
				imp = true;
		if(imp)
			cout << "Case #" << t << ": " << "IMPOSSIBLE" << endl;
		else
			cout << "Case #" << t << ": " << r << endl;
	}
	
	
	return 0;
}
