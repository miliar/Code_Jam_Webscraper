#include <iostream>
#include <vector>
#include <set>
#include <functional>
#include <algorithm>
#include <map>
#include <cassert>
#include <queue>

using std::string;
using std::vector;
using std::set;
using std::map;
using std::pair;
using std::make_pair;
using std::tuple;
using std::make_tuple;
using std::queue;
using std::cin;
using std::cout;
using std::cerr;
using std::endl;

/* ================================================================ */
/* ================ Edges given as boolean sparse graph =========== */
/* ================================================================ */
bool bipartite_match(const vector<vector<bool>>& graph, int m, 
		     vector<bool>& seen, vector<int>& reverse) {
    const auto& edge_graph = graph.at(m);
    for (int n = 0; n < seen.size(); ++n) {
	if (edge_graph[n] && !seen[n]) {
	    seen[n] = true;
	    
	    if (reverse[n] < 0 || bipartite_match(graph, reverse[n], seen, reverse)) {
		reverse[n] = m;
		return true;
	    }
	}
    }
    return false;
}

/* ================================================================ */
/* ================ Edges given as dense (m,n) mapping ============ */
/* ================================================================ */

bool bipartite_match(const vector<vector<int>>& graph, int m,
		      vector<bool>& seen, vector<int>& reverse) {
    const auto& edge_graph = graph.at(m);
    for (auto n : edge_graph) {
	if (!seen[n]) {
	    seen[n] = true;

	    if (reverse[n] < 0 || bipartite_match(graph, reverse[n], seen, reverse)) {
		reverse[n] = m;
		return true;
	    }
	}
    }
    return false;
}

template <typename T>
std::pair<int, vector<int>> maximal_bipartite_matching(T& graph, int M, int N) {
    assert (graph.size() == M);
    
    vector<int> reverse(N, -1);

    int result = 0;
    for (int mx = 0; mx < M; ++mx) {
	vector<bool> seen(N, false);

	if (bipartite_match(graph, mx, seen, reverse)) {
	    ++result;
	}
    }
    
    return std::make_pair(result, reverse);
}

/* ======================================================== */
/* ======================================================== */
template <typename T, typename U, typename V>
bool recurse(T& grid, U& starts, V& used, int R, int C) {
    if (used.size() == starts.size()) {
	for (int rx = 0; rx < R; ++rx) {
	    for (int cx = 0; cx < C; ++cx) {
		if (grid[rx][cx] == '?') {
		    return false;
		}
	    }
	}
	return true;
    }

    for (auto& kv : starts) {
	if (used.count(kv.first) > 0) {
	    continue;
	}
	int row = kv.second.first;
	int col = kv.second.second;

	int right_col = col + 1;
	for (; right_col < C; ++right_col) {
	    if (grid[row][right_col] != '?') {
		break;
	    }
	    grid[row][right_col] = kv.first;
	}

	int left_col = col - 1;	
	for (; left_col >= 0; left_col--) {
	    if (grid[row][left_col] != '?') {
		break;
	    }
	    grid[row][left_col] = kv.first;
	}
	left_col++;
	
	int bottom_row = row + 1;
	for (; bottom_row < R; bottom_row++) {
	    bool cando = true;
	    for (int cx = left_col; cx < right_col; cx++) {
		if (grid[bottom_row][cx] != '?') {
		    cando = false;
		    break;
		}
	    }
	    
	    if (cando) {
		for (int cx = left_col; cx < right_col; ++cx) {
		    grid[bottom_row][cx] = kv.first;
		}
	    } else {
		break;
	    }
	}

	int top_row = row - 1;
	for (; top_row >= 0; top_row--) {
	    bool cando = true;
	    for (int cx = left_col; cx < right_col; cx++) {
		if (grid[top_row][cx] != '?') {
		    cando = false;
		    break;
		}
	    }
	    
	    if (cando) {
		for (int cx = left_col; cx < right_col; ++cx) {
		    grid[top_row][cx] = kv.first;
		}
	    } else {
		break;
	    }
	}
	top_row++;

	used.insert(kv.first);
	if (recurse(grid, starts, used, R, C)) {
	    return true;
	} else {
	    // unwind
	    for (int rx = top_row; rx < bottom_row; ++rx) {
		for (int cx = left_col; cx < right_col; ++cx) {
		    grid[rx][cx] = '?';
		}
	    }
	    grid[row][col] = kv.first;
	    used.erase(kv.first);
	}


    }
    return false;
}

int main() {
  int nTests;
  cin >> nTests;
  for (unsigned nTest = 0; nTest < nTests; nTest++) {
    cout << "Case #" << (nTest + 1) << ": ";
    /* =============== Put Solution Here ================= */
    int R, C;
    cin >> R >> C;
    vector<vector<char>> grid(R, vector<char>(C, '?'));
    std::map<char, pair<int, int>> starts;
    for (int rx = 0; rx < R; ++rx) {
	for (int cx = 0; cx < C; ++cx) {
	    char c;
	    cin >> c;
	    if (c != '?') {
		grid[rx][cx] = c;
		starts[c] = std::make_pair(rx, cx);
	    }
	}
    }

    std::set<char> used;
    bool success = recurse(grid, starts, used, R, C);
    assert (success);

    for (int rx = 0; rx < R; ++rx) {
	for (int cx = 0; cx < C; ++cx) {
	    assert (grid[rx][cx] != '?');
	}
    }

    cout << endl;

    for (const auto& row : grid) {
	for (auto& ch : row) {
	    cout << ch;
	}
	cout << endl;
    }

    /* =================================================== */
  }
}
