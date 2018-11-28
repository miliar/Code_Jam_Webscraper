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

bool check(string S){
	int max_c = -1;
	for (int i = 0; i < S.size(); i ++){
		max_c = max(max_c, (int) S[i]);
		if (S[i] < max_c)
			return false;
	}
	return true;
}

int main(){
	int T = FastInput::nextInt();
		for (int t = 0; t < T; t ++){
		lli N = FastInput::nextLong();
		lli K = FastInput::nextLong();
		lli C, L;
		if (N % 2 == 0){
			C = 1;
			L = 0;
		} else{
			C = 0;
			L = 1;
		}
		lli maximal = N;
		lli res_in;
		while (true){
			if (K > (C + L))
				K -= (C + L);
			else if (K == C + L){
				if (maximal % 2 == 0){
					if (L > 0) res_in = maximal - 1;
					else res_in = maximal;
				} else{
					if (C > 0) res_in = maximal - 1;
					else res_in = maximal;
				}
				break;
			} else{
				if (maximal % 2 == 0){
					if (K <= C) res_in = maximal;
					else res_in = maximal - 1;
				} else{
					if (K <= L) res_in = maximal;
					else res_in = maximal - 1;
				}
				break;
			}
			lli odd;
			if (maximal % 2 == 0) odd = maximal - 1;
			else odd = maximal;
			odd /= 2;
			if (odd % 2 == 0){
				lli old_C = C;
				C = 2 * L + C;
				L = old_C;
			} else{
				L = 2 * L + C;
			}
			maximal /= 2;
		}
		lli LS, RS;
		if (res_in % 2 == 0){
			LS = res_in / 2 - 1;
			RS = res_in / 2;
		} else{
			LS = res_in / 2;
			RS = res_in / 2;
		}
		cout << "Case #" << t + 1 << ": " << max(LS, RS) << " " << min(LS, RS) << endl;
	}
	return 0;
}