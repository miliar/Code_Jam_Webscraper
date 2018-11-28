#include <iostream>
#include <string>
using namespace std;

#define FORi(m) for( int i = 0; i < (m); ++i )
#define FOR(i, M) for( int i = 0; i < (M); ++i )
#define FOR1(i, M) for( int i = 1; i <= (M); ++i )
#define DEBUGGING 1
#define CERRL() if (DEBUGGING) { std::cerr << '\n'; }
#define EXAM(var) if (DEBUGGING) { std::cerr << #var << ": " << (var) << '\n'; }
#define EXAMARR(var) if (DEBUGGING) { std::cerr << #var << ": "; for (const auto& _var_: var) std::cerr << _var_ << " "; std::cerr << '\n'; }


string solve(string& in) {
	int l = in.length();
	for (int i = l-2; i >= 0; i--) {
		if (in[i] > in[i+1]) {
			in[i]--;
			for (int j = i+1; j < l; j++) {
				in[j] = '9';
			}
		}
	}
	return in[0] == '0' ? in.substr(1) : in;
}


int main() {
	int T;
    cin >> T;
    FOR1(t, T) {
        string in;
    	cin >> in;
        cout << "Case #" << t << ": " << solve(in) << endl;
    }
}

