#define _CRT_SECURE_NO_DEPRECATE
#include<iostream>
#include<string>
#include<sstream>
#include<vector>
#include<deque>
#include<queue>
#include<stack>
#include<numeric>
#include<math.h>
#include<set>
#include<map>
#include<fstream>
#define epsilon 0.000000001
#define cosinusa(a, b, c) ((a * a + b * b - c * c) / (2.0 * a * b));
#define infi 1000000000
using namespace std;

string solve(int r, int y, int b, char left, char right) {
	if (r < 0 || y < 0 || b < 0) return "";
	bool canr = true;
	bool cany = true;
	bool canb = true;
	int targety = (right == 'Y');
	int targetb = (right == 'B');
	int targetr = (right == 'R');
	if (r == 0 && left == 'R') return "";
	if (b == 0 && left == 'B') return "";
	if (y == 0 && left == 'Y') return "";
	string res;

	switch (left) {
	case 'R': r--; res = "R"; canr = false; break;
	case 'Y': y--; res = "Y"; cany = false; break;
	case 'B': b--; res = "B"; canb = false; break;
	}
	int n = r + y + b;
	if (n == 0) return res;
	if (r == 0 && right == 'R') return "";
	if (b == 0 && right == 'B') return "";
	if (y == 0 && right == 'Y') return "";

	for (int i = 0; i < n - 1; i++) {
		if (canr && (r >= y || !cany) && (r >= b || !canb) && r > targetr) {
			res += "R";
			r--;
			canr = false;
			cany = canb = true;
			continue;
		}
		if (cany && (y >= r || !canr) && (y >= b  || !canb) && y > targety) {
			res += "Y";
			y--;
			cany = false;
			canr = canb = true;
			continue;
		}
		if (canb && (b >= y || !cany) && (b >= r  || !canr) && b > targetb) {
			res += "B";
			b--;
			canb = false;
			canr = cany = true;
			continue;
		}
		return "";
	}
	if (right == 'B' && !canb) return "";
	if (right == 'Y' && !cany) return "";
	if (right == 'R' && !canr) return "";
	res += right;
	return res;
}
string composeSolution(string solution, int pseudob, int pseudoy, int pseudor) {
	string sol = "";
	for (int i = 0; i < solution.size(); i++) {
		if (solution[i] == 'B') {
			if (pseudob > 0) {
				sol += "BOB";
				pseudob--;
			} else {
				sol += "B";
			}
		}
		if (solution[i] == 'Y') {
			if (pseudoy > 0) {
				sol += "YVY";
				pseudoy--;
			} else {
				sol += "Y";
			}
		}
		if (solution[i] == 'R') {
			if (pseudor > 0) {
				sol += "RGR";
				pseudor--;
			} else {
				sol += "R";
			}
		}
	}
	return sol;
}

int main()
{
	freopen("google.in", "r", stdin);
	freopen("google.out", "w", stdout);
	int numTests;
	cin >> numTests;
	for(int testCounter = 0; testCounter < numTests; ++testCounter)
	{
		printf("Case #%d: ", testCounter + 1);
		int n, r, o, y, g, b, v;
		cin >>  n >> r >> o >> y >> g >> b >> v;
		int pseudor, pseudob, pseudoy;
		string no = "IMPOSSIBLE";
		char combinations[3][2] = {{'R', 'B'}, {'R', 'Y'}, {'Y', 'B'}};
		bool solved = false;
		for (int i = 0; i < 3 && !solved; i++)	{
			if (r < 2 * g || y < 2 * v || b < 2 * o) continue;
			string solution = solve(r - g, y - v, b - o, combinations[i][0], combinations[i][1]);
			if (solution.size() == 0) {
				continue;
			}
			string sol = composeSolution(solution, o, v, g);
			cout << sol << endl;
			solved = true;
		}
		char secondCombinations[3][2] = {{'R', 'R'}, {'Y', 'Y'}, {'B', 'B'}};
		char lastLetter[] = "GVO";
		int additions[3][3] = {{1,0,0},{0,1,0},{0,0,1}};
		for (int i = 0; i < 3 && !solved; i++)	{
			if (i == 0 && g == 0)continue;
			if (i == 1 && v == 0)continue;
			if (i == 2 && o == 0)continue;
			if (r < 2 * (g - additions[i][0])) continue;
			if (y < 2 * (v - additions[i][1])) continue;
			if (b < 2 * (o - additions[i][2])) continue;
			string solution = solve(r - g + additions[i][0], y - v + additions[i][1], b - o  + additions[i][2], secondCombinations[i][0], secondCombinations[i][1]);
			if (solution.size() == 0) {
				continue;
			}
			string sol = composeSolution(solution, o - additions[i][2], v - additions[i][1], g  - additions[i][0]);
			sol += lastLetter[i];
			cout << sol << endl;
			solved = true;
		}
		if (!solved) {
			cout << no << endl;
		}
		
	}
	return 0;
}


