#pragma comment(linker, "/STACK:64777216")

#include <cstdio>
#include <cmath>
#include <cstring>
#include <ctime>
#include <algorithm>
#include <vector>
#include <queue>
#include <string>
#include <map>
#include <unordered_map>
#include <set>
#include <iostream>
#include <functional>
#include <numeric>
#include <sstream>
#include <exception>
#include <cassert>
#include <thread>
#include <mutex>
#include <iomanip>

typedef long long i64;
typedef unsigned long long u64;
typedef unsigned int u32;
using namespace std;

typedef vector<int> VI;
#define endl '\n'

#define all(a) a.begin(),a.end()

template<class T>
int size(const T &a) {
    return int(a.size());
}

template<class T>
T abs(const T &a) {
    return (a < 0 ? -a : a);
}

template<class T>
T sqr(const T &a) {
    return a * a;
}

const double pi = acos(-1.0);

int mod = int(1e9 + 7.1);

inline int msum(int a, int b) {
    return (a + b < mod ? a + b : a + b - mod);
}

inline int mdiff(int a, int b) {
    return (a < b ? a - b + mod : a - b);
}

inline void madd(int &a, int b) {
    a = msum(a, b);
}

inline void msub(int &a, int b) {
    a = mdiff(a, b);
}

inline i64 mmul(int a, int b) {
    return i64(a) * b % mod;
}

struct Solver {
	//define only input data & result
	int n, p;
	vector<int> a;
	int result;

	vector<vector<int> > b;

	void read() {
		cin >> n >> p;
		a.resize(p, 0);
		for (int i = 0; i < n; ++i) {
			int t;
			cin >> t;
			++a[t % p];
		}
	}

	map<vector<int>, int> dp;

	int solve(vector<int> &a) {
		auto it = dp.find(a);
		if (it != dp.end()) {
			return it->second;
		}
		int res = accumulate(all(a), 0) > 0? 1 : 0;
		for (auto &x : b) {
			bool g = true;
			for (int j = 0; j < p - 1; ++j) {
				a[j] -= x[j];
				if (a[j] < 0) {
					g = false;
				}
			}
			if (g) {
				res = max(res, solve(a) + 1);
			}
			for (int j = 0; j < p - 1; ++j) {
				a[j] += x[j];
			}
		}

		return dp[a] = res;
	}

    void solve() {
		result = a[0];
		a.erase(a.begin());
		if (p == 2) {
			b.push_back({ 2 });
		}
		else if (p == 3) {
			b.push_back({ 3,0 });
			b.push_back({ 1,1 });
			b.push_back({ 0,3 });
		}
		else if (p == 4) {
			b.push_back({ 4, 0, 0 });
			b.push_back({ 2, 1, 0 });
			b.push_back({ 1, 0, 1 });
			b.push_back({ 0, 2, 0 });
			b.push_back({ 0, 0, 4 });
			b.push_back({ 0, 1, 2 });
		}
		result += solve(a);
		
	}

	void print() {
		cout << result;
	}
};

vector<Solver> res;

struct Thread {
	thread t;
	int rem, mod;
	void solve(int rem, int mod) {
		this->rem = rem;
		this->mod = mod;
		t = thread(&Thread::run, this);
	}

	void run() {
		int n = res.size();
		for (int i = rem; i < n; i += mod) {
			res[i].solve();
		}
	}

};


int main() {

#ifdef pperm
    freopen("input.txt", "r", stdin);
    //freopen("input.txt", "w", stdout);
    freopen("output.txt", "w", stdout);
#endif
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int T = 1;
    cin >> T;
	res.resize(T);
    for (int iTest = 0; iTest < T; ++iTest) {
		res[iTest].read();
    }
	int nThreads = 4;
#ifdef _DEBUG
	nThreads = 1;
#endif
	vector<Thread> threads(nThreads);
	for (int i = 0; i < nThreads; ++i) {
		threads[i].solve(i, nThreads);
	}
	for (int i = 0; i < nThreads; ++i) {
		threads[i].t.join();
	}
    for (int i = 0; i < T; i++) {
		cout << "Case #" << (i + 1) << ": ";
		res[i].print();
		cout << endl;
    }
#ifdef pperm
    flush(cout);
    cerr << endl << "Time: " << (clock() / double(CLOCKS_PER_SEC)) << endl;
#endif
    return 0;
}
