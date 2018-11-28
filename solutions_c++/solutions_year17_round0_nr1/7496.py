#include<iostream>
#include<string>
using namespace std;




int solve(string s, int k)
{
	int ret = 0;
	int i = 0;
	int size = s.size();
	while (i + k <= size)
	{
		if (s[i] == '-')
		{
			ret++;
			for (int j = 0; j < k; j++)
				s[i + j] = s[i + j] == '-' ? '+' : '-';
		}
		i++;
	}
	if (size < k)
	{
		bool flag = true;
		for (int i = 1; i <= k; i++)flag &= s[size - i] != '-';
		if (true)return 0;
		else return -1;
	}
	bool flag = true;
	for (int i = 1; i <= k; i++)flag &= s[size - i] != '-';
	if(flag)return ret;
	else return -1;
}

int main()
{
	int T;
	//freopen("A-small-attempt6.in", "r", stdin);
	//freopen("A-small-attempt6.out", "w", stdout);
	ios::sync_with_stdio(false);
	cin >> T;
	for (int tc = 1; tc <= T; tc++)
	{
		
		cout << "Case #" << tc << ": ";
		string s;
		int k;
		cin >> s >> k;
		//if (tc == 57)
		//	int debug = 1;
		int ret = solve(s, k);
		if (ret == -1)cout << "IMPOSSIBLE" << endl;
		else cout << ret << endl;
	}
	//fclose(stdin);
	//fclose(stdout);

	return 0;
}