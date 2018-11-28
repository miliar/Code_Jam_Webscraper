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
#include <iomanip>
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

int main(){
	int T = FastInput::nextInt();
	for (int t = 1; t <= T; t ++){
		int D = FastInput::nextInt();
		int N = FastInput::nextInt();
		int K[N], S[N];
		double time[N];
		double max_t = -1;
		for (int i = 0; i < N; i ++){
			K[i] = FastInput::nextInt();
			S[i] = FastInput::nextInt();
			time[i] = (D - K[i]) / (double) S[i];
			if (time[i] > max_t)
				max_t = time[i];
		}
		cout << fixed;
		cout << setprecision(6);
		cout << "Case #" << t << ": " << D / max_t << endl;
	}
	return 0;
}