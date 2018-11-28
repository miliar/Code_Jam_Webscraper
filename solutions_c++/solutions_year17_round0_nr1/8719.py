#include <iostream>
#include <string>
#include <map>
#include <queue>

using namespace std;

bool substr_eq(string str, char ch)
{
	bool all_eq = true;
	for (auto s : str) {
		if (s != ch) {
			all_eq = false;
			break;
		}
	}
	return all_eq;
}

string flip_substr(string state, int pos, int K)
{
	for (int i = pos; i < pos + K && i < state.length(); i++) {
		if (state[i] == '+')
			state[i] = '-';
		else if (state[i] == '-')
			state[i] = '+';
	}
	return state;
}

/*
int flip(string state, int pos, int K)
{
	
	return -1;
}

int count_flips(string state, int K)
{
	visited_states.clear();
	for (int pos = 0; pos < state.length() - K; pos++) {
		if (substr_eq(state.substr(pos, K), '+'))
			continue;
		int nflips = flip(state, pos, K);
		if (nflips >= 0)
			return nflips;
	}
	return -1;
}
*/

int dist(string state)
{
// count the number of minuses
	int count = 0;
	for (auto s : state) {
		if (s == '-')
			count++;
	}
	return count;
}

struct node {
	int est_dist;
	int curr_dist;
	string state;
	node(int est_dist, int curr_dist, string state) : est_dist(est_dist), curr_dist(curr_dist), state(state) {}
};

int count_flips(string state, int K)
{
	map<string, int> visited_states;
	auto cmp = [](node left, node right) { return left.est_dist > right.est_dist;  };
	priority_queue<node, vector<node>, decltype(cmp)> pq(cmp);

	int best_count = -1;

	// BFS with priority queue
	pq.push(node(dist(state), 0, state));

	while (!pq.empty()) {
		auto curr_node = pq.top();
		pq.pop();
		string curr_state = curr_node.state;
		int curr_dist = curr_node.curr_dist;
		//cout << curr_state << " " << curr_dist << endl;

		if (substr_eq(curr_state, '+')) {
			best_count = curr_dist;
			break;
		}

		// if current state was already visited then skip
		if (visited_states.find(curr_state) != visited_states.end())
			continue;

		visited_states.insert(pair<string, int>(curr_state, curr_dist));
		for (int pos = 0; pos <= state.length() - K; pos++) {
			auto new_state = flip_substr(curr_state, pos, K);
			int new_dist = curr_dist + 1;
			pq.push(node(new_dist, new_dist, new_state));
		}
	}
	return best_count;
}

int main(int argc, char ** argv)
{
	int T;
	string input;
	int K;
	cin >> T;
	for (int caseNo = 1; caseNo <= T; caseNo++) {
		cin >> input >> K;
//		cout << input << K << endl;
		//cout << substr_eq(input.substr(0, K), '+') << endl;
		//cout << flip_substr(input, 0, K) << endl;
		//cout << dist(input) << endl;
		cout << "Case #" << caseNo << ": ";
		int nFlips = count_flips(input, K);
		
		if (nFlips < 0) cout << "IMPOSSIBLE";
		else cout << nFlips;
		cout << endl;
	}
	return 0;
}
