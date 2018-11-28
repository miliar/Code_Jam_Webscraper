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

struct InputData {
	vector<string> a;
};

struct OutputData {
	bool ans;
	vector<string> a;
};

istream& operator >>(istream& istr, InputData& inputData) {
	int n, m;
	istr >> n >> m;
	inputData.a.resize(n);
	for (int i = 0; i < n; ++i) {
		istr >> inputData.a[i];
	}
	return istr;
}

ostream& operator <<(ostream& ostr, const OutputData& outputData) {
	if (!outputData.ans) {
		ostr << "IMPOSSIBLE";
		return ostr;
	}
	ostr << "POSSIBLE";
	for (auto s : outputData.a) {
		ostr << "\n" << s;
	}
	return ostr;
}

const int xx[4] = {-1, 0, 1, 0};
const int yy[4] = {0, -1, 0, 1};

struct Field {
	int n, m;
	vector<string> s;
	vector<vector<vector<pair<int, int>>>> a;
	vector<vector<vector<char>>> used;
	vector<vector<int>> num;

	Field(const vector<string>& ar) {
		s = ar;
		n = ar.size();
		m = ar[0].size();
		a.resize(n, vector<vector<pair<int, int>>>(m, vector<pair<int, int>>(4, {-1, -1})));
		used.resize(n, vector<vector<char>>(m, vector<char>(4, 0)));
		num.resize(n, vector<int>(m, 0));

		int cur = 0;
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < m; ++j) {
				if (s[i][j] == '|' || s[i][j] == '-') {
					num[i][j] = cur++;
				}
			}
		}
	}

	pair<int, int> mark(int x, int y, int d) {
		if (used[x][y][d]) {
			return a[x][y][d];
		}
		used[x][y][d] = 1;
		int nx = x + xx[d];
		int ny = y + yy[d];
		auto& res = a[x][y][d];
		if (nx < 0 || nx >= n || ny < 0 || ny >= m) {
			return res;
		}
		if (s[nx][ny] == '#') {
			return res;
		} else if (s[nx][ny] == '.') {
			return res = mark(nx, ny, d);
		} else if (s[nx][ny] == '/') {
			return res = mark(nx, ny, 3 - d);
		} else if (s[nx][ny] == '\\') {
			return res = mark(nx, ny, d ^ 1);
		} else {
			return res = {num[nx][ny], d % 2};
		}
	}

	void markAll() {
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < m; ++j) {
				for (int ij = 0; ij < 4; ++ij) {
					mark(i, j, ij);
				}
			}
		}
	}
};

struct Graph {
	int n;
	vector<vector<int>> a;
	vector<vector<int>> ar;
	vector<char> used;
	vector<int> order;

	Graph(const vector<vector<int>>& ed) {
		a = ed;
		n = a.size();

		ar.resize(n);
		for (int i = 0; i < n; ++i) {
			for (int j : a[i]) {
				ar[j].push_back(i);
			}
		}

		used.assign(n, 0);
	}

	void dfs(int v) {
		used[v] = 1;
		for (itn x : a[v]) {
			if (!used[x]) {
				dfs(x);
			}
		}
		order.push_back(v);
	}

	void dfs1(int v, vector<int>& comp) {
		used[v] = 2;
		comp.push_back(v);
		for (int x : ar[v]) {
			if (used[x] < 2) {
				dfs1(x, comp);
			}
		}
	}

	vector<vector<int>> getScc() {
		vector<vector<int>> res;
		for (int i = 0; i < n; ++i) {
			if (!used[i]) {
				dfs(i);
			}
		}
		reverse(all(order));
		for (int i : order) {
			if (used[i] < 2) {
				res.emplace_back();
				dfs1(i, res.back());
			}
		}
		return res;
	}
};

struct TwoSat {
	int n;
	vector<pair<int, int>> a;

	TwoSat(int _n): n(_n) {}

	int f(int x) const {
		if (x < 0) {
			return n - x - 1;
		} else {
			return x - 1;
		}
	}

	void add(int x, int y) {
		a.push_back({-x, y});
		a.push_back({-y, x});
	}

	void add(int x) {
		a.push_back({-x, x});
	}

	vector<char> solve() {
		vector<vector<int>> ed(n + n);
		for (auto p : a) {
			ed[f(p.first)].push_back(f(p.second));
			// cerr << f(p.first) << " -> " << f(p.second) << "\n";
		}

		Graph gr(ed);
		auto sccs = gr.getScc();
		vector<int> color(n + n);
		for (int i = 0; i < (int)sccs.size(); ++i) {
			for (int x : sccs[i]) {
				color[x] = i;
			}
		}
		// for (auto v : sccs) {
		// 	for (int x : v) {
		// 		cerr << x << " ";
		// 	}
		// 	cerr << "\n";
		// }
		vector<char> res(n);
		for (int i = 0; i < n; ++i) {
			if (color[i] == color[i + n]) {
				return {};
			} else {
				res[i] = color[i] > color[i + n];
			}
		}
		return res;
	}
};

OutputData solve(InputData inputData) {
	auto a = inputData.a;
	int n = a.size(), m = a[0].size();

	Field field(a);
	field.markAll();

	int cnt_beams = 0;
	vector<vector<int>> num(n, vector<int>(m, 0));
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < m; ++j) {
			if (a[i][j] == '|' || a[i][j] == '-') {
				num[i][j] = cnt_beams++;
			}
		}
	}

	TwoSat twosat(cnt_beams);
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < m; ++j) {
			if (a[i][j] == '.') {
				vector<pair<int, int>> ps = field.a[i][j];
				vector<int> hmm(2, 0);
				for (int k = 0; k < 2; ++k) {
					if (ps[k].first == -1 && ps[k + 2].first == -1) {
						continue;
					} else if (ps[k + 2].first == -1) {
						hmm[k] = (ps[k].first + 1) * (2 * ps[k].second - 1);
					} else if (ps[k].first == -1) {
						hmm[k] = (ps[k + 2].first + 1) * (2 * ps[k + 2].second - 1);
					} else {
						twosat.add((ps[k].first + 1) * (-2 * ps[k].second + 1));
						twosat.add((ps[k + 2].first + 1) * (-2 * ps[k + 2].second + 1));
					}
				}
				if (hmm[0] && hmm[1]) {
					// cerr << hmm[0] << " " << hmm[1] << "\n";
					twosat.add(hmm[0], hmm[1]);
				} else if (hmm[0]) {
					twosat.add(hmm[0]);
				} else if (hmm[1]) {
					twosat.add(hmm[1]);
				} else {
					return {false, {}};
				}
			} else if (a[i][j] == '/') {
				vector<pair<int, int>> ps = field.a[i][j];
				// vector<int> hmm(2, 0);
				for (int k = 0; k < 4; k += 2) {
					if (ps[k].first == -1 && ps[k ^ 1].first == -1) {
						continue;
					} else if (ps[k ^ 1].first == -1) {
						// hmm[k] = (ps[k].first + 1) * (2 * ps[k].second - 1);
					} else if (ps[k].first == -1) {
						// hmm[k] = (ps[k ^ 1].first + 1) * (2 * ps[k ^ 1].second - 1);
					} else {
						twosat.add((ps[k].first + 1) * (-2 * ps[k].second + 1));
						twosat.add((ps[k ^ 1].first + 1) * (-2 * ps[k ^ 1].second + 1));
					}
				}
			} else if (a[i][j] == '\\') {
				vector<pair<int, int>> ps = field.a[i][j];
				// vector<int> hmm(2, 0);
				for (int k = 0; k < 2; ++k) {
					if (ps[k].first == -1 && ps[3 - k].first == -1) {
						continue;
					} else if (ps[3 - k].first == -1) {
						// hmm[k] = (ps[k].first + 1) * (2 * ps[k].second - 1);
					} else if (ps[k].first == -1) {
						// hmm[k] = (ps[3 - k].first + 1) * (2 * ps[3 - k].second - 1);
					} else {
						twosat.add((ps[k].first + 1) * (-2 * ps[k].second + 1));
						twosat.add((ps[3 - k].first + 1) * (-2 * ps[3 - k].second + 1));
					}
				}
			} else if (a[i][j] == '|' || a[i][j] == '-') {
				vector<pair<int, int>> ps = field.a[i][j];
				// vector<int> hmm(2, 0);
				for (int k = 0; k < 4; ++k) {
					if (ps[k].first != -1) {
						twosat.add((num[i][j] + 1) * (-2 * (k % 2) + 1));
						twosat.add((ps[k].first + 1) * (-2 * ps[k].second + 1));
					}
				}
			}
		}
	}

	auto res = twosat.solve();
	if (res.empty()) {
		return {false, {}};
	}
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < m; ++j) {
			if (a[i][j] == '-' || a[i][j] == '|') {
				a[i][j] = (res[num[i][j]] ? '-' : '|');
			}
		}
	}
	return {true, a};
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