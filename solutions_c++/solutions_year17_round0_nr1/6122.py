/// A_oversizedPancake

#include <cstdio>
#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int main()
{
	int t;	cin >> t;
	ofstream fout;
	fout.open("output.txt");

	for (int testCase = 1; testCase <= t; testCase++) {
		string s;
		int k, sLen, ans = 0;
		bool pi[1004];
		cin >> s;
		cin >> k;

		sLen = s.length();
		for (int i = 0; i < sLen; i++) {
			if (s[i] == '-')
				pi[i] = true;
			else
				pi[i] = false;
		}

		for (int i = 0; i <= sLen - k; i++) {
			if (pi[i]) {
				for (int j = i; j < i + k; j++)
					pi[j] = !pi[j];
				ans++;
			}			
		}

		bool imp = false;
		for (int i = sLen - k; i < sLen; i++) {
			if (pi[i])
				imp = true;
		}

		if (!imp) {
			cout << "Case #" << testCase << ": " << ans << endl;
			fout << "Case #" << testCase << ": " << ans << endl;
		}
		else {
			cout << "Case #" << testCase << ": IMPOSSIBLE" << endl;
			fout << "Case #" << testCase << ": IMPOSSIBLE" << endl;
		}
	}
}