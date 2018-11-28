#include <cstdio>
#include <algorithm>
#include <cstring>
#include <vector>
#include <map>
#include <string>
#include <iostream>

using namespace std;

const int Maxn = 1100;

int R, O, Y, G, B, V;
int N;
int T;
string RR, BB, YY;
string ans;
bool flag;

void reduceG() {
	if (R == G) {
		if (R + G != N) {
			flag = false;
		}
		else {
			RR = "";
			for (int i=0;i<R;++i)
				RR = RR + "RG";
			R = 1; G = 0;
		}
	}
	else if (R < G) {
		flag = false;
	}
	else {
		RR = "R";
		for (int i=0;i<G;++i)
			RR = RR + "GR";
		R -= G;
		G = 0;
	}
}

void reduceO() {
	if (B == O) {
		if (B + O != N) {
			flag = false;
		}
		else {
			BB = "";
			for (int i=0;i<B;++i)
				BB = BB + "BO";
			B = 1; O = 0;
		}
	}
	else if (B < O) {
		flag = false;
	}
	else {
		BB = "B";
		for (int i=0;i<O;++i)
			BB = BB + "OB";
		B -= O;
		O = 0;
	}
}

void reduceV() {
	if (Y == V) {
		if (Y + V != N) {
			flag = false;
		}
		else {
			YY = "";
			for (int i=0;i<Y;++i)
				YY = YY + "YV";
			Y = 1; V = 0;
		}
	}
	else if (Y < V) {
		flag = false;
	}
	else {
		YY = "Y";
		for (int i=0;i<V;++i)
			YY = YY + "VY";
		Y -= V;
		V = 0;
	}
}

bool append_ans(int &xx, char ch) {
	if (ch == 'R') {
		if (ans.size() > 0 && RR.size() > 0 && ans[ans.size() - 1] == RR[0])
			return false;
		ans = ans + RR;
		RR = "R";
	}
	if (ch == 'B') {
		if (ans.size() > 0 && BB.size() > 0 && ans[ans.size() - 1] == BB[0])
			return false;
		ans = ans + BB;
		BB = "B";
	}
	if (ch == 'Y') {
		if (ans.size() > 0 && YY.size() > 0 && ans[ans.size() - 1] == YY[0])
			return false;
		ans = ans + YY;
		YY = "Y";
	}
	--xx;
	return true;
}

void doRBY() {
	//printf("doRBY() : %d %d %d\n", R, B, Y);
	N = R + B + Y;
	if (N > 1 && (R > B + Y || B > R + Y || Y > R + B)) {
		flag = false;
		return;
	}	
	int x, y, z;
	char chx, chy, chz;
	if (R <= B && R <= Y) {
		x = R; chx = 'R';
		y = B; chy = 'B';
		z = Y; chz = 'Y';
	}
	else if (B <= R && B <= Y) {
		x = B; chx = 'B';
		y = R; chy = 'R';
		z = Y; chz = 'Y';
	}
	else {
		x = Y; chx = 'Y';
		y = B; chy = 'B';
		z = R; chz = 'R';
	}

	//printf("%d %d %d %c %c %c\n", x, y, z, chx, chy, chz);
	ans = "";
	for (;x > 0;) {
		if (y > z) {
			append_ans(x, chx);
			append_ans(y, chy);
		}
		else {
			append_ans(x, chx);
			append_ans(z, chz);
		}
	}
	for (;y > 0 || z > 0;) {
		if (y > z) append_ans(y, chy);
		else {
			if (!append_ans(z, chz)) {
				append_ans(y, chy);
			}
		}
	}
}

int main() {
	freopen("B-small-attempt1.in.txt", "r", stdin);
	freopen("B-small.out", "w", stdout);

	scanf("%d", &T);
	for (int ii=1;ii<=T;++ii) {
		printf("Case #%d: ", ii);

		scanf("%d %d %d %d %d %d %d", &N, &R, &O, &Y, &G, &B, &V);

		flag = true;
		RR = BB = YY = "";
		if (R > 0) RR = "R";
		if (B > 0) BB = "B";
		if (Y > 0) YY = "Y";

		if (G > 0) 
			reduceG();
		if (!flag) {
			printf("IMPOSSIBLE\n");
			continue;
		}
		if (O > 0)
			reduceO();
		if (!flag) {
			printf("IMPOSSIBLE\n");
			continue;
		}
		if (V > 0)
			reduceV();
		if (!flag) {
			printf("IMPOSSIBLE\n");
			continue;
		}
		doRBY();
		if (!flag) {
			printf("IMPOSSIBLE\n");
			continue;
		}
		else {
			printf("%s\n", ans.c_str());
			for (int i=1;i<ans.size();++i)
				if (ans[i] == ans[i - 1]) {
					cerr << ii << " : wrong" << endl;
				}
		}
	}
}