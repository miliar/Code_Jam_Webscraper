#define _CRT_SECURE_NO_DEPRECATE
#pragma comment(linker, "/STACK:167772160000")
#include <iostream>
#include <fstream>
#include <cstdio>
#include <stdio.h>
#include <cstdlib>
#include <stdlib.h>
#include <string>
#include <list>
#include <fstream>
#include <algorithm>
#include <cmath>
#include <map>
#include <vector>
#include <iomanip>
#include <queue>
#include <deque>
#include <set>
#include <stack>
#include <sstream>
#include <assert.h>
#include <functional>
#include <climits>
#include <cstring>
using namespace std;
typedef long long ll;
typedef pair<ll, ll> pll;
typedef pair<int, int> pii;
typedef pair<double, double> pdd;
//typedef uint64_t ull;
//typedef std::pair<long double,long double> pdd;
#define for8(i) for( i = 1; i<=8; i++)
#define fori(N)          for(int i = 0; i<(N); i++)
#define forj(N)         for(int j = 0; j<(N); j++)
#define fork(N)         for(int k = 0; k<(N); k++)
#define forl(N)         for(int l = 0; l<(N); l++)
#define ford(N)         for(int d = 0; d<(N); d++)
#define fori1(N)          for(int i = 1; i<=(N); i++)
#define forj1(N)         for(int j = 1; j<=(N); j++)
#define fork1(N)         for(int k = 1; k<=(N); k++)
#define ford1(N)         for(int d = 1; d<=(N); d++)
#define PI (2*asin(1))
#define print(n) printf("%d ", (n))
#define printll(n) printf("%I64d ", (n))
#define printline() printf("\n")
#define read(n) scanf("%d", &n);
#define read2(n, m) scanf("%d%d", &n, &m);
#define readll(n) scanf("%I64d", &n);
#define mp make_pair
template <typename T>
using min_heap = std::priority_queue<T, std::vector<T>, std::greater<T> >;
template <typename T>
using max_heap = std::priority_queue<T, std::vector<T>, std::less<T> >;

int n, r, o, y, g, b, v;
vector<string>B, R, Y;
string answer;
void toAns(vector<string> &a) {
	answer += a.back();
	a.pop_back();
}
string solve() {
	B.clear();
	R.clear();
	Y.clear();
	answer = "";
	if (b + o == n) {
		if (b != o) {
			return  "IMPOSSIBLE";
		}
		else {
			answer+= "BO";
			return answer;
		}
	}
	if (g + r == n) {
		if (g != r) {
			return  "IMPOSSIBLE";
		}
		else {
			fori(g)answer +=  "GR";
			return answer;
		}
	}
	if (v + y == n) {
		if (v != y) {
			return  "IMPOSSIBLE";
		}
		else {
			fori(v)answer += "VY";
			return answer;
		}
	}
	if ((o >= b && o>0) || (g >= r && g>0) || (v >= y && v>0)) {
		return  "IMPOSSIBLE";
	}
	
	if (o > 0) {
		string curString = "";
		curString += 'B';
		fori(o)curString += "OB";
		b -= (o + 1);
		B.push_back(curString);
	}

	if (g > 0) {
		string curString = "";
		curString += 'R';
		fori(g)curString += "GR";
		r -= (g + 1);
		R.push_back(curString);
	}
	if (v > 0) {
		string curString = "";
		curString += 'Y';
		fori(v)curString += "VY";
		y -= (v + 1);
		Y.push_back(curString);
	}
	fori(r)
		R.push_back("R");
	fori(b) {
		B.push_back("B");
	}
	fori(y) {
		Y.push_back("Y");
	}
	int sum = R.size() + B.size() + Y.size();
	if (R.size() > sum / 2 || B.size() > sum / 2 || Y.size() > sum / 2) {
		return  "IMPOSSIBLE";
	}
	char prev;
	if (!B.empty()) {
		answer += B.back();
		B.pop_back();
		prev = 'B';
	}
	else {
		answer += R.back();
		R.pop_back();
		prev = 'R';
	}
	
	sum--;
	fori(sum) {
		if (prev == 'B') {
			if (R.size() > Y.size()) {
				toAns(R);
				prev = 'R';
			}
			else {
				toAns(Y);
				prev = 'Y';
			}
		}
		else if (prev == 'R') {
			if (Y.size() > B.size()) {
				toAns(Y);
				prev = 'Y';
			}
			else {
				toAns(B);
				prev = 'B';
			}
		}
		else if (prev == 'Y') {
			if (R.size() > B.size()) {
				toAns(R);
				prev = 'R';
			}
			else {
				toAns(B);
				prev = 'B';
			}
		}
	}
	return answer;
}
int main()
{
#if defined(_DEBUG) || defined(_RELEASE)
#endif
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int cases; cin >> cases;
	for(int currentCase = 1;currentCase<=cases;currentCase++){
		cin >> n >> r >> o >> y >> g >> b >> v;
		cout << "Case #" << currentCase << ": ";

		cout << solve() << endl;

	}
	return 0;

}