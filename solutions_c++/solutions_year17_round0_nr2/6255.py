#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;

int len;

int found ( char *s ) {
	for ( int i = len - 1; i >= 0; i -- ) {
		for ( int j = i - 1; j >= 0; j -- ) {
			if ( s[j] > s[i] ) {
				return i;
			}
		}
	}
	return -1;
}

void substract ( char *s, int p ) {
	while ( p >= 0 ) {
		if ( s[p] == '0' ) {
			s[p] = '9';
			p --;
		}
		else {
			s[p] --;
			break;
		}
	}
}

void full ( char *s, int p ) {
	for ( int i = p + 1; i < len; i ++ ) {
		s[i] = '9';
	}
}

long long solve ( char *s ) {
	while ( true ) {
		int p = found (s);
		if ( p == -1 ) {
			break;
		}
		substract ( s, p );
		full (s, p);
	}

	long long ans = 0;
	long long ten = 1;
	for ( int i = len - 1; i >= 0; i -- ) {
		ans = ans + ( s[i] - '0' ) * ten;
		ten *= 10;
	}
	return ans;
}

char s[100];

int main (  ) {
	int T;
	scanf ("%d", &T);
	for ( int kase = 1; kase <= T; kase ++ ) {
		cin >> s;
		len = (int) strlen(s);
		cout << "Case #" << kase << ": " <<  solve ( s ) << endl;
	}
	return 0;
}