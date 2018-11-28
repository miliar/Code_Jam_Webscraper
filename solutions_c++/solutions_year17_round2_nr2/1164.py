#include "stdafx.h"

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <stdio.h>
#include <iomanip>
using namespace std;
typedef long long ll;
int T;

std::string myreplace(std::string &s,
	const std::string &toReplace,
	const std::string &replaceWith)
{
	if (s.find(toReplace) == string::npos) {
		return s;
	}
	return(s.replace(s.find(toReplace), toReplace.length(), replaceWith));
}

int main()
{
	cin >> T;
	for (int testcase = 0; testcase < T; testcase++) {
		int N, R, O, Y, G, B, V;
		cin >> N >> R >> O >> Y >> G >> B >> V;

		if (R > N / 2 || Y > N / 2 || B > N / 2) {
			cout << "Case #" << testcase + 1 << ": " << "IMPOSSIBLE" << endl;
			continue;
		}

		if (R == 0) {
			string res = "";
			for (int i = 0; i < B; i++) {
				res += "BY";
			}
			cout << "Case #" << testcase + 1 << ": " << res << endl;
			continue;
		}
		if (B == 0) {
			string res = "";
			for (int i = 0; i < R; i++) {
				res += "RY";
			}
			cout << "Case #" << testcase + 1 << ": " << res << endl;
			continue;
		}
		if (Y == 0) {
			string res = "";
			for (int i = 0; i < B; i++) {
				res += "BR";
			}
			cout << "Case #" << testcase + 1 << ": " << res << endl;
			continue;
		}

		int maxSame = min(min(R, Y), B);
		string res = "A";
		for (int i = 0; i < maxSame; i++) {
			res += "RBY";
		}
		// RB, BY, YR, YA(=YR), AR(=YR)
		R -= maxSame;
		Y -= maxSame;
		B -= maxSame;

		if (B >= 1) {
			res = myreplace(res, "AR", "BR");
			B--;
		}
		res = myreplace(res, "A", "");

		while (R > 0 || B > 0 || Y > 0) {
			if (R > 0) {
				if (res.find("BY") != string::npos) {
					res = myreplace(res, "BY", "BRY");
					R--;
				} else if (res.find("YB") != string::npos) {
					res = myreplace(res, "YB", "YRB");
					R--;
				}
			}
			if (B > 0) {
				if (res.find("RY") != string::npos) {
					res = myreplace(res, "RY", "RBY");
					B--;
				}
				else if (res.find("YR") != string::npos) {
					res = myreplace(res, "YR", "YBR");
					B--;
				}
			}
			if (Y > 0) {
				if (res.find("RB") != string::npos) {
					res = myreplace(res, "RB", "RYB");
					Y--;
				}
				else if (res.find("BR") != string::npos) {
					res = myreplace(res, "BR", "BYR");
					Y--;
				}
			}
		}
		cout << fixed << setprecision(6) << "Case #" << testcase + 1 << ": " << res << endl;
	}
	return 0;
}

