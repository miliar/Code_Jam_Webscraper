// ConsoleApplication1.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <fstream>
#include <cstdlib>
#include <string>

#define rep(i, a, b) for (int i=a;i<b;i++)

using namespace std;

int main()
{
	ifstream reader("input.txt");
	ofstream writer("output.txt");
	int T;
	reader >> T;
	rep(i, 0, T) {
		string str;
		int len;
		int ans = 0;
		reader >> str >> len;
		rep(j, 0, str.size() - len + 1)
		{
			if (str[j] == '-') {
				ans++;
				rep(k, j, j + len)
					str[k] = (str[k] == '-') ? '+' : '-';
			}
		}
		bool flag = true;
		rep(j, 0, str.size())
		{
			if (str[j] == '-') flag = false;
		}
		if (flag) writer << "Case #" << i + 1 << ": "  << ans << endl;
		else writer << "Case #" << i + 1 << ": " << "IMPOSSIBLE" << endl;
	}

	system("pause");
    return 0;
}

