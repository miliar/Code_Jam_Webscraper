#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
	int t;
	cin >> t;
	// cout << "starting loop";
	for (int c = 1; c <= t; ++c) {
		cout << "Case #" << c << ": ";
		string s;
		int k;
		cin >> s;
		cin >> k;
		vector<bool> flips(s.size());
		// cout << "string len" << s.size() << endl;
		for (int i = 0; i < s.size(); ++i)
		{
			flips[i] = s[i] == '+';
		}
		try {
			int count = 0;
			for (int i = 0; i < s.size(); ++i)
			{
				// cout << "finding solution";
				if (!flips[i])
				{
					++count;
					for (int j = i; j < i+k; ++j)
					{
						// cout <<"idx: "<< j<<endl;
						flips[j] = !flips.at(j);
					}
				}
			}
			cout << count;
		}
		catch (...) {
			cout << "IMPOSSIBLE";
		}
		cout << endl;
	}
	return 0;
}