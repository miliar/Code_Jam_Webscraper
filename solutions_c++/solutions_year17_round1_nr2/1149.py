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

template <typename T, typename U>
bool recurse(T& possibles, U& used, int row, int lbound, int rbound) {
    if (row == possibles.size()) {
	return true;
    }

    for (int col = 0; col < used[row].size(); ++col) {
	if (!used[row][col]) {
	    const auto& pos = possibles[row][col];
	    int inter_lbound = std::max(pos.first, lbound);
	    int inter_rbound = std::min(pos.second, rbound);
	    if (inter_lbound <= inter_rbound) {
		used[row][col] = true;
		if (recurse(possibles, used, row + 1, inter_lbound, inter_rbound)) {
		    return true;
		} else {
		    used[row][col] = false;
		    // keep trying a different path
		}
	    }
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
    int N, P;
    cin >> N >> P;

    vector<int> servings;
    for (int nx = 0; nx < N; ++nx) {
	int serving;
	cin >> serving;
	servings.push_back(serving);
    }

    vector<vector<pair<int, int>>> possibles;
    for (int nx = 0; nx < N; ++nx) {
	possibles.push_back(vector<pair<int, int>>());
	for (int px = 0; px < P; ++px) {
	    int package_size;
	    cin >> package_size;
	    double d_lower_bound = package_size / 1.1;
	    double d_upper_bound = package_size / 0.9;
	    int i_lower_bound = ((int)d_lower_bound / servings[nx]);
	    if (i_lower_bound * servings[nx] < d_lower_bound) {
		i_lower_bound++;
	    }
	    int i_upper_bound = (int)d_upper_bound / servings[nx];
	    
	    possibles[nx].push_back(make_pair(i_lower_bound, i_upper_bound));
	}
	std::sort(possibles[nx].begin(), possibles[nx].end(),
		  [](const auto& lhs, const auto& rhs) -> bool {
		      return lhs.second > rhs.second;
		  });
    }

//     for (int nx = 0; nx < N; ++nx) {
// 	for (int px = 0; px < P; ++px) {
// 	    std::cout << " (" << possibles[nx][px].first
// 		      << "," << possibles[nx][px].second
// 		      << ")";
// 		;
// 	}
// 	cout << endl;
//     }

    vector<vector<bool>> used(N, vector<bool>(P, false));

    int result = 0;
    for (int px = 0; px < N; ++px) {
	auto x = possibles[0][px];
	while (recurse(possibles, used, 0, 0, std::numeric_limits<int>::max())) {
	    result++;
	}
    }

    cout << result << endl;
    /* =================================================== */
  }
}
