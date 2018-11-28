#include <iostream>
#include <fstream>
#include <string>
#include <math.h>
#include <vector>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

#define ll long long

int main() {


	std::ifstream in("C:/Users/Yoav/Documents/Visual Studio 2015/Projects/20171b/20171b/B-small-attempt1.in");
	std::streambuf *cinbuf = std::cin.rdbuf(); //save old buf
	std::cin.rdbuf(in.rdbuf()); //redirect std::cin to in.txt!

	std::ofstream out("C:/Users/Yoav/Documents/Visual Studio 2015/Projects/20171b/20171b/B-small-attempt0.out");
	std::streambuf *coutbuf = std::cout.rdbuf(); //save old buf
	std::cout.rdbuf(out.rdbuf()); //redirect std::cout to out.txt!

	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		cout << "Case #" << t << ": ";
		int n, r, o, y, g, b, v;
		cin >> n >> r >> o >> y >> g >> b >> v;
		if (r + b < y || r + y < b || b + y < r)
			cout << "IMPOSSIBLE" << endl;
		else {
			char highest;
			char last_type = 'r';
			int m = max(r, y);
			m = max(m, b);
			if (r == m)
				last_type = 'y';
			char first = 'r';
			if (b >= r && b >= y) {
				first = 'b';
			}
			else if (y >= r && y >= b)
				first = 'y';
			string ans;

			int grade_r = 1, grade_b = 1, grade_y = 1;
			if (r > b)
				grade_r *= 2;
			else
				grade_b *= 2;
			if (b > y)
				grade_b *= 2;
			else grade_y *= 2;
			if (r > y)
				grade_r *= 2;
			else
				grade_y *= 2;

			while (r + b + y > 0) {
				if (last_type == 'y') {
					if (r > b || (r == b && grade_r > grade_b)) {
						ans += "R";
						r--;
						last_type = 'r';
					}
					else {
						ans += "B";
						b--;
						last_type = 'b';
					}
				}
				else if (last_type == 'r') {
					if (y > b || (y == b && grade_y > grade_b)) {
						ans += "Y";
						y--;
						last_type = 'y';
					}
					else {
						ans += "B";
						b--;
						last_type = 'b';
					}
				}
				else if (last_type == 'b') {
					if (y > r || (y == r && grade_y > grade_r)) {
						ans += "Y";
						y--;
						last_type = 'y';
					}
					else {
						ans += "R";
						r--;
						last_type = 'r';
					}
				}
			}
			if (ans[ans.length() - 1] == ans[0])
				cout << "now";
			cout << ans << endl;
		}
	}
	return 0;
}