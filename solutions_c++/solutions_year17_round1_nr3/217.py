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

const int MAXN = 105;

//[dragon health][dragon attack][knight health][knight attack]
int dp[MAXN][MAXN][MAXN][MAXN];
int hd, ad, hk, ak, b, d;

int recur(int DH, int DA, int KH, int KA) {
	if (KH <= 0) {
		//cout << DH << ", ";
		//cout << DA << ", ";
		//cout << KH << ", ";
		//cout << KA << " returns 0\n";
		return 0;
	}
	if (DH <= 0) {
		//cout << DH << ", ";
		//cout << DA << ", ";
		//cout << KH << ", ";
		//cout << KA << " returns INF\n";
		return INF;
	}
	if (DA >= MAXN) {
		DA = MAXN - 1;
	}
	if (KA < 0) {
		KA = 0;
	}

	if (dp[DH][DA][KH][KA] != -1) {
		return dp[DH][DA][KH][KA];
	}
	//syntactic sugar
	int &dpv = dp[DH][DA][KH][KA];

	dpv = INF;

	//buff self
	if (DA + b < MAXN) {
		dpv = min(dpv, recur(DH - KA, DA + b, KH, KA) + 1);
	}

	//nerf dragon
	if (KA != 0) {
		int newDMG = max(0, KA - d);
		if (newDMG != KA) {
			dpv = min(dpv, recur(DH - newDMG, DA, KH, newDMG) + 1);
		}
	}

	//attack
	dpv = min(dpv, recur(DH - KA, DA, KH - DA, KA) + 1);

	//cure, make sure afterwards we would actually gain health
	if (DH < hd - KA) {
		dpv = min(dpv, recur(hd - KA, DA, KH, KA) + 1);
	}
	return dpv;
}

string testcase() {
	memset(dp, -1, sizeof(dp));

	cin >> hd >> ad >> hk >> ak >> b >> d;
	int ans = recur(hd, ad, hk, ak);
	//for (int x1 : range(MAXN)) {
	//	for (int x2 : range(MAXN)) {
	//		for (int x3 : range(MAXN)) {
	//			for (int x4 : range(MAXN)) {
	//				if (dp[x1][x2][x3][x4] != -1) {
	//					cout << x1 << ", ";
	//					cout << x2 << ", ";
	//					cout << x3 << ", ";
	//					cout << x4 << " = " << dp[x1][x2][x3][x4] << "\n";
	//				}
	//			}
	//		}
	//	}
	//}
	if (ans < INF) {
		return to_string(ans);
	} else {
		return "IMPOSSIBLE";
	}
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