#include <iostream>
#include <fstream>
#include <string>
using namespace std;
bool isAscend(string s)
{
	if (s.length() == 1)
		return true;
	for (int i = 0; i < s.length() - 1; i++)
		if (s[i] > s[i + 1])
			return false;
	return true;
}
int main()
{
	ifstream fin;
	ofstream fout;
	fin.open("B-large.in");
	fout.open("b-large-out.txt");
	int t;
	fin >> t;
	for (int ti = 1; ti <= t; ti++)
	{
		string n;
		fin >> n;
		while (!isAscend(n))
		{
			for (int i = 0; i < n.length() - 1; i++)
				if (n[i] > n[i + 1]) {
					n[i]--;
					for (int j = 1; j + i < n.length(); j++)
						n[i + j] = '9';
				}
		}
		fout << "Case #" << ti << ": " << stoll(n) << endl;
	}
}