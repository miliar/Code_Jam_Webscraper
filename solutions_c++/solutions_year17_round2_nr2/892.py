#include <iostream>
#include <string>
#include <algorithm>
#include <assert.h>

using namespace std;

string mfill(string r, int A, int B, char Ac, char Bc) {
	if (abs(A - B) > 1) {
		return "IMPOSSIBLE";
	}
	if (A >= B) {
		while (B > 0) {
			r += Ac;
			A--;
			r += Bc;
			B--;
		}
		if (A > 0) {
			r += Ac;
			A--;
		}
	}
	else {
		while (A > 0) {
			r += Bc;
			B--;
			r += Ac;
			A--;
		}
		if (B > 0) {
			r += Bc;
			B--;
		}
	}
	return r;
}

string mfill2(int A, int B, int C, char Ac, char Bc, char Cc) {
	if (A == 0) {
		return mfill("", B, C, Bc, Cc);
	}
	string res = "";
	while ((A > 1) && (B > C)) {
		res += Ac;
		A--;
		res += Bc;
		B--;
	}
	while (A > 1) {
		res += Ac;
		A--;
		res += Bc;
		B--;
		res += Cc;
		C--;
	}
	res += Ac;
	res = mfill(res, B, C, Bc, Cc);
	return res;
}

string solve(int R, int Y, int B)
{
	string res = "";
	int m = min(min(R, Y), B);
	if (m == R) {
		int m2 = min(Y, B);
		if (m2 == B) {
			res = mfill2(R, Y, B, 'R', 'Y', 'B');
		}
		else {
			res = mfill2(R, B, Y, 'R', 'B', 'Y');
		}
	}
	else if (m == B) {
		int m2 = min(Y, R);
		if (m2 == R) {
			res = mfill2(B, Y, R, 'B', 'Y', 'R');
		}
		else {
			res = mfill2(B, R, Y, 'B', 'R', 'Y');
		}
	}
	else if (m == Y) {
		int m2 = min(B, R);
		if (m2 == R) {
			res = mfill2(Y, B, R, 'Y', 'B', 'R');
		}
		else {
			res = mfill2(Y, R, B, 'Y', 'R', 'B');
		}
	}

	if (res[0] == res[res.size() - 1]) {
		return "IMPOSSIBLE";
	}
	return res;
}

string solve2(string res, int O, int G, int V) {
	string nres;
	for (int i = 0; i < res.size(); ++i) {
		nres += res[i];
		switch (res[i]) {			
		case 'R':
			for (int j = 0; j < G; ++j) {
				nres += "GR";
			}
			G = 0;
			break;
		case 'Y':
			for (int j = 0; j < V; ++j) {
				nres += "VY";
			}
			V = 0;
			break;
		case 'B':
			for (int j = 0; j < O; ++j) {
				nres += "OB";
			}
			O = 0;
			break;
		}
	}
	return nres;
}

int main() {
	int t, T;
	cin >> T;
	for (t = 0; t < T; ++t) {
		int N, R, Orange, Y, G, B, V;
		cin >> N >> R >> Orange >> Y >> G >> B >> V;
		cout << "Case #" << (t + 1) << ": ";

		
		if ((V > Y) || (G > R) || (Orange > B)) {
			cout << "IMPOSSIBLE" << endl;
			continue;
		}

		if (V > 0) {
			if ((V == Y) && ((V + Y) < N)) {
				cout << "IMPOSSIBLE" << endl;
				continue;
			}
			else if (V == Y) {
				cout << mfill("", V, Y, 'V', 'Y');
				cout << endl;
				continue;
			}
		}
		if (G > 0) {
			if ((G == R) && ((G + R) < N)) {
				cout << "IMPOSSIBLE" << endl;
				continue;
			}
			else if (G == R) {
				cout << mfill("", G, R, 'G', 'R');
				cout << endl;
				continue;
			}
		}
		if (Orange > 0) {
			if ((Orange == B) && ((Orange + B) < N)) {
				cout << "IMPOSSIBLE" << endl;
				continue;
			}
			else if (Orange == B) {
				cout << mfill("", Orange, B, 'O', 'B');
				cout << endl;
				continue;
			}
		}
		string res = solve(R - G, Y - V, B - Orange);
		if (res == "IMPOSSIBLE") {
			cout << "IMPOSSIBLE" << endl;
			continue;
		}
		res = solve2(res, Orange, G, V);
		cout << res << endl;

	}
	return 0;
}