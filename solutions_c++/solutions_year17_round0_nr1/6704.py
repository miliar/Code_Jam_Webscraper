#include <iostream>
#include <string>

using namespace std;

int main()
{
	ios::sync_with_stdio(false);
	
	int T;
	cin >> T;
	
	for(int l = 1; l <= T; l++)
	{
		cout << "Case #" << l << ": ";
		
		string s;
		cin >> s;
		
		int k;
		cin >> k;
		
		int len = s.size();
		bool chk[len] = {};
		
		for(int i = 0; i < len; i++)
			if(s[i] == '+')
				chk[i] = 1;
		
		int cnt = 0;
		for(int i = 0; i +k <= len; i++)
		{
			if(chk[i] == 0)
			{
				cnt++;
				int curr = 0;
				for(int j = i; curr != k; j++, curr++)
					chk[j] = 1 -chk[j];
			}
		}
		
		int i = 0;
		for(i = 0; i < len; i++)
		{
			if(chk[i] == 0)
			{
				cout << "IMPOSSIBLE\n";
				break;
			}
		}
		
		if(i == len)
			cout << cnt << endl;
	}
	
	return 0;
}
