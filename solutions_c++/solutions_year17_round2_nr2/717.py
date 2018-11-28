#include <iostream>
using namespace std;

// x >= y, z
string build(char a, char b, char c, int x, int y, int z) {
	//cerr << a << "," << b << "," << c << " ";
	//cerr << x << "," << y << "," << z << endl;
	if (x < 0 || y < 0 || z < 0) {
		//cerr << "IMPOSSIBLE" << endl;;
		return "IMPOSSIBLE";
	}
	if (x > y + z) {
		//cerr << "IMPOSSIBLE" << endl;;
		return "IMPOSSIBLE";
	}
	string ret = "";
	for (int i = 0; i < x; i++) {
		ret += a;
		if (i < y) {
			ret += b;
		}
		if ((x - i - 1) < z) {
			ret += c;
		}
	}
	return ret;
}

int main() {
	int T; cin >> T;
	for (int No = 1; No <= T; No++) {
		int N, R, O, Y, G, B, V; cin >> N >> R >> O >> Y >> G >> B >> V;
		int r = R - G;
		int y = Y - V;
		int b = B - O;
		string ans;
		if (r >= y && r >= b) {
			ans = build('R', 'Y', 'B', r, y, b);
		} else if (y >= r && y >= b) {
			ans = build('Y', 'R', 'B', y, r, b);
		} else {
			ans = build('B', 'R', 'Y', b, r, y);
		}
		if (ans != "IMPOSSIBLE") {
			while (O--) {
				string::size_type p = ans.find("B");
				ans.insert(p == string::npos ? 0 : p, "BO");
			}
			while (G--) {
				string::size_type p = ans.find("R");
				ans.insert(p == string::npos ? 0 : p, "RG");
			}
			while (V--) {
				string::size_type p = ans.find("Y");
				ans.insert(p == string::npos ? 0 : p, "YV");
			}
		}
		if (ans.length() != N && ans != "IMPOSSIBLE") {
			//cerr << "WARNING!" << " " << ans << endl;
		}
		cout << "Case #" << No << ": " << ans << endl;
	}
	return 0;
}
