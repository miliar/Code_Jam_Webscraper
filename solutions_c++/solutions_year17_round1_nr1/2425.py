#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
using namespace std;
 
#define FORi(m) for( int i = 0; i < (m); ++i )
#define FOR(i, M) for( int i = 0; i < (M); ++i )
#define FOR1(i, M) for( int i = 1; i <= (M); ++i )
#define DEBUGGING 0
#define CERRL() if (DEBUGGING) { std::cerr << '\n'; }
#define EXAM(var) if (DEBUGGING) { std::cerr << #var << ": " << (var) << '\n'; }
#define EXAMARR(var) if (DEBUGGING) { std::cerr << #var << ": "; for (const auto& _var_: var) std::cerr << _var_ << " "; std::cerr << '\n'; }


class Node {
public:
	char ch;
	int r, c;
	Node(char ch, int r, int c): ch(ch), r(r), c(c) {}
};

class Case {
public:
	int R;
	int C;
	vector<vector<char>> cake;
	vector<Node> nodes;
	Case(int R, int C): R(R), C(C), cake(R) {}
	Case() {}
} CASE;

int next_up(int i) {
	for (int j = i - 1; j >= 0; j--) {
		if (CASE.nodes[j].r < CASE.nodes[i].r) {
			return CASE.nodes[i].r;
		}
	}
	return 0;
}

int next_left(int i) {
	int j = i - 1;
	if (j >= 0 && CASE.nodes[j].r == CASE.nodes[i].r) {
		return CASE.nodes[i].c;
	}
	return 0;
}

int next_down(int i) {
	for (int j = i + 1; j < CASE.nodes.size(); j++) {
		if (CASE.nodes[j].r > CASE.nodes[i].r) {
			return CASE.nodes[j].r;
		}
	}
	return CASE.R;
}

int next_right(int i) {
	int j = i + 1;
	if (j < CASE.nodes.size() && CASE.nodes[j].r == CASE.nodes[i].r) {
		return CASE.nodes[j].c;
	}
	return CASE.C;
}

void fill(char c, pair<int, int> from, pair<int, int> to) {
	for (int i = from.first; i < to.first; i++) {
		for (int j = from.second; j < to.second; j++) {
			CASE.cake[i][j] = c;
		}
	}
}

void solve() {
	pair<int, int> from = make_pair(0,0), to;
	int i = 0;
	for (int l = CASE.nodes.size(); i < l; i++) {
		from = make_pair(next_up(i), next_left(i));
		to = make_pair(next_down(i), next_right(i));
		EXAM(CASE.nodes[i].ch);
		EXAM(from.first);
		EXAM(from.second);
		EXAM(to.first);
		EXAM(to.second);
		fill(CASE.nodes[i].ch, from, to);
	}
}

int code(char c) {
	return c == '?'? -1 : c-'A';
}

char decode(int v) {
	return v == -1? '?' : v+'A';
}
 
int main() {
    int T;
    cin >> T;
    FOR1(t, T) {
        int R, C;
        cin >> R >> C;
        
		CASE = Case(R, C);
        
        FOR(r, R) {
        	FOR(c, C) {
        		char ch;
        		cin >> ch;
        		CASE.cake[r].push_back(ch);
        		if (ch != '?') {
        			CASE.nodes.push_back(Node(ch, r, c));
				}
				EXAM(ch);
			}
		}
        solve();
        cout << "Case #" << t << ":" << endl;
        for (auto r: CASE.cake) {
        	for (auto c: r) {
        		cout << c;
			}
			cout << endl;
		}
    }
}
