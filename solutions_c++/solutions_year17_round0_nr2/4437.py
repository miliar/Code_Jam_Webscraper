#include <cstdlib>
#include <iostream>
#include <string> 

using namespace std;

typedef long long ll;

#define MAXLEN 20

const size_t LIMIT = 4686824;

ll dp[MAXLEN][10];
ll sm[MAXLEN];

void complete() {
	for (int i = 1; i < 10; ++i) {
		dp[1][i] = 1;
	}
	ll sum = 0;
	sm[1] = 0;
	for (int j = 2; j < MAXLEN; ++j) {
		ll local_sum = 0;
		for (int i = 9; i >= 1; --i) {
			local_sum += dp[j-1][i];
			dp[j][i] = local_sum;
			// printf("dp[%d][%d] = %lld\n", j, i, dp[j][i]);
			//local_row += dp[j][i];
		}
		sum += local_sum;
		// if (sum < 0) printf("ERROR!");
		sm[j] = sum;
	} /*
	for (int i = 0; i < MAXLEN; ++i) {
		printf("sm[%d] = %lld\n", i, sm[i]);
	} */
	
	// Compute the total number of values smaller than or equal to
	
	/* for (int j = 1; j < MAXLEN; ++j) {
		ll current = 0;
		for (int i = 1; i <= 9; ++i) {
			ll temp = dp[j][i];
			dp[j][i] += current;
			current += temp;
		}
	}*/
}
/* 111111111111111110
   5679333028629099124
*/
bool isTidy(ll num) {
	ll prev = 10;
	while (num) {
		int digit = num % 10;
		num /= 10;
		if (digit > prev) {
			return false;
		}
		prev = digit;
	}
	return true;
}

string findNum(ll num) {
	if (to_string(num).size() > 18) {
		return to_string(1LL << 62);
	}
	string ans;
	int max_len = MAXLEN - 1;
	while (sm[max_len] >= num) {
		--max_len;
	}
	num -= sm[max_len];
	// printf("max_len : %d\n", max_len);
	int d = 1;
	for (int idx = max_len; idx >= 1; --idx) {
		// printf("Remaining : %lld\n", num);
		for (int digit = d; digit < 10; ++digit) {
			ll current = dp[idx][digit];
			if (current >= num) {
				d = digit;
				// printf("Found at %d digit %d with %lld\n", idx, digit, current);
				ans.push_back('0' + digit);
				break;
			}
			num = num - current;
		}
	}
	return ans;
}

ll fromString(string s) {
	ll sum = 0;
	for (int i = 0; i < s.size(); ++i) {
		sum = 10 * sum + (s[i] - '0');
	}
	return sum;
}

ll findSmaller(ll than) {
	if (isTidy(than)) {
		return than;
	}
	ll st = 1, en = LIMIT, md;
	// printf("en : %lld\n", en);
	while (st < en) {
		md = (st + en + 1) / 2;
		// printf("mid = %lld\n", md);
		if (fromString(findNum(md)) <= than) {
			st = md;
		} else {
			en = md - 1;
		}
	}
	// printf("st : %lld\n", findNum(st).c_str());
	return fromString(findNum(st));
}

ll findWithFewerDigits(int than) {
	/* if (isTidy(than)) {
		return than;
	} */
	ll cur = 1;
	while (findNum(cur).size() < than) cur *= 2;
	printf("%lld\n", cur);
	return fromString(findNum(cur));
}

int main() {
	complete();
	// printf("%lld\n", findWithFewerDigits(18));
	freopen("B-Large.in", "r", stdin);
	freopen("out.out", "w", stdout);
	int T;
	scanf("%d", &T);
	int count = 0, cur = 0;
	/*while (count < 1000) {
		// printf("%d\n",  
		++cur;
		if (isTidy(cur)) {
			++count;
			printf("%d\n", cur);
			if (findNum(count) != std::to_string(cur)) {
				printf("Error at %d with %d and %s\n", count, cur, findNum(count).c_str()); 
			}
		}
	} */
	for (int i = 1; i <= T; ++i) {
		ll cur;
		scanf("%lld", &cur);
		ll ans = findSmaller(cur);
		printf("Case #%d: %lld\n", i, ans);
	}
	
	// printf("%lld\n", findWithFewerDigits(18));
	
	return 0;
}

