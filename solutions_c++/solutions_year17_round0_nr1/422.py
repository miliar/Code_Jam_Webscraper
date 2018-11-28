#include <iostream>
#include <string>
#include <cstdio>
#include <ctype.h>
#include <limits.h>
#include <cmath>
#include <algorithm>
#include <utility>
#include <vector>
#include <unordered_set>
#include <unordered_map>
#include <array>
#include <queue>
using namespace std; 

#define gc getchar_unlocked
#define lli long long int
#define ld long double

class FastInput{
private:
	template <class T>
	inline static T nextInteger(){
		int c = gc();
		T x = 0;
		bool neg = 0;
		for (; ((c < 48 || c > 57) && c != '-'); c = gc());
		if (c == '-') {
			neg = 1;
			c = gc();
		}
		for (; c > 47 && c < 58 ; c = gc()) {
			x = (x << 1) + (x << 3) + c - 48;
		}
		if (neg)
			x = -x;
		return x;
	}
public:
	inline static int nextInt(){
		return nextInteger<int>();
	}

	inline static lli nextLong(){
		return nextInteger<lli>();
	}

	inline static string nextString(){
		string str = "";
		char c = gc();

		while (c >= 0 && c < 33)
			c = gc();

		while (!isspace(c) && c >= 0) {
			str += c;
			c = gc();
		}
		return str;
	}

	inline static string nextLine(){
		string str = "";
				char c = gc();

		while (c >= 0 && c < 33)
			c = gc();

		while (c != '\n' && c >= 0) {
			str += c;
			c = gc();
		}
		return str;
	}

	inline static ld nextDouble(){
		string str = nextString();
		ld res = {stold(str)};
		return res;
	}
};

int dp(string S, int K, int l){
	if (l == S.size()) return 0;
	if (S[l] == '+') return dp(S, K, l + 1);
	else{
		if (S.size() - l <= K - 1) return -1000000;
		string reS = "";
		for (int j = l; j < l + K; j ++)
			if (S[j] == '-') reS += "+";
			else reS += "-";
		S.replace(l, K, reS);
		return 1 + dp(S, K, l + 1);
	}
}

int main(){
	int T = FastInput::nextInt();
	for (int t = 0; t < T; t ++){
		string S = FastInput::nextString();
		int K = FastInput::nextInt();
		int res = dp(S, K, 0);
		if (res >= 0)
			cout << "Case #" << t + 1 << ": " << res << endl;
		else
			cout << "Case #" << t + 1 << ": IMPOSSIBLE" << endl;
	}
	return 0;
}