//
//  main.cpp
//  GCJ 2017 Qualification Round - Problem A. Oversized Pancake Flipper
//
//  Created by Arturo Martin-de-Nicolas on 4/8/17.
//  Copyright © 2017 ___Arturo_Martin-de-Nicolas___. All rights reserved.
//

#include <iostream>
#include <limits>
#include <string>

using std::cin;
using std::cout;
using std::string;

enum { ERROR = std::numeric_limits<int>::max(), IMPOSSIBLE = ERROR-1 };

static void flip(string & S, int const X, int const K) {
	for(int i=X; i<X+K; ++i) {
		S[i] = (S[i] == '-') ? '+' : '-';
	}
}

static int min_left(string const& S, int const K) {
	string s{S};
	int const L = S.length();
	int m{0};
	int i{0};
	for(; i<=(L-K); ++i) {
		if (s[i]=='-') {
			++m;
			flip(s,i,K);
		}
	}
	for(; i<L; ++i) {
		if (s[i] == '-') return IMPOSSIBLE;
	}
	return m;
}

static int min_right(string const& S, int const K) {
	string s{S};
	int const L = S.length();
	int m{0};
	int i{L-1};
	for(; i>=K-1; --i) {
		if (s[i]=='-') {
			++m;
			flip(s,i+1-K,K);
		}
	}
	for(; i>=0; --i) {
		if (s[i] == '-') return IMPOSSIBLE;
	}
	return m;
}

static int min_times(string const& S, int const K) {
	int const L = S.length();
	if (K < 2 || L < 2 || K > L) return ERROR;
	return std::min( min_left(S,K), min_right(S,K) );
}

int main()
{
    int T;
    cin >> T;

    for (int i=0; i<T; ++i)
    {
		string S;
		int K;
		cin >> S >> K;
		cout << "Case #" << (i+1) << ": ";
		int times = min_times(S,K);
		if (times < IMPOSSIBLE)
			cout << times << '\n';
		else
			cout << "IMPOSSIBLE\n";
    }
}
