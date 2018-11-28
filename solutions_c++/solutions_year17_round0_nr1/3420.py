#include <cstdio>
#include <string>
#include <iostream>

using namespace std;

int k;

int f(string s, int flip_start_idx) {
    if (flip_start_idx + k > s.length()) {
	for (int i = flip_start_idx; i < s.length(); i++) {
	    if (s[i] == '-') return -1;
	}
	return 0;
    }

    if (s[flip_start_idx] == '+') return f(s, flip_start_idx+1);

    for (int i = flip_start_idx; i < flip_start_idx + k; i++) {
	if (s[i] == '+') s[i] = '-';
	else s[i] = '+';
    }
    int ret = f(s, flip_start_idx+1);
    if (ret == -1) return -1;
    return ret+1;
}

int main() {

    int TC;
    cin >> TC;

    for (int tc = 1; tc <= TC; tc++) {
	string state;
	cin >> state;
	cin >> k;
	
	int result = f(state, 0);
	printf("Case #%d: ", tc);
	if (result == -1) {
	    printf("IMPOSSIBLE\n");
	} else {
	    printf("%d\n", result);
	}
    }
    return 0;
}
