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
	return is >> p.first >> p.second;
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

string testcase() {
	int K;
	string str;
	cin >> str >> K;

	queue<int> q;
	int flip = 0;
	int cost = 0;
	for (int a = 0; a + K <= str.size(); a++) {
		while (!q.empty() && q.front() == a) {
			flip ^= 1;
			q.pop();
		}
		int v = ((str[a] == '+') ^ flip);
		if (v == 1) {
			//correct!
		} else {
			cost++;
			flip ^= 1;
			q.push(a + K);
		}
		str[a] ^= (flip * 6);
	}
	for (int a = str.size() - K + 1; a < str.size(); a++) {
		while (!q.empty() && q.front() == a) {
			flip ^= 1;
			q.pop();
		}
		if (flip) {
			str[a] ^= 6;
		}
		int v = str[a] == '+';
		if (v == 0) {
			return "IMPOSSIBLE";
		}
	}
	return to_string(cost);
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
		cout << "Case #" << a << ": " << testcase() << "\n";
	}
}
#endif