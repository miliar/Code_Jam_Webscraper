#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
#include <functional>
#include <unordered_map>
#include <stack>
#include <queue>
#include <deque>

using namespace std;

int main()
{
	int N;
	cin >> N;
	cin.ignore();

	for (int n = 1; n <= N; ++n)
	{
		int k, cnt = 0;
		string line;
		getline(cin, line, ' ');
		cin >> k;

		auto isPossible = [](string &line, int k) -> bool {
			for (int i = line.size() - k; i < line.size(); ++i)
				if (line[i] == '-') return false;
			return true;
		};

		char map[128];
		map['+'] = '-';
		map['-'] = '+';

		for (int i = 0; i <= line.size() - k; ++i)
		{
			if (line[i] == '-')
			{
				for (int j = i; j < i + k; j++) line[j] = map[line[j]];
				cnt++;
			}
				
		}

		printf("Case #%d: ", n);
		if (isPossible(line, k)) cout << cnt << endl;
		else cout << "IMPOSSIBLE" << endl;
	}
}