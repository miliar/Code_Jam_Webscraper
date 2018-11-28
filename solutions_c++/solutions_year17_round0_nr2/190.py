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
	long long x;
};

using OutputData = string;

// struct OutputData {
// 	int x;
// };

istream& operator >>(istream& istr, InputData& inputData) {
	istr >> inputData.x;
	return istr;
}

// ostream& operator <<(ostream& ostr, const OutputData& outputData) {
// 	ostr << outputData.x;
// 	return ostr;
// }

OutputData solve(InputData inputData) {
	string s = to_string(inputData.x);
	int n = s.length();
	int index = 0;
	while (index + 1 < n && s[index] <= s[index + 1]) {
		++index;
	}
	if (index == n - 1) {
		return s;
	} else {
		s = s.substr(0, index + 1) + string(n - index - 1, '9');
		s[index] -= 1;
		while (index > 0 && s[index] < s[index - 1]) {
			s[index] = '9';
			--index;
			s[index] -= 1;
		}
		while (s[0] == '0') {
			s = s.substr(1);
		}
		return s;
	}
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