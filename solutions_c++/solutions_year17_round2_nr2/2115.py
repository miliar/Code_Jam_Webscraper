#include<iostream>
#include<algorithm>
#include<fstream>
#include<string>
#include<vector>
#include<queue>
using namespace std;

int test;
int n, r, o, y, g, b, v;

string process()
{
	string s = "";
	for (int i = 0; i < n; ++i)
		s.push_back('.');

	int pos = 0;

	bool f = (o + g + v <= 0);

	if (o > 0) {
		while (o > 0) {
			s[pos++] = 'B'; --b;
			s[pos++] = 'O'; --o;
		}
		if (pos < n) {
			s[pos++] = 'B'; --b;
			if (b < 0) return "IMPOSSIBLE";
		}
	}
	
	if (g > 0) {
		while (g > 0) {
			s[pos++] = 'R'; --r;
			s[pos++] = 'G'; --g;
		}
		if (pos < n) {
			s[pos++] = 'R'; --r;
			if (r < 0) return "IMPOSSIBLE";
		}
	}

	if (v > 0) {
		while (v > 0) {
			s[pos++] = 'Y'; --y;
			s[pos++] = 'V'; --v;
		}
		if (pos < n) {
			s[pos++] = 'Y'; --y;
			if (y < 0) return "IMPOSSIBLE";
		}
	}

	if (f)
	{
		int rem = n - pos;
		if (r >= y && r >= b && r > rem/2) return "IMPOSSIBLE";
		if (y >= r && y >= b && y > rem/2) return "IMPOSSIBLE";
		if (b >= y && b >= r && b > rem/2) return "IMPOSSIBLE";
	}

	while (pos < n) {
		if (pos == 0) {
			if (r >= y && r >= b) {
				s[pos++] = 'R'; --r;
			}
			else if (y >= r && y >= b) {
				s[pos++] = 'Y'; --y;
			}
			else if (b >= y && b >= r) {
				s[pos++] = 'B'; --b;
			}
		}
		else {
			if (s[pos - 1] == 'R') {
				if (y >= b) {
					s[pos++] = 'Y'; --y;
				}
				else {
					s[pos++] = 'B'; --b;
				}
			}
			else if (s[pos - 1] == 'Y') {
				if (r >= b) {
					s[pos++] = 'R'; --r;
				}
				else {
					s[pos++] = 'B'; --b;
				}
			}
			else if (s[pos - 1] == 'B') {
				if (r >= y) {
					s[pos++] = 'R'; --r;
				}
				else {
					s[pos++] = 'Y'; --y;
				}
			}
		}
	}

	if (r + y + b + o + g + v > 0) return "IMPOSSIBLE";

	if (s[n - 1] == s[0]) {
		char k = s[n - 2];
		s[n - 2] = s[n - 1];
		s[n - 1] = k;
	}

	for (int i = 1; i < n; ++i) {
		if (s[i] == s[i - 1]) return "IMPOSSIBLE";
	}
	if (s[n - 1] == s[0]) return "IMPOSSIBLE";

	return s;
}

int main()
{
	ifstream in("B-small-attempt0.in");
	//ifstream in("input.txt");
	ofstream out("output.txt");
	in >> test;
	for (int t = 1; t <= test; ++t)
	{
		in >> n >> r >> o >> y >> g >> b >> v;
		out << "Case #" << t << ": " << process() << endl;
		/*string s = process();
		if (s == "IMPOSSIBLE")
			out << "Case #" << t << ": " << s << endl;
		else
		{

		}*/
	}

	in.close();
	out.close();
	return 0;
}