#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <map>
#include <algorithm>
#include <utility>
#include <cstring>
using namespace std;

int t;

string genBO(int O)
{
	string BO(O + O, 'O');
	for (int i = 0; i < O; ++i) {
		BO[2 * i] = 'B';
	}
	return BO;
}

string genRG(int G)
{
	string RG(G + G, 'G');
	for (int i = 0; i < G; ++i) {
		RG[2 * i] = 'R';
	}
	return RG;
}

string genYV(int V)
{
	string YV(V + V, 'V');
	for (int i = 0; i < V; ++i) {
		YV[2 * i] = 'Y';
	}
	return YV;
}

void setR(string& S, int& id, int R)
{
	for (int i = 0; i < R; ++i) {
		S[id] = 'R';
		id += 2;
		if (id >= int(S.size())) {
			id = 1;
		}
	}
}

void setY(string& S, int& id, int Y)
{
	for (int i = 0; i < Y; ++i) {
		S[id] = 'Y';
		id += 2;
		if (id >= int(S.size())) {
			id = 1;
		}
	}
}

void setB(string& S, int& id, int B)
{
	for (int i = 0; i < B; ++i) {
		S[id] = 'B';
		id += 2;
		if (id >= int(S.size())) {
			id = 1;
		}
	}
}

int main()
{
	scanf("%d", &t);
	for (int ti = 0; ti < t; ++ti) {
		int N, R, O, Y, G, B, V;
		scanf("%d%d%d%d%d%d%d", &N, &R, &O, &Y, &G, &B, &V);
		if (B == O && B + O == N) {
			printf("Case #%d: %s\n", ti+1, genBO(O).data());
			continue;
		}
		if (R == G && R + G == N) {
			printf("Case #%d: %s\n", ti+1, genRG(G).data());
			continue;
		}
		if (Y == V && Y + V == N) {
			printf("Case #%d: %s\n", ti+1, genYV(V).data());
			continue;
		}
		B -= O;
		R -= G;
		Y -= V;
		if (B < 0 || R < 0 || Y < 0 || (O > 0 && B <= 0) || (G > 0 && R <= 0) || (V > 0 && Y <= 0)) {
			printf("Case #%d: IMPOSSIBLE\n", ti+1);
			continue;
		}
		int N2 = (R + Y + B) / 2;
		if (R > N2 || Y > N2 || B > N2) {
			printf("Case #%d: IMPOSSIBLE\n", ti+1);
			continue;
		}
		string S(R + Y + B, ' ');
		int id = 0;
		if (R >= Y && R >= B) {
			setR(S, id, R);
			setY(S, id, Y);
			setB(S, id, B);
		} else if (Y >= R && Y >= B) {
			setY(S, id, Y);
			setR(S, id, R);
			setB(S, id, B);
		} else {
			setB(S, id, B);
			setR(S, id, R);
			setY(S, id, Y);
		}
		if (O > 0) {
			S.insert(S.find('B'), genBO(O));
		}
		if (G > 0) {
			S.insert(S.find('R'), genRG(G));
		}
		if (V > 0) {
			S.insert(S.find('Y'), genYV(V));
		}
		printf("Case #%d: %s\n", ti+1, S.data());
	}
	return 0;
}

/* vim: set ts=4 sw=4 noet: */
