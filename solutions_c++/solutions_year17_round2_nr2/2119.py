#include <fstream>
#ifdef ONLINE_JUDGE
#define cin in
#define cout out
#endif
#include <algorithm>
#include <iostream>
#include <cstdint>
#include <cstdio>
#include <cstring>
#include <set>
#include <string>
#include <map>
#define M_PI 3.14159265358979323846
#include <cmath>
#include <iomanip>
#include <vector>
#include <cstdlib>
#include <bitset>
#include <cfloat>
#include <queue>
#include <climits>
using namespace std;

const size_t MAX = 100 + 2;

uint64_t gcd(uint64_t a, uint64_t b)
{
	return b ? gcd(b, a%b) : a;
}

string capitalize(string str) {
	for (int32_t i = 0; i < str.length(); ++i)
		str[i] = toupper(str[i]);
	return str;
}

int main(int argc, char *argv[])
{
	ios_base::sync_with_stdio(false);
	ifstream in("input.txt");
	ofstream out("output.txt");
	int32_t tests, d, n, k, s;
	map<char, int32_t> pets;
	map<char, string> allowed = {
		{ 'r', "gyb" },
		{ 'o', "b" },
		{ 'y', "vrb" },
		{ 'g', "r" },
		{ 'b', "ory" },
		{ 'v', "y" },
	};
	string colors = "roygbv";
	cin >> tests;
	for (int32_t t = 1; t <= tests; ++t) {
		string ans = "";
		cin >> n >> pets['r'] >> pets['o']
			>> pets['y'] >> pets['g']
			>> pets['b'] >> pets['v'];
		int32_t lessByOne = 0;
		char start = 0;
		if (pets['g'] == 2 * pets['r'] - 1) {
			start = 'g';
			++lessByOne;
		}
		if (pets['o'] == 2 * pets['b'] - 1) {
			start = 'b';
			++lessByOne;
		}
		if (pets['v'] == 2 * pets['y'] - 1) {
			start = 'v';
			++lessByOne;
		}
		if (lessByOne > 1
			|| pets['g'] > 2 * pets['r']
			|| pets['o'] > 2 * pets['b']
			|| pets['v'] > 2 * pets['y']) goto ANSWER_SECTION;

		for (int32_t i = 0; i < colors.size() && start == 0; ++i)
			if (pets[colors[i]] != 0) start = colors[i];
		
		ans += start;
		--pets[start];
		char prev = start, curr;
		while (ans.length() < n) {
			if (prev == 'r' || prev == 'b' || prev == 'y') {
				char next = allowed[prev][0];
				if (pets[next] > 0) {
					ans += next;
					--pets[next];
					prev = next;
					continue;
				}
			}
			int32_t maximum = 0;
			for (auto &ch : allowed[prev]) {
				if (pets[ch] > maximum) {
					maximum = pets[ch];
					curr = ch;
				}
			}
			if (maximum == 0) break;
			ans += curr;
			--pets[curr];
			prev = curr;
		}
		char firstPet = ans[0], secondPet = ans[ans.length() - 1];
		bool ok = false;
		for (int32_t i = 0; i < allowed[firstPet].length() && !ok; ++i)
			if (allowed[firstPet][i] == secondPet) ok = true;
		if (!ok) ans = "";
	ANSWER_SECTION: 
		cout << "Case #" << t << ": ";
		if (ans.length() < n) cout << "IMPOSSIBLE" << endl;
					else cout << capitalize(ans) << endl;
	}
	return 0;
}