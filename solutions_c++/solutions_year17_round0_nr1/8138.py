#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

#define FORi(m) for( int i = 0; i < (m); ++i )
#define FOR(i, M) for( int i = 0; i < (M); ++i )
#define FOR1(i, M) for( int i = 1; i <= (M); ++i )
#define DEBUGGING 1
#define CERRL() if (DEBUGGING) { std::cerr << '\n'; }
#define EXAM(var) if (DEBUGGING) { std::cerr << #var << ": " << (var) << '\n'; }
#define EXAMARR(var) if (DEBUGGING) { std::cerr << #var << ": "; for (const auto& _var_: var) std::cerr << _var_ << " "; std::cerr << '\n'; }



int solve(string S, int K) {
	vector<bool> r(S.length());
	transform(S.begin(), S.end(), r.begin(), [](char c) { return c == '+'; });
	int tries = 0, i;
	for (i = 0; i <= S.length() - K; i++) {
		if (r[i]) continue;
		tries++;
		for (int j = 0; j < K; j++) {
			r[i+j].flip();
		}
	}
	for (; i < S.length(); i++) {
		if (!r[i]) return -1;
	}
	return tries;
}


int main() {
	int T;
    cin >> T;
    FOR1(t, T) {
    	string S;
        int K;
    	cin >> S >> K;
    	auto r = solve(S, K);
//    	EXAMARR(r);
        cout << "Case #" << t << ": " << (r == -1 ? "IMPOSSIBLE": to_string(r)) << endl;
    }
}

