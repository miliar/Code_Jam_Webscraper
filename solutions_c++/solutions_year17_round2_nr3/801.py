#define _CRT_SECURE_NO_WARNINGS

#include <vector>
#include <iostream>
#include <string>
#include <algorithm>
#include <iomanip>

using namespace std;

void solve_single_C() {
	int n, q;
	cin >> n >> q;
	vector<long long> speed(n);
	vector<long long> capacity(n);
	for (int i = 0; i < n; ++i) {
		cin >> capacity[i] >> speed[i];
	}
	vector<vector<long long>> length(n, vector<long long>(n));
	for (long long i = 0; i < n; ++i) {
		for (int j = 0; j < n; ++j) {
			cin >> length[i][j];
		}
	}
	long long cur;
	for (int i = 0; i < q; ++i) {
		cin >> cur >> cur;
	}
	vector<double> ans(n, 1e18);
	ans[0] = 0;
	for (int i = 1; i < n; ++i) {
		long long sum_length = 0;
		for (int j = i-1; j >= 0; --j) {
			sum_length += length[j][j + 1];
			if (ans[i] > ans[j] + static_cast<double>(sum_length) / speed[j] && capacity[j] >= sum_length) {
				ans[i] = ans[j] + static_cast<double>(sum_length) / speed[j];
			}
		}
	}
	printf("%f\n", ans[n-1]);
}

void solve_single_B() {
	int n;
	vector<int> base(3);
	vector<char> base_symbol{'R','Y','B'};
	vector<int> doubled(3);
	vector<char> doubled_symbol{'G', 'V', 'O'};
	cin >> n >> base[0] >> doubled[2] >> base[1]  >> doubled[0] >> base[2] >> doubled[1];
	string ans;
	ans.resize(n);
	for (int i = 0; i < 3; ++i) {
		if (doubled[i] > 0 && doubled[i] >= base[i]) {
			if (n == doubled[i] + base[i] && doubled[i] == base[i]) {
				for (int j = 0; j < doubled[i]; ++j) {
					ans[2 * j] = doubled_symbol[i];
					ans[2 * j + 1] = base_symbol[i];
				}
				cout << ans << endl;
				return;
			}
			else {
				cout << "IMPOSSIBLE" << endl;
				return;
			}
		}
	}
	vector<string> first(3);
	int sum = 0;
	for (int i = 0; i < 3; ++i) {
		base[i] = base[i] - doubled[i];
		first[i].resize(2 * doubled[i] + 1);
		for (int j = 0; j < doubled[i]; ++j) {
			first[i][2 * j] = base_symbol[i];
			first[i][2 * j + 1] = doubled_symbol[i];
		}
		first[i][2 * doubled[i]] = base_symbol[i];
		sum += base[i];
	}
	ans.resize(0);
	for (int i = 0; i < 3; ++i) {
		if (2 * base[i] > sum) {
			cout << "IMPOSSIBLE" << endl;
			return;
		}
	}
	int rest = sum;
	int last = -1;
	int first_index = -1;
	while (rest > 0) {
		int max = first_index == -1 ? 0 : first_index;
		if (max == last) {
			if (last != 0) {
				max = 0;
			}
			else {
				max = 1;
			}
		}
		if (base[0] > base[max] && last != 0 ) {
			max = 0;
		}
		if (base[1] > base[max] && last != 1) {
			max = 1;
		}
		if (base[2] > base[max] && last != 2) {
			max = 2;
		}
		ans += first[max];
		first[max] = base_symbol[max];
		base[max]--;
		if (rest == sum) {
			first_index = max;
		}
		rest--;
		last = max;
		if (rest == 0 && ans[ans.size() - 1] == ans[0]) {
				
			char last_char = ans[ans.size() - 1];
			ans[ans.size() - 1] = ans[ans.size() - 2];
			ans[ans.size() - 2] = last_char;
		}
	}
	cout << ans << endl;
	return;
}

void solve_single_A() {
	int D, n;
	cin >> D >> n;
	vector<int> d(n);
	vector<int> s(n);
	double max_time = 0;
	for (int i = 0; i < n; ++i) {
		cin >> d[i] >> s[i];
		max_time = max(max_time, static_cast<double>(D - d[i]) / s[i]);
	}
	printf("%f\n", static_cast<double> (D) / max_time);
	//cout <<  std::setprecision(6) << static_cast<double> (D) / max_time << endl;
}

int main () {
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	cin >> T;
	for (int i = 0; i < T; ++i) {
		cout << "Case #" << i + 1 << ": ";
		solve_single_C();
	}
	return 0;
};


//void solve_single_C() {
//	long long n;
//	long long k;
//	cin >> n >> k;
//	long long max_pow = 1;
//	int exp = 0;
//	while (max_pow * 2 < k + 1) {
//		exp++;
//		max_pow *= 2;
//	}
//	long long div = (n + 1) / max_pow;
//	long long res = (n + 1) % max_pow;
//	long long long_seg = res;
//	long long short_seg = max_pow - res;
//	long long operation_rest = k - max_pow + 1;
//	if (operation_rest <= long_seg) {
//		cout << (div + 2) / 2 - 1 << ' ' << (div + 1) / 2 - 1<< endl;
//	}
//	else {
//		cout << (div + 1) / 2 - 1 << ' ' << (div) / 2 - 1 << endl;
//	}
//}
//
//bool check_tidy(string str) {
//	for (int i = 0; i < str.size() - 1; ++i) {
//		if (str[i] > str[i + 1]) {
//			return false;
//		}
//	}
//	return true;
//}
//
//void solve_single_B() {
//	string str;
//	cin >> str;
//	if (check_tidy(str)) {
//		cout << str << endl;
//		return;
//	}
//	for (int i = str.size() - 2; i >= 0; --i) {
//		string new_str = str;
//		if (str[i] == '0') {
//			continue;
//		}
//		new_str[i] = str[i] - 1;
//		for (int j = i + 1; j < str.size(); ++j) {
//			new_str[j] = '9';
//		}
//		if (check_tidy(new_str)) {
//			if (new_str[0] == '0') {
//				new_str = new_str.substr(1, new_str.size() - 1);
//			}
//			cout << new_str << endl;
//			return;
//		}
//	}
//}
//
//void solve_single_A() {
//	string str;
//	int k;
//	cin >> str >> k;
//	int ans = 0;
//	for (int i = 0; i <= str.size() - k; ++i) {
//		if (str[i] == '-') {
//			ans++;
//			for (int j = i; j < i + k; ++j) {
//				if (str[j] == '-') {
//					str[j] = '+';
//				}
//				else {
//					str[j] = '-';
//				}
//			}
//		}
//	}
//	for (int i = 0; i < str.size(); ++i) {
//		if (str[i] != '+') {
//			cout << "IMPOSSIBLE" << endl;
//			return;
//		}
//	}
//	cout << ans << endl;
//	return;
//}