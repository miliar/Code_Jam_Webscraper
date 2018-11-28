#include<iostream>
#include<vector>
#include<string>
#include<algorithm>

using namespace std;
int main()
{
	int T;

	string line;

	cin >> T;
	for (int i = 1; i <= T; i++)
	{
		vector<char> h;
		cin >> line;
		unsigned long long  num = stoull(line, nullptr, 10);
		for (int j = 0; j < line.length(); j++)
		{
			h.push_back(line.at(j));
		}

		if (!is_sorted(h.begin(), h.end()))
		{
			int k;
			for (k = 1; k < h.size(); k++)
			{
				if (h[k - 1] >= h[k])
					break;
			}
			int num = (int)h[k - 1] - '0';
			int bnum = (int)h[0] - '0';
			if (bnum == 9) {
				h[0] = '8';
			}
			else {
				num--;
				h[k - 1] = (char)num + '0';
			}
			for (int j = k; j < h.size(); j++)
			{
				h[j] = '9';
			}
			cout << "Case #" << i << ": ";
			if (h[0] == '0')
			{
				h[0] = '9';
				h.pop_back();
			}
			for (int j = 0; j < h.size(); j++)
				cout << h[j];
			cout << endl;

		}

		else
			cout << "Case #" << i << ": " << line << endl;


	}


	return 0;
}