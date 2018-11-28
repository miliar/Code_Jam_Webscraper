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

int main() {
  int nTests;
  cin >> nTests;
  for (unsigned nTest = 0; nTest < nTests; nTest++) {
    cout << "Case #" << (nTest + 1) << ": ";
    /* =============== Put Solution Here ================= */
    int D, N;
    cin >> D >> N;
    vector<pair<int, int>> horses;
    for (int nx = 0; nx < N; ++nx) {
	int K, S;
	cin >> K >> S;
	horses.push_back(make_pair(K, S));
    }

    std::sort(horses.begin(), horses.end(), [](const auto& lhs, const auto& rhs) {
	   return lhs.first > rhs.first;
	});

    double max_speed = std::numeric_limits<double>::max();
    for (auto horse : horses) {
	if (horse.first < D) {
	    double hours = (D - horse.first) / (double)horse.second;
	    double i_max_speed = ((horse.first) / hours) + horse.second;
	    max_speed = std::min(max_speed, i_max_speed);
	}
    }

    
    printf("%.6f\n", max_speed);
    /* =================================================== */
  }
}
