#include <bits/stdc++.h>

#define all(x) (x).begin(), (x).end()
#define itn int

using namespace std;

inline int nxt() {
	int x;
	cin >> x;
	return x;
}

void sleep(double secs) {
	clock_t start = clock();
	while (clock() < start + secs * CLOCKS_PER_SEC) {
		//
	}
}

class Semaphore {
public:
	explicit Semaphore(int free_count = 0): free_count_(free_count) {}

	void notify() {
		unique_lock<mutex> lock(mutex_);
		++free_count_;
		cv_.notify_one();
	}

	void wait() {
		unique_lock<mutex> lock(mutex_);
		while (!free_count_) {
			cv_.wait(lock);
		}
		--free_count_;
	}

private:
	mutex mutex_;
	condition_variable cv_;
	size_t free_count_;
};

template <typename InputData, typename OutputData>
OutputData solve(InputData inputData);

template <typename InputData, typename OutputData>
class ParallelTaskRunner {
public:
	explicit ParallelTaskRunner(int num_threads = 4,
								int history_limit = 10,
								int progressbar_length = 100):
			history_limit_(history_limit),
			progressbar_length_(progressbar_length),
			sem(num_threads) {}

	void readData() {
		int testCount = nxt();

		inputs.resize(testCount);
		for (itn i = 0; i < testCount; ++i) {
			cin >> inputs[i];
		}
	}

	void run() {
		int testCount = inputs.size();
		vector<char> states(testCount);

		future<void> shower = async(show, history_limit_, progressbar_length_,
									testCount, states.data());

		states.resize(testCount);
		futures.resize(testCount);
		for (itn i = 0; i < testCount; ++i) {
			futures[i] = async(launch::async, solveData, ref(sem), ref(states[i]), inputs[i]);
		}

		outputs.resize(testCount);
		for (int i = 0; i < testCount; ++i) {
			outputs[i] = futures[i].get();
		}

		shower.wait();
	}

	void print(ostream& ostr = cout) {
		int testCount = outputs.size();
		for (int i = 0; i < testCount; ++i) {
			ostr << "Case #" << i + 1 << ": " << outputs[i] << "\n";
		}
	}

private:
	static OutputData solveData(Semaphore& sem,
								volatile char& state,
								InputData input) {
		sem.wait();
		state = 1;
		auto result = solve(input);
		state = 2;
		sem.notify();
		return result;
	}

	static void show(int history_limit, int progressbar_length,
					 int testCount, char* states) {
		deque<int> history(history_limit, -1);
		for (int i = 0; i < history_limit + 2; ++i) {
			cerr << "\n";
		}
		int finishedCount = 0;
		vector<char> old_states(testCount, 0);
		size_t animation = 0;
		while (finishedCount != testCount) {
			for (int i = 0; i < testCount; ++i) {
				if (states[i] != old_states[i]) {
					old_states[i] = states[i];
					if (states[i] == 2) {
						++finishedCount;
						history.push_back(i);
						history.pop_front();
					}
				}
			}

			for (int i = 0; i < history_limit + 2; ++i) {
				cerr << "\e[A";
			}
			for (int i = 0; i < history_limit; ++i) {
				if (history[i] == -1) {
					cerr << string((animation + i) % 10, ' ') << "..." << string(10 - (animation + i) % 10, ' ') << "\n";
				} else {
					cerr << "Testcase #" << history[i] + 1 << " is done   \n";
				}
			}
			cerr << "Finished in total: " << finishedCount << " of " << testCount << "\n";

			cerr << "[";
			for (int i = 0; i < progressbar_length; ++i) {
				int l = i * testCount / progressbar_length;
				int r = (i + 1) * testCount / progressbar_length;
				if (r == l) {
					r = l + 1;
				}
				int counts[3] = {0, 0, 0};
				for (int j = l; j < r; ++j) {
					counts[states[j]] += 1;
				}
				int argmax = max_element(counts, counts + 3) - counts;
				if (argmax == 0) {
					cerr << " ";
				} else if (argmax == 1) {
					// cerr << ".";
					cerr << ".oO*"[animation / 10 % 4];
				} else {
					cerr << "\e[32m#\e[0m";
				}
			}
			cerr << "]\n";

			sleep(0.1);
			animation += 1;
		}
	}

	vector<InputData> inputs;
	vector<OutputData> outputs;
	vector<future<OutputData>> futures;
	Semaphore sem;
	int history_limit_;
	int progressbar_length_;
};

// ===== Essential part is here =====

// using InputData = long long;

struct InputData {
	vector<vector<int>> a;
};

struct OutputData {
	int pts;
	vector<pair<pair<int, int>, char>> chgs;
};

istream& operator >>(istream& istr, InputData& inputData) {
	int n, m;
	istr >> n >> m;
	inputData.a.resize(n, vector<int>(n, 0));
	for (int i = 0; i < m; ++i) {
		int x, y;
		char c;
		istr >> c >> x >> y;
		--x, --y;
		if (c == '.') {
			inputData.a[x][y] = 0;
		} else if (c == '+') {
			inputData.a[x][y] = 1;
		} else if (c == 'x') {
			inputData.a[x][y] = 2;
		} else {
			inputData.a[x][y] = 3;
		}
	}
	return istr;
}

ostream& operator <<(ostream& ostr, const OutputData& outputData) {
	ostr << outputData.pts << " " << outputData.chgs.size();
	for (auto p : outputData.chgs) {
		ostr << "\n" << p.second << " " << p.first.first + 1 << " " << p.first.second + 1;
	}
	return ostr;
}

struct Network {

	struct Edge {
		int from, to, cap, flow;

		Edge(int fr, int to, int cap, int fl = 0):
			from(fr),to(to),cap(cap),flow(fl){}
	};

	int n;
	int s, t;
	vector<Edge> edges;
	vector<vector<int>> a;
	vector<int> ptr;

	Network(int n, int s, int t): n(n), s(s), t(t) {
		a.resize(n);
		ptr.resize(n);
	}

	void add_edge(int from, int to, int cap) {
		int num = edges.size();
		edges.push_back(Edge(from, to, cap));
		edges.push_back(Edge(to, from, 0));
		a[from].push_back(num);
		a[to].push_back(num + 1);
	}

	int push(int v, int limit) {
		if (v == t)
			return limit;
		if (limit == 0)
			return 0;
		int res = 0;
		while (ptr[v] < a[v].size() && limit){
			int pos = a[v][ptr[v]];
			int to = edges[pos].to;
			int lm = min(limit, edges[pos].cap - edges[pos].flow);
			ptr[v]++;
			int flow = push(to, lm);
			limit -= flow;
			res += flow;
			edges[pos].flow += flow;
			edges[pos ^ 1].flow -= flow;
		}
		return res;
	}

	int get_flow() {
		int res = 0;
		while (true){
			for (int i = 0; i < n; i++)
				ptr[i] = 0;
			int flow = push(s, INT_MAX / 10);
			if (flow == 0)
				break;
			res += flow;
		}
		return res;
	}

	void show_flow() const {
		vector<vector<int>> out(n);
		for (int i = 0; i < edges.size(); i += 2){
			if (edges[i].flow == 0)
				continue;
			int j = i;
			if (edges[i].flow < 0)
				j++;
			out[edges[j].from].push_back(j);
		}
		for (int i = 0; i < n; i++){
			for (int j : out[i]){
				cerr << i << " -> " << edges[j].to << " (" << edges[j].flow << "/" << edges[j].cap << ")\n";
			}
		}
	}
};

vector<int> find_matching(vector<vector<int>> a, int n, int m) {
	Network network(n + m + 2, 0, n + m + 1);
	for (int i = 0; i < n; i++)
		network.add_edge(0, i + 1, 1);
	for (int i = 0; i < m; i++)
		network.add_edge(i + n + 1, n + m + 1, 1);
	for (int i = 0; i < n; i++){
		for (int j : a[i]){
			network.add_edge(i + 1, j + n + 1, 1);
		}
	}

	int sz = network.get_flow();
	vector<int> res(n);
	for (int i = 0; i < n; i++){
		int j = 0;
		while (j < network.a[i + 1].size() && network.edges[network.a[i + 1][j]].flow < 1)
			j++;
		if (j == network.a[i + 1].size())
			res[i] = -1;
		else
			res[i] = network.edges[network.a[i + 1][j]].to - n - 1;
	}

	// network.show_flow();

	return res;
}

OutputData solve(InputData inputData) {
	int n = inputData.a.size();
	auto a = inputData.a;
	vector<int> rows, cols;
	vector<char> row_ok(n, 1), col_ok(n, 1);
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < n; ++j) {
			if (a[i][j] & 2) {
				row_ok[i] = false;
				col_ok[j] = false;
			}
		}
	}
	for (int i = 0; i < n; ++i) {
		if (row_ok[i]) {
			rows.push_back(i);
		}
		if (col_ok[i]) {
			cols.push_back(i);
		}
	}
	int sz = min(rows.size(), cols.size());
	for (int i = 0; i < sz; ++i) {
		a[rows[i]][cols[i]] |= 2;
	}

	vector<char> diag_p_ok(n + n - 1, 1), diag_n_ok(n + n - 1, 1);
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < n; ++j) {
			if (a[i][j] & 1) {
				diag_p_ok[i + j] = false;
				diag_n_ok[i - j + n - 1] = false;
			}
		}
	}
	vector<int> diag_p, diag_n;
	for (int i = 0; i < n + n - 1; ++i) {
		if (diag_p_ok[i]) {
			diag_p.push_back(i);
		}
		if (diag_n_ok[i]) {
			diag_n.push_back(i);
		}
	}

	vector<vector<int>> edges(diag_p.size());
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < n; ++j) {
			if ((!(a[i][j] & 1)) && diag_p_ok[i + j] && diag_n_ok[i - j + n - 1]) {
				int index1 = lower_bound(all(diag_p), i + j) - diag_p.begin();
				int index2 = lower_bound(all(diag_n), i - j + n - 1) - diag_n.begin();
				edges[index1].push_back(index2);
			}
		}
	}
	auto matching = find_matching(edges, diag_p.size(), diag_n.size());
	for (int i = 0; i < (int)diag_p.size(); ++i) {
		if (matching[i] != -1) {
			int sum = diag_p[i];
			int dif = diag_n[matching[i]] - n + 1;
			int x = (sum + dif) / 2;
			int y = (sum - dif) / 2;
			a[x][y] |= 1;
		}
	}

	vector<pair<pair<int, int>, char>> ans;
	int pts = 0;
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < n; ++j) {
			if (a[i][j] != inputData.a[i][j]) {
				ans.push_back({{i, j}, a[i][j][".+xo"]});
			}
			pts += __builtin_popcount(a[i][j]);
		}
	}

	return {pts, ans};
}

// ===== End of the essential part =====

int main() {
	ios_base::sync_with_stdio(0);

	ParallelTaskRunner<InputData, OutputData> runner;
	runner.readData();
	runner.run();

	ofstream ostr("out.out");
	runner.print(ostr);

	return 0;
}