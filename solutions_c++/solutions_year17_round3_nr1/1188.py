#include <iostream>
#include <vector>
#include <set>
#include <functional>
#include <algorithm>
#include <map>
#include <cassert>
#include <queue>
#include <math.h>

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

// without pi
int64_t surface(int64_t R, int64_t H) {
    return R*R + 2*R*H;
}

template <typename U>
int64_t get_rest(U& pancakes, int64_t index, int64_t base_radius, int64_t remaining) {
    if (remaining == 0) {
	return 0;
    }

    vector<pair<int64_t, int64_t>> rest_of_pancakes;
    for (int ix = 0; ix < pancakes.size(); ++ix) {
	if (ix != index) {
	    // doable
	    if (pancakes[ix].first <= base_radius) {
		rest_of_pancakes.push_back(pancakes[ix]);
	    }
	}
    }

    if (rest_of_pancakes.size() < remaining) {
	return -1;
    }
    
    std::sort(rest_of_pancakes.begin(), rest_of_pancakes.end(),
	      [](const auto& lhs, const auto& rhs) {
		  return (lhs.first * lhs.second) > (rhs.first * rhs.second);
	      });

    int64_t rest = 0;
    for (int nx = 0; nx < remaining; ++nx) {
	rest += rest_of_pancakes[nx].first * rest_of_pancakes[nx].second;
    }
    return rest;
}
   
int main() {
  int nTests;
  cin >> nTests;
  for (unsigned nTest = 0; nTest < nTests; nTest++) {
    cout << "Case #" << (nTest + 1) << ": ";
    /* =============== Put Solution Here ================= */
    int64_t K, N;
    cin >> N >> K;
    vector<pair<int64_t, int64_t>> pancakes;
    for (int nx = 0; nx < N; ++nx) {
	int64_t R, H;
	cin >> R >> H;
	pancakes.push_back(make_pair(R, H));
    }
    
    std::sort(pancakes.begin(), pancakes.end(), [](const auto& lhs, const auto& rhs) {
	    return surface(lhs.first, lhs.second) > surface(rhs.first, rhs.second);
	});

    // Final surface is pi times (R_0)^2 + 2*sum of H_i, R_i of those chosen
    // order doesn't matter, we can always turn it around

    int64_t largest = -1;
    for (int ix = 0; ix < pancakes.size(); ++ix) {
	auto base = pancakes[ix];
	auto rest = get_rest(pancakes, ix, base.first, K-1);
	if (rest == -1) {
	    // not possible to use base
	} else {
	    int64_t total = surface(base.first, base.second) + 2*rest;
	    if (total > largest) {
		largest = total;
	    }
	}
    } 

    assert (largest != -1);

    printf("%.9f\n", M_PI * largest);

    /* =================================================== */
  }
}
