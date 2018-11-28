#include<fstream>
#include <string>
using namespace std;

int main()
{
	ifstream fin("in.txt");
	ofstream fout("out.txt");
	int T;
	fin >> T;
	for (int t = 0; t < T; t++)
	{
		string s;
		int k;
		fin >> s >> k;
		int cnt = 0;
		for (int i = 0; (i+k-1) < s.length(); i++) {
			if (s[i] == '-') {
				cnt++;
				for (int j = 0; j < k; j++) {
					s[i + j] = (s[i + j] == '-') ? '+' : '-';
				}
			}
		}

		bool good = true;
		for (char c : s) {
			if (c == '-')
				good = false;
		}
		if (!good)
			fout << "Case #" << t + 1 << ": " << "IMPOSSIBLE" << endl;
		else
			fout << "Case #" << t + 1 << ": " << cnt << endl;
	}
}