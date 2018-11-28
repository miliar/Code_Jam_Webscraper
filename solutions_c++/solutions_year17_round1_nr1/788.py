#include<iostream>
#include<vector>
#include<string>
#define M 30
using namespace std;
int main(void)
{
	int T;
	cin >> T;
	for (int z = 1; z <= T; ++z)
	{
		int r, c;
		string in[M];
		cin >> r >> c;
		for (int i = 0 ; i < r; ++i)
			cin >> in[i];
		
		string ans[M];
		for (int i = 0; i < r; ++i)
		{
			int idx = 0;
			while (in[i][idx] == '?' && idx < c)
				++idx;
			
			if (idx == c)
				continue;

			char now = in[i][idx];
			for (int j=0; j < idx; ++j)
				ans[i].push_back(now);
			
			for (int j = idx; j < c; ++j)
			{
				if (in[i][j] != '?')
					now = in[i][j];
				ans[i].push_back(now);
			}
		}
		for (int i= 0; i < r; ++i)
		{
			if (ans[i].size() == 0)
			{
				for (int j = i; j >= 0 ; --j)
				{
					if (ans[j].size() != 0)
					{
						ans[i] = ans[j];
						break;
					}
				}
			}
			
			if (ans[i].size() == 0)
			{
				for (int j = i; j < r ; ++j)
				{
					if (ans[j].size() != 0)
					{
						ans[i] = ans[j];
						break;
					}
				}
			}
		}

		cout << "Case #" << z << ": " << endl;
		for (int i = 0; i < r; ++i)
		{
			cout << ans[i] << endl;
		}
	}
}

