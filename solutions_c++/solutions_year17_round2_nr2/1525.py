#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <array>
#include <tuple>

#define ll long long
#define ull unsigned long long
#define FOR(n) for(long long i = 0; i < n; i++)
#define DFOR(n) for(long long i = n - 1; i >= 0; i--)

using namespace std;

int N, R, O, Y, G, B, V, r, y, b;

bool impossible() {
	//cout << y << " " << bool(r > N / 2 || y > N / 2 || b > N / 2);
	return bool(r > N / 2 || y > N / 2 || b > N / 2);
}

int main() {
	int T;
	cin >> T;
	for(int temp_t = 0; temp_t < T; temp_t++) {
		cout << "Case #" << temp_t + 1 << ": ";
		ll D;
		cin >> N >> R >> O >> Y >> G >> B >> V;
		r = R + O + V;
		y = Y + O + G;
		b = B + V + G;
		if(impossible()) {
			cout << "IMPOSSIBLE\n";
			continue;
		}
		int A[N];
		if(r > y) {
		int rstop;
		for(long long i = 0; i < N; i = i + 2) {
			if(r > 0) {
				A[i] = 1;
				r--;
				if(r == 1) rstop = i + 2;
			}
			else {
				A[i] = 3;
				y--;
			}
		}
		/*for(long long i = 0; i < N && O > 0; i = i + 2) {
			if(A[i] == 1) {
				A[i] = 2;
				O--;
			}
		}
		for(long long i = rstop; i < N && i >= 0 && V > 0; i = i - 2) {
			if(A[i] == 1) {
				A[i] = 6;
				V--;
			}
		}*/
		int ystop = -1;
		for(long long i = 1; i < N; i = i + 2) {
			if(y > 0) {
				A[i] = 3;
				y--;
				if(y == 1) ystop = i + 2;
			}
			else {
				A[i] = 5;
				b--;
			}
		}/*
		for(long long i = 1; i < N && G > 0; i = i + 2) {
			if(A[i] == 3 || ((A[i + 1] == 1 || A[i + 1] == 6) && (A[i - 1] == 1 || A[i - 1] == 6))) {
				A[i] = 4;
				G--;
			}
		}
		for(long long i = ystop; i < N && i >= 0 && V > 0; i = i - 2) {
			if(A[i] == 1) {
				A[i] = 6;
				V--;
			}
		}*/
		}
		else {
		int ystop;
		for(long long i = 0; i < N; i = i + 2) {
			if(y > 0) {
				A[i] = 3;
				y--;
				if(y == 1) ystop = i + 2;
			}
			else {
				A[i] = 1;
				r--;
			}
		}/*
		for(long long i = 0; i < N && O > 0; i = i + 2) {
			if(A[i] == 1) {
				A[i] = 2;
				O--;
			}
		}
		for(long long i = rstop; i < N && i >= 0 && V > 0; i = i - 2) {
			if(A[i] == 1) {
				A[i] = 6;
				V--;
			}
		}*/
		int rstop = -1;
		for(long long i = 1; i < N; i = i + 2) {
			if(r > 0) {
				A[i] = 1;
				r--;
				if(r == 1) ystop = i + 2;
			}
			else {
				A[i] = 5;
				b--;
			}
		}/*
		for(long long i = 1; i < N && G > 0; i = i + 2) {
			if(A[i] == 3 || ((A[i + 1] == 1 || A[i + 1] == 6) && (A[i - 1] == 1 || A[i - 1] == 6))) {
				A[i] = 4;
				G--;
			}
		}
		for(long long i = ystop; i < N && i >= 0 && V > 0; i = i - 2) {
			if(A[i] == 1) {
				A[i] = 6;
				V--;
			}
		}*/
		}
		FOR(N) {
			switch(A[i]) {
				case 1: cout << "R"; break;
				case 2: cout << "O"; break;
				case 3: cout << "Y"; break;
				case 4: cout << "G"; break;
				case 5: cout << "B"; break;
				case 6: cout << "V"; break;
			}
		}
		cout << "\n";
	}
	return 0;
}