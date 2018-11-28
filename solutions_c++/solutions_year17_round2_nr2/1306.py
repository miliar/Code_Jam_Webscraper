#include <iostream>
#include <cstdio>
#include <string>
#include <array>
#include <list>
#include <utility>
#include <algorithm>
using namespace std;

enum Color {
	R,
	O,
	Y,
	G,
	B,
	V,
	COUNT
};

static vector<list<int>> CanNear = {
	{G, Y, B},	//R
	{B},		//O
	{V, B, R},	//Y
	{R},		//G
	{O, R, Y},	//B
	{Y},		//V
};

constexpr auto ColorText = "ROYGBV";

bool Solve3(int N, array<int, COUNT> &U, vector<int> &Ans) {
	if (N == Ans.size()) {
		return Ans.front() != Ans.back();
	}

	if (N - Ans.size() < 10) {
		for (int Try : CanNear[Ans.back()]) {
			if (U[Try] == 0){
				continue;
			}

			U[Try]--;
			Ans.push_back(Try);
			if (true == Solve3(N, U, Ans)) {
				return true;
			}
			Ans.pop_back();
			U[Try]++;
		}

		return false;
	}

	if (Ans.back() != Ans.front() && U[Ans.front()] != 0) {
		U[Ans.front()]--;
		Ans.push_back(Ans.front());
		return Solve3(N, U, Ans);
	}

	int Next = CanNear[Ans.back()].front();

	for (int Try : CanNear[Ans.back()]) {
		if (U[Try] > U[Next]) {
			Next = Try;
		}
	}

	if (U[Next] == 0) {
		return false;
	} else {
		U[Next]--;
		Ans.push_back(Next);
		return Solve3(N, U, Ans);
	}
}

bool Solve(int N, array<int, COUNT> &U, vector<int> &Ans) {
	if (U[O] == 0 && U[G] == 0 && U[V] == 0) {
		return Solve3(N, U, Ans);
	}

	return false;
}

int main() {
	int T;
	cin >> T;

	for (int i = 1; i <= T; i++) {
		int N;
		array<int, COUNT> U;

		cin >> N >> U[R] >> U[O] >> U[Y] >> U[G] >> U[B] >> U[V];

		int MaxIndex = 0;
		for (int i = 0; i < U.size(); i += 2) {
			if (U[i] > U[MaxIndex]) {
				MaxIndex = i;
			}
		}
		if (U[MaxIndex] == 0) {
			for (int i = 1; i < U.size(); i += 2) {
				if (U[i] > U[MaxIndex]) {
					MaxIndex = i;
				}
			}
		}

		vector<int> Ans;
		Ans.reserve(N);

		U[MaxIndex]--;
		Ans.push_back(MaxIndex);
		bool Able = Solve(N, U, Ans);

		if (Able) {
			cout << "Case #" << i << ": ";
			for (int Color : Ans) {
				cout << ColorText[Color];
			}
			cout << "\n";
		} else {
			cout << "Case #" << i << ": " << "IMPOSSIBLE" << "\n";
		}
	}
	return 0;
}
