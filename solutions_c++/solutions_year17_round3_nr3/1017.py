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

template <typename U>
double get_best(U& probs, double X) {
    std::priority_queue<double, vector<double>, std::greater<double>> pq;
    
    for (auto u : probs) {
	pq.push(u);
    }

    double front = 0.0;
    int equal_count = 1;
    while (true) {
	front = pq.top();
	pq.pop();

	double next = 1.0;
	while (!pq.empty()) {
	    next = pq.top();
	    if (next <= front) {
		equal_count += 1;
		pq.pop();
	    } else {
		break;
	    }
	}

	double diff = next - front;
	diff = std::min(diff, X / equal_count);
	front += diff;
	X -= diff * equal_count;
	pq.push(front);

	if (X < 1e-9) {
	    break;
	}
    }

    double total_prob = 1.0;

    auto worst = pq.top();
    for (int ix = 0; ix < equal_count; ++ix) {
	total_prob *= worst;
    }
    pq.pop();    

    while (!pq.empty()) {
	total_prob *= pq.top();
	pq.pop();
    }

    return total_prob;
}

template <typename U>
double get_best(U& probs, int64_t X) {
    // gradient descent
    std::priority_queue<int64_t, vector<int64_t>, std::greater<int64_t>> pq;
    
    for (auto u : probs) {
	pq.push(u);
    }

    auto do_simple = [&]() {
	auto top = pq.top();
	pq.pop();
	int64_t to_second = 10000;
	if (!pq.empty()) {
	    auto second = pq.top();
	    to_second = second - top;
	    to_second = std::min(to_second, X);
	    if (to_second == 0) {
		to_second += 1;
	    }
	    X -= to_second;
	    top += to_second;
	    pq.push(top);
	}
    };

    while (X > 0) {
	do_simple();
    }

    cout << ">>>>" << endl;
    double total_prob = 1;
    while (!pq.empty()) {
	auto top = pq.top();
	pq.pop();
	cout << "TOP=" << top << endl;
	total_prob *= top;
	total_prob /= 10000.0;
    }
    return total_prob;
}
int parse() {
    string s;
    cin >> s;
    
    string s2;
    for (auto x : s) {
	if (x != '.') {
	    s2 += x;
	}
    }
    return stoi(s2);
}

int main() {
  int64_t nTests;
  cin >> nTests;
  for (unsigned nTest = 0; nTest < nTests; nTest++) {
    cout << "Case #" << (nTest + 1) << ": ";
    /* =============== Put Solution Here ================= */
    int64_t N, K;
    cin >> N >> K;
    double U;
    cin >> U;
    //int64_t iU = parse();
    vector<double> probs;
    for (int64_t nx = 0; nx < N; ++nx) {
	//int64_t iP = parse();
	double P;
	cin >> P;
	probs.push_back(P);
    }

    auto bb = get_best(probs, U);

    printf("%.6f\n", bb);

    /* =================================================== */
  }
}
