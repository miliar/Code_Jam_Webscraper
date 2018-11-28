////#define _CRT_SECURE_NO_WARNINGS
//
//#include <stdio.h>
//#include <bits/stdc++.h>
//
//using namespace std;
//
////#define F first
////#define S second
//
//// TIMER
//std::clock_t __start;
//double __duration;
//void start_timer() { __start = std::clock(); }
//void print_timer() {
//	__duration = (std::clock() - __start) / (double)CLOCKS_PER_SEC;
//	std::cout << "Duration (msec): " << __duration * 1000 << '\n';
//}
//// END TIMER
//
////PI
//#define M_PI		3.14159265358979323846
//// fast input
//#define scan(x) do{while((x=getchar())<'0'); for(x-='0'; '0'<=(_=getchar()); x=(x<<3)+(x<<1)+_-'0');}while(0)
//
//template <class T>
//T min_(T a, T b) { return (a < b ? a : b); }
//template <class T>
//T max_(T a, T b) { return (a > b ? a : b); }
//
//double EPS = 1e-16;
//bool eq_(const double& lhs, const double &rhs) {
//	return (fabs(lhs - rhs) < EPS);
//}
//
//typedef unsigned long long ull;
//typedef long long ll;
//typedef long double ld;
//typedef pair<int, int> ii;
//typedef pair<ll, ll> llll;
//typedef pair<int, ii> iii;
//typedef vector<ii> vii;
//typedef vector<ll> vll;
//typedef vector<llll> vllll;
//typedef vector<int> vi;
//typedef vector<ull> vull;
//
//const int INF = int(2e9);
//const ll INF_LL = LLONG_MAX;
//const ll MOD = 1e9 + 7;
//const int MAX_N = 1e6 + 5;
//
//
//int main() {
//	//ios_base::sync_with_stdio(false);
//	//cin.tie(0);
//	
//	ifstream fin("b.in");
//	ofstream fout("b.out");
//	int T;
//	string num;
//	fin >> T;
//	for (int t = 0; t < T; ++t) {
//		fin >> num;
//		int max_idx = 0;
//		int max_val = 0;
//		for (int i = 0;i < num.size();++i) {
//			int curr_val = num[i] - '0';
//			if (i>0 && curr_val < num[i - 1] - '0')
//				break;
//
//			if (curr_val > max_val) {
//				max_val = curr_val;
//				max_idx = i;
//			}
//		}
//		bool done = true;
//		for (int i = max_idx + 1; i < num.size(); ++i) {
//			int curr_val = num[i] - '0';
//			if (curr_val != max_val) {
//				done = false;
//				break;
//			}
//		}
//		if (!done) {
//			if (max_val == 1) {
//				num.erase(num.begin());
//			}
//			else {
//				num[max_idx]--;
//				max_idx++;
//			}
//			for (int i = max_idx; i < num.size(); ++i)
//				num[i] = '9';
//		}
//		fout << "Case #" << t + 1 << ": " << num << '\n';
//	}
//	return 0;
//}