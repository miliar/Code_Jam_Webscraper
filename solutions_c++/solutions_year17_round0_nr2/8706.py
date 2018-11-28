#include <iostream>
#include <vector>
#include <unordered_map>
#include <string>

using namespace std;

unordered_map<unsigned long long, unsigned long long> tbl;

unsigned long long search(const unsigned long long& N)
{
	if (N < 10)
		return N;

	auto&& res = tbl.find(N);
	if (res != tbl.end())
		return res->second;

	unsigned long long num = 0, tmp = N;
	unsigned cnt = 0;

	while (tmp > 10) tmp /= 10, cnt++;

	unsigned long long tmp2 = pow(10, cnt);

	for (unsigned i = 1; i <= tmp; ++i)
		num += search(N - i * tmp2);
	tbl[N] = num;

	return num;
}


int main()
{
	ios::sync_with_stdio(false);

	int t;
	cin >> t;
	
	for (unsigned i = 1; i <= t; ++i)
	{
		unsigned long long N, K;
		cin >> N;// >> K;

		string tmp = to_string(N);
		string res = string(1, tmp[0]);
		unsigned j;
		for (j = 1; j < tmp.length(); ++j)
		{
			if (tmp[j] < tmp[j - 1])
				break;
		}
		res = tmp.substr(0, j) + string(tmp.length() - j, '9');
		if (j < tmp.length())
		{
			res[--j]--;
			while (j > 0 && res[j] < res[j - 1])
			{
				res[j - 1]--;
				res[j] = '9';
				j--;
			}
		}
		//vector<unsigned long long> vec(N);

		//cout << "Case #" << i << ": " << search(N);
		cout << "Case #" << i << ": " << stoull(res) << '\n';
	}

	return 0;
}