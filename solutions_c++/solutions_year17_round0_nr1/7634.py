#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

void flip(string &in, int inx, int k)
{
	for(int i = 0; i < k; i++)
	{
		if (in.at(inx + i) == '-')
		{
			in[inx + i] = '+';
		}
		else {
			in[inx + i] = '-';
		}
	}
}

bool check(string in, int k)
{
	for(int i = 0 ; i < k ; i++)
	{
		if(in[in.size() - 1 - i] == '-')
			return false;
	}
	return true;
}

int solve(string in, int k)
{
	int res = -1;
	int cnt = 0;
	string temp = in;
	
	
	for (int i = 0 ; i < (int)in.size() - k + 1; i++) 
	{
		if(in.at(i) == '-')
		{
			flip(in, i, k);
			cnt++;
		}
	}

	if (check(in, k))
		res = cnt;
	return res;
}

int main()
{
	string in;
	int T;
	int K;
	//~ freopen("out.txt", "w", stdout);
	//~ freopen("A-large.in", "r", stdin);
	cin >> T;
	for (int i = 0; i < T; i++)
	{
		cin >> in;
		cin >> K;
		int res = solve(in , K);
		//~ std::reverse(in.begin(), in.end());
		//~ int res2 = solve(in, K);
//~ 
		//~ if (res != -1 && res2 != -1)
			//~ res = std::min(res, res2);
		//~ else if(res == -1)
			//~ res = res2;

		cout << "Case #" << i + 1 << ":  ";
		if (res == -1)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << res << endl;
	}
	return 0;
}
