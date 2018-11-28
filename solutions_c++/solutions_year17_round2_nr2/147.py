#include <algorithm>
#include <iomanip>
#include <istream>
#include <map>
#include <numeric>
#include <ostream>
#include <set>
#include <sstream>
#include <string>
#include <utility>
#include <vector>
#include <random>
#include <complex>
#include <functional>
#include <cstdarg>
#include <cstdio>
#include <stack>
#include <limits>
#include <tuple>

using namespace std;
// Powered by caide (code generator, tester, and library code inliner)


class Solution {
public:
	const string IMP = "IMPOSSIBLE";

    void solve(std::istream& in, std::ostream& out) {
		int T; in >> T;
		for (int test = 1; test <= T; ++test) {
			int N, R, O, Y, G, B, V;
			in >> N >> R >> O >> Y >> G >> B >> V;
			N = R + O + Y + G + B + V;
			string s = solve(N, R, O, Y, G, B, V);
			
#define BAIL throw logic_error("...");
//#define BAIL s = IMP; goto go;

			if (s != IMP) {
				if ((int)s.size() != N)
					BAIL;
				vector<int> cnt { R, O, Y, G, B, V };
				map<char, int> idx{
					{ 'R', 0 },
					{ 'O', 1 },
					{ 'Y', 2 },
					{ 'G', 3 },
					{ 'B', 4 },
					{ 'V', 5 }
				};
				for (int i = 0; i < N; ++i) {
					if (s[i] == s[(i + 1) % N])
						BAIL;
					cnt[idx.at(s[i])]--;
				}
				for (int i : cnt)
					if (i != 0)
						BAIL;
			}

			go:
			out << "Case #" << test << ": " << s << "\n";
		}
    }

	string loop(const string& s, int n) {
		string res;
		while (n--)
			res += s;
		return res;
	}

	string solve(int N, int R, int O, int Y, int G, int B, int V) {
		if (G > 0 && R == G)
			return N == 2*R ? loop("RG", R) : IMP;
		if (O > 0 && B == O)
			return N == 2*B ? loop("BO", B) : IMP;
		if (V > 0 && Y == V)
			return N == 2 * Y ? loop("YV", Y) : IMP;
		if (R < G || B < O || Y < V)
			return IMP;

		bool haveG = G > 0, haveO = O>0, haveV = V>0;
		R -= G;
		B -= O;
		Y -= V;

		N = R + B + Y;
		if (2 * R > N || 2 * Y > N || 2 * B > N)
			return "IMPOSSIBLE";
		string s(N, '?');
		vector<int> cnt{ R, Y, B };
		string col = "RYB";
		int j = 0;
		if (cnt[1] > cnt[j])
			j = 1;
		if (cnt[2] > cnt[j])
			j = 2;
		for (int i = 0; i < N; ++i) {
			int k = (j + 1) % 3;
			if (cnt[k] > cnt[j])
				j = k;
			--cnt[j];
			s[i] = col[j];
			j = (j + 1) % 3;
		}

		if (s.front() == s.back()) {
			swap(s[0], s[1]);
			int i = 2;
			while (i < N && s[i] == s[i-1]) {
				swap(s[i], s[(i + 1) % N]);
				i += 2;
			}
		}

		string res;
		for (char c : s) {
			res.push_back(c);
			if (haveG && c == 'R') {
				haveG = false;
				res += loop("GR", G);
			}
			if (haveO && c == 'B') {
				haveO = false;
				res += loop("OB", O);
			}
			if (haveV && c == 'Y') {
				haveV = false;
				res += loop("VY", V);
			}
		}

		return res;
	}
};

void solve(std::istream& in, std::ostream& out)
{
    out << std::setprecision(12);
    Solution solution;
    solution.solve(in, out);
}


#include <fstream>
#include <iostream>


int main() {
    
    ios_base::sync_with_stdio(0);
    cin.tie(0);


    istream& in = cin;


    ostream& out = cout;

    solve(in, out);
    return 0;
}


#include <cstdlib>


