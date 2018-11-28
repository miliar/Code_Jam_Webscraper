#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <unordered_map>
#include <unordered_set>
#include <map>
#include <set>

using namespace std;

typedef long long ll; typedef unsigned long long ull; typedef vector<ll> vi; typedef pair<ll,ll> pi;
const int _1e5 = 100000; const int _1e7 = 10000000; const int _1e9 = 1000000000;

template<typename A, typename B> ostream& operator<<(ostream& str, const pair<A,B>& p) { str << "(" << p.first << ", " << p.second << ")"; return str; }
template<typename T> ostream& operator<<(ostream& str,             const vector<T>& v) { str << "["; for(auto n : v) str << n << ", "; str << "]"; return str; }
template<typename T> ostream& operator<<(ostream& str,             const set<T>& v) { str << "{"; for(auto n : v) { str << n << ", "; } str << "}"; return str; }
template<typename K, typename V> ostream& operator<<(ostream& str, const unordered_map<K, V>& v) { str << "{"; for(auto&& p : v) { str << p.first << " => " << p.second << ", "; } str << "}"; return str; }

#define debug(x) cout <<  #x  << ": " << x << endl


int main() {
	ios_base::sync_with_stdio(false);
	
	int n;
	cin >> n;

	for (int ncase=1; ncase<=n; ++ncase) {

		int r,c;
		cin >> r >> c;

		vector<vector<char>> grid(r, vector<char>(c));

		for (auto& row : grid) {
			for (auto& c : row) cin >> c;
		}

		for (int i=0; i<grid.size(); ++i) {
			// right
			for (int j=0; j<grid.at(0).size(); ++j) {
				char& c = grid.at(i).at(j);
				if (c == '?' && j > 0) {
					c = grid.at(i).at(j-1);
				}
			}

			// left
			for (int j=grid.at(0).size()-1; j --> 0;) {
				char& c = grid.at(i).at(j);
				if (c == '?') {
					c = grid.at(i).at(j+1);
				}
			}
		}


		// up
		for (int i=1; i<r; ++i) {
			if (grid.at(i).at(0) == '?') {
				for (int j=0; j<c; ++j) {
					grid.at(i).at(j) = grid.at(i-1).at(j);
				}
			}
		}

		// down
		for (int i=r-1; i --> 0;) {
			if (grid.at(i).at(0) == '?') {
				for (int j=0; j<c; ++j) {
					grid.at(i).at(j) = grid.at(i+1).at(j);
				}
			}
		}

		std::cout << "Case #" << ncase << ":\n";
		for (auto& row : grid) {
			for (auto& c : row) cout << c;
			cout << endl;
		}

	}
}
