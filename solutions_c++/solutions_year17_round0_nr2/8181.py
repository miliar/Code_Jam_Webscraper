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

bool isTidy(ll v) {
	string str = to_string(v);
	return is_sorted(str.begin(), str.end());
}

string testcase() {
	ll N;
	cin >> N;

	

	string lim = to_string(N);

	if (isTidy(N)) {
		return lim;
	}
	fill(lim.begin(), lim.end(), '1');
	if (N < stoll(lim)) {
		return string(lim.size() - 1, '9');
	}

	for (int a = lim.size() - 1; a >= 0; a--) {
		if (lim[a] == '0') {
			continue;
		}
		string tmp = to_string(N);
		tmp[a]--;
		fill(tmp.begin() + a + 1, tmp.end(), '9');
		if (is_sorted(tmp.begin(), tmp.end())) {
			return tmp;
		}
		//cout << tmp << " doesn't work\n";
	}

	return "wtf";
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