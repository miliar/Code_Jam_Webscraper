#include <iostream>
#include <iomanip>
#include <cstdio>
#include <vector>
#include <queue>
#include <set>
#include <stack>
#include <string.h>
#include <algorithm>
#include <fstream>
#include <cassert>
#include <limits>
#include <numeric>
#include <map>
//#define NDEBUG
#ifdef NDEBUG
  #define DEBUG( x )
#else
  #define DEBUG( x )  x
#endif
using namespace std;
typedef long long int ll;
typedef long double ld;

class CaseSolver {
    public:
        void static precompute();
        void read(istream& is);
        void solve();
        void write(ostream& os);
    private:
        int n;
        vector<vector<char> > board;
        vector<vector<char> > original_board;
        void greedy_upgrade(int x, int y, std::string only);
        bool is_free_row_column(int x, int y);
        bool is_free_diagonal(int x, int y);
        bool legal_position(int x, int y);
        int model_score(int x, int y);
        int compute_score();
        vector<tuple<char, int, int> > compute_actions();
        void write_board(ostream& os);
};

void CaseSolver::precompute() {
}

int CaseSolver::model_score(int x, int y) {
    switch (board[x][y]) {
        case 'o':
            return 2;
        case '+':
            return 1;
        case 'x':
            return 1;
    }
    return 0;
}

int CaseSolver::compute_score() {
    int score = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            score += model_score(i, j);
        }
    }
    return score;
}

vector<tuple<char, int, int> > CaseSolver::compute_actions() {
    vector<tuple<char, int, int> > actions;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (original_board[i][j] != board[i][j]) {
                actions.push_back(make_tuple(board[i][j], i + 1, j + 1));
            }
        }
    }
    return actions;
}

void CaseSolver::read(istream& is) {
    int m;
    is >> n >> m;
    board = std::vector<std::vector<char> >(n, std::vector<char>(n, '.'));
    while (m--) {
        std::string s;
        int x, y;
        is >> s >> x >> y;
        board[x - 1][y - 1] = s[0];
    }
    original_board = board;
}

bool CaseSolver::is_free_row_column(int x, int y) {
    return !legal_position(x, y) || (board[x][y] == '+') || (board[x][y] == '.');
}

bool CaseSolver::is_free_diagonal(int x, int y) {
    return !legal_position(x, y) || (board[x][y] == 'x') || (board[x][y] == '.');
}

bool CaseSolver::legal_position(int x, int y) {
    return (0 <= x) && (x < n) && (0 <= y) && (y < n);
}

void CaseSolver::greedy_upgrade(int x, int y, string only) {
    bool empty_row_column = true;
    bool empty_diagonal = true;
    for (int i = -n; i <= n; ++i) {
        if (i == 0) {
            continue;
        }
        empty_row_column &= is_free_row_column(x, y + i);
        empty_row_column &= is_free_row_column(x + i, y);
        empty_diagonal &= is_free_diagonal(x + i, y + i);
        empty_diagonal &= is_free_diagonal(x + i, y - i);
    }
    char desired_state = '.';
    if (empty_row_column && empty_diagonal && only.find('o') != std::string::npos) {
        desired_state = 'o';
    } else if (empty_diagonal && only.find('+') != std::string::npos) {
        desired_state = '+';
    } else if (empty_row_column && only.find('x') != std::string::npos) {
        desired_state = 'x';
    }
    if (only.find(desired_state) != std::string::npos) {
        board[x][y] = desired_state;
    }
}

void CaseSolver::solve() {
    for (int i = 0; i < n; ++i) {
        greedy_upgrade(0, i, "o+");
    }
    for (int i = 0; i < n; ++i) {
        greedy_upgrade(n - 1, i, "o+");
    }

    for (int i = 0; i < n; ++i) {
        greedy_upgrade(i, 0, "o+x");
    }
    for (int i = 0; i < n; ++i) {
        greedy_upgrade(i, n-1, "o+x");
    }

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            greedy_upgrade(i, j, "x+o");
        }
    }
}

void CaseSolver::write_board(ostream& os) {
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            os << board[i][j];
        }
        os << "\n";
    }
}

void CaseSolver::write(ostream& os) {
    auto const actions = compute_actions();
    os << compute_score() << " " << actions.size() << "\n";
    for (auto action : actions) {
        os << std::get<0>(action) << " " << std::get<1>(action) << " " << std::get<2>(action) << "\n";
    }
    //write_board(os);
}


int main() {
    CaseSolver::precompute();
    int numberOfCases;
	cin >> numberOfCases;
	for(int testCase = 1; testCase <= numberOfCases; ++testCase) {
        CaseSolver caseSolver;
        caseSolver.read(cin);
        caseSolver.solve();
        cout << "Case #" << testCase << ": ";
        caseSolver.write(cout);
	}
}
