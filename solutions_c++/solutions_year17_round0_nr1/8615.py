#include <iostream>
#include <vector>
#include <unordered_map>
#include <string>
#include <algorithm>
#include <fstream>

using namespace std;

unordered_map<unsigned long long, unsigned long long> tbl;

unordered_map<string, unsigned> tbl2;
unordered_map<string, unsigned> tasks;


unsigned search(const string& s, const unsigned &K, const unsigned& depth)
{
	auto&& it = tbl2.find(s);
	const char * pTmp = s.c_str();
	if (it != tbl2.end())
		return it->second;

	auto&& task = tasks.find(s);
	if (task != tasks.end() && task->second <= depth)
		return -1;
	
	tasks.insert(make_pair(s, depth));

	unsigned res = -1;

	unsigned cnt = 0;
	for (char c : s)
		cnt += (c == '+');
	if (cnt == s.length())
		res = 0;
	else
	{
		for (unsigned x = K; x <= s.length(); ++x)
		{
			string tmp = s;

			for (unsigned j = x - K; j < x; ++j)
				tmp[j] = s[j] == '+' ? '-' : '+';
			unsigned searchVal = search(tmp, K, depth + 1);
			if (searchVal != -1)
				res = std::min(res, searchVal + 1);
		}
	}
	

	tasks.erase(s);
	tbl2.insert(make_pair(s, res));

	return res;
}

int main()
{
	ios::sync_with_stdio(false);

	int t;
	cin >> t;
	//ofstream ofs("tmp.txt");
	for (unsigned i = 1; i <= t; ++i)
	{
		unsigned K;
		string S;
		cin >> S >> K;
		tbl2.clear();
		tasks.clear();
		unsigned res = search(S, K, 0);

		cout << "Case #" << i << ": " << (res == -1 ? "IMPOSSIBLE" : to_string(res)) << '\n';
		//ofs << "Case #" << i << ": " << (res == -1 ? "IMPOSSIBLE" : to_string(res)) << '\n';
	}
	//ofs.close();
	return 0;
}