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
	vector<pair<int, int>> c, j;
};

struct OutputData {
	int res;
};

istream& operator >>(istream& istr, InputData& inputData) {
	int n, m;
	istr >> n >> m;
	inputData.c.resize(n);
	inputData.j.resize(m);
	for (int i = 0; i < n; ++i) {
		istr >> inputData.c[i].first >> inputData.c[i].second;
	}
	for (int i = 0; i < m; ++i) {
		istr >> inputData.j[i].first >> inputData.j[i].second;
	}
	return istr;
}

ostream& operator <<(ostream& ostr, const OutputData& outputData) {
	ostr << outputData.res;
	return ostr;
}

OutputData solve(InputData inputData) {
	int N = 24 * 60;
	vector<int> who(N, 3);
	for (auto p : inputData.c) {
		for (int i = p.first; i < p.second; ++i) {
			who[i] &= (~1);
		}
	}
	for (auto p : inputData.j) {
		for (int i = p.first; i < p.second; ++i) {
			who[i] &= (~2);
		}
	}

	vector<vector<vector<vector<int>>>> dp(2, vector<vector<vector<int>>>(N, vector<vector<int>>(N / 2 + 1, vector<int>(2, 100000000))));
	for (int i = 0; i < 2; ++i) {
		if (who[0] & (1 << i)) {
			dp[i][0][i][i] = 0;
		}
	}

	for (int i = 1; i < N; ++i) {
		for (int s = 0; s < 2; ++s) {
			for (int f = 0; f < 2; ++f) {
				if (!(who[i] & (1 << f))) {
					continue;
				}
				for (int pr = 0; pr < 2; ++pr) {
					for (int j = 0; j <= i && j <= N / 2; ++j) {
						if (dp[s][i - 1][j][pr] > 1e7) {
							continue;
						}
						if (j + f > N / 2) {
							continue;
						}
						if (pr == f) {
							dp[s][i][j + f][f] = min(dp[s][i][j + f][f], dp[s][i - 1][j][pr]);
						} else {
							dp[s][i][j + f][f] = min(dp[s][i][j + f][f], dp[s][i - 1][j][pr] + 1);
						}
					}
				}
			}
		}
	}

	int ans = 1e8;
	for (int i = 0; i < 2; ++i) {
		for (int j = 0; j < 2; ++j) {
			ans = min(ans, dp[i][N - 1][N / 2][j] + (i == j ? 0 : 1));
		}
	}

	return {ans};
}

// ===== End of the essential part =====

int main() {
	ios_base::sync_with_stdio(0);

	ParallelTaskRunner<InputData, OutputData> runner(1);
	runner.readData();
	runner.run();

	ofstream ostr("out.out");
	runner.print(ostr);

	return 0;
}