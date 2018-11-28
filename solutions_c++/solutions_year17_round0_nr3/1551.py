#include <bits/stdc++.h>

using namespace std;
typedef long long LL;

pair<LL, LL> get_split(LL len) {
	len--;
	LL half = len >> 1;
	LL other = len - half;
	return {max(half, other), min(half, other)};
}

void process_segment(LL num, LL cnt, LL& odd, LL& odd_cnt, LL& even, LL& even_cnt) {
	if (num == 0) return;
	if (num & 1) {
		if (odd == -1) odd = num;
		odd_cnt += cnt;
	} else {
		if (even == -1) even = num;
		even_cnt += cnt;
	}
}

void gen_next(LL& odd, LL& even, LL& odd_cnt, LL& even_cnt) {
	LL nodd = -1, neven = -1, nodd_cnt = 0, neven_cnt = 0;
	 if (odd != -1) {
		pair<LL, LL> temp = get_split(odd);
		process_segment(temp.first, odd_cnt, nodd, nodd_cnt, neven, neven_cnt);
		process_segment(temp.second, odd_cnt, nodd, nodd_cnt, neven, neven_cnt);
	}
	if (even != -1) {
		pair<LL, LL> temp = get_split(even);
		process_segment(temp.first, even_cnt, nodd, nodd_cnt, neven, neven_cnt);
		process_segment(temp.second, even_cnt, nodd, nodd_cnt, neven, neven_cnt);
	}
	odd = nodd, even = neven, odd_cnt = nodd_cnt, even_cnt = neven_cnt;
}

pair<LL, LL> get_last(LL odd, LL even, LL odd_cnt, LL even_cnt, LL K) {
	if (K == 0) {
		if (odd == -1) {
			return {even, even};
		} else if (even == -1) {
			return {odd, odd};
		}
		return {max(odd, even), min(odd, even)};
	}
	LL max_cnt = odd > even ? odd_cnt : even_cnt;
	LL split = K > max_cnt ? min(odd, even) : max(odd, even);
	return get_split(split);
}

pair<LL, LL> get_count(LL start, LL end, LL K) {
	if (K == 1) {
		return get_split(end - start + 1);
	}
	if (K == end - start + 1) {
		return {0, 0};
	}

	// init
	K--;
	LL odd_cnt = 0, even_cnt = 0;
	LL odd = -1, even = -1;
	LL len = end - start + 1;
	if (len & 1) {
		LL half = len >> 1;
		if (half & 1) {
			odd = half;
			odd_cnt = 2;
		} else {
			even = half;
			even_cnt = 2;
		}
	} else {
		LL less = (len - 1) >> 1;
		LL greater = len - 1 - less;
		if (less & 1) {
			odd = less;
			even = greater;
		} else {
			odd = greater;
			even = less;
		}
		odd_cnt = even_cnt = 1;
	}

	// iteration
	while (K > odd_cnt + even_cnt) {
		K -= odd_cnt + even_cnt;
		gen_next(odd, even, odd_cnt, even_cnt);
	}
	return get_last(odd, even, odd_cnt, even_cnt, K);
}

int main() {
  freopen("input", "r", stdin);
  freopen("output", "w", stdout);
  int T; cin >> T;
  for (int kase = 1; kase <= T; kase++) {
  	LL N, K; cin >> N >> K;
  	auto result = get_count(1, N, K);
  	cout << "Case #" << kase << ": " << result.first << " " << result.second << endl;
  }
  return 0;
}
