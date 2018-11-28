#ifdef NOT_DMOJ
//secret header that provides answers to all questions
#include"contest includes.h"
#else
//include everything header for GCC
#include<bits/stdc++.h>
#endif

#pragma region template code
using namespace std;
template<typename T>
using minheap = priority_queue<T, vector<T>, greater<T>>;
template<typename T>
using maxheap = priority_queue<T>;
template<typename T>
using dpair = pair<T, T>;
typedef long long ll;
typedef unsigned long long llu;
typedef dpair<int> pii;
typedef dpair<long long> pll;
typedef dpair<float> pff;
typedef dpair<double> pdd;
template<class T1, class T2>
istream& operator >> (istream &is, pair<T1, T2> &p) {
	return is >> p.irst >> p.second;
}
template<class T1, class T2>
void operator+=(vector<T1> &v, const T2 &obj) {
	v.push_back(obj);
}
template<class T1>
void operator+=(vector<T1> &v, const T1 &obj) {
	v.push_back(obj);
}
ll get_millis() {
	using namespace std::chrono;
	return duration_cast<milliseconds>(system_clock::now().time_since_epoch()).count();
}
const int INF = 0x3f3f3f3f;
const ll mod = 1e9 + 7;
#define in :
class range {
public:
	range(int end) :_start(0), _end(end), _step(1) {}
	range(int start, int end) :_start(start), _end(end), _step(1) {}
	range(int start, int end, int step) :_start(start), _end(end), _step(step) {}
	class iterator {
	public:
		iterator(int v, range &par) :val(v), parent(par) {};
		int operator*() const { return val; }
		int operator++() { return (val += parent._step); }
		bool operator==(const range::iterator &iter) const {
			//check if both out of bounds
			if (&parent != &iter.parent) { return false; }
			if (val == iter.val) { return true; }
			if (parent._step > 0) {
				return val >= parent._end && iter.val >= parent._end;
			} else {
				return val <= parent._end && iter.val <= parent._end;
			}
		}
		bool operator!=(const range::iterator &iter) const { return !(this->operator==(iter)); }
	private:
		int val;
		range &parent;
	};
	range::iterator begin() { return{ _start, *this }; }
	range::iterator end() { return{ _end, *this }; }
protected:
	int _start, _end, _step;
private:
};

#pragma endregion

const int MAXN = 3e5 + 5;

string testcase() {
	int R, C;
	cin >> R >> C;
	vector<string> grid;
	for (int a = 0; a < R; a++) {
		string str;
		cin >> str;
		grid.push_back(str);
	}

	bool found = false;
	for (int a = 0; a < R; a++) {
		char foundC = '!';
		for (int b = 0; b < C; b++) {
			if (grid[a][b] != '?') {
				found = true;
				foundC = grid[a][b];
				int idx = b - 1;
				while (idx >= 0 && grid[a][idx] == '?') {
					grid[a][idx] = grid[a][b];
					idx--;
				}
			} else if (foundC != '!') {
				grid[a][b] = foundC;
			}
		}
	}
	for (int a = 1; a < R; a++) {
		if (grid[a][0] == '?') {
			grid[a] = grid[a - 1];
		}
	}
	for (int a = R - 2; a >= 0; a--) {
		if (grid[a][0] == '?') {
			grid[a] = grid[a + 1];
		}
	}

	string ans = "";
	for (int a = 0; a < R; a++) {
		ans += grid[a] + "\n";
	}
	return ans;
}

#ifndef SIGNATURE_GRADER
int main() {
#ifdef NOT_DMOJ
	freopen("text.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#else
	cin.tie(0);
	cin.sync_with_stdio(0);
#endif
	int T;
	cin >> T;
	for (int a = 1; a <= T; a++) {
		cout << "Case #" << a << ":\n" << testcase();
	}

}
#endif