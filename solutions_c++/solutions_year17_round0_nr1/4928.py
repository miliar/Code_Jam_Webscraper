#include <iostream>
#include <fstream>
#include <string>
using namespace std;
int main()
{
	ifstream fin;
	ofstream fout;
	fin.open("A-large.in");
	fout.open("outlarge.txt");
	int t;
	fin >> t;
	for (int ti = 1; ti <= t; ti++)
	{
		string s;
		int k;
		fin >> s >> k;
		int len = s.length();
		int ans = 0;
		for (int i = 0; i <= len - k; i++) 
			if (s[i] == '-') {
				ans++;
				for (int j = 0; j < k; j++)
					s[i + j] = s[i + j] == '-' ? '+' : '-';
			}
		int ipsb = false;
		for (int i = 0; i < len; i++)
			if (s[i] == '-') {
				fout << "Case #" << ti << ": IMPOSSIBLE" << endl;
				ipsb = true;
				break;
			}
		if (!ipsb)
			fout << "Case #" << ti << ": " << ans << endl;
	}
}