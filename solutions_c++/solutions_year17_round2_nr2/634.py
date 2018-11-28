#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

pair<int, char> a[10];
char S[100000];

bool find(int A, int B, int C) {
	a[1] = make_pair(A,'R');
	a[2] = make_pair(B,'Y');
	a[3] = make_pair(C,'B');
	sort(a + 1,a + 4);
	C = a[1].first;
	B = a[2].first;
	A = a[3].first;
	//cout<<A<<B<<C<<endl;
	if (A > B + C) return false;
	int n = A + B + C;
	
	for (int i = 0; i < A * 2; i += 2) {
		S[i] = a[3].second;
	}
	for (int i = 1; i < A * 2; i += 2) {
		if (B > C) 
		{
			S[i] = a[2].second;
			B--;
		}
		else 
		{
			S[i] = a[1].second;
			C--;
		}
	}
	for (int i = A * 2; i < n; ++i) {
		if (B > C) 
		{
			S[i] = a[2].second;
			B--;
		}
		else 
		{
			S[i] = a[1].second;
			C--;
		}
	}
	return true;
}

int main() {
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);
	int T;
	scanf("%d", &T);
	for (int cas = 1; cas <= T; ++cas) {
		int n,A,B,C,D,E,F;
		scanf("%d%d%d%d%d%d%d", &n, &A, &B, &C, &D, &E, &F);
		printf("Case #%d: ", cas);
		if (A <= D && A != 0) 
		{
			if (n != A + D) puts("IMPOSSIBLE");
			else 
			{
				for (int i = 1; i <= A; ++i) printf("RG");
				puts("");
			}
			continue;
		}
		else A -= D;
		if (C <= F && C != 0) 
		{
			if (n != C + F) puts("IMPOSSIBLE");
			else 
			{
				for (int i = 1; i <= C; ++i) printf("VY");
				puts("");
			}
			continue;
		}
		else C -= F;
		if (E <= B && E != 0) 
		{
			if (n != E + B) puts("IMPOSSIBLE");
			else 
			{
				for (int i = 1; i <= E; ++i) printf("OB");
				puts("");
			}
			continue;
		}
		else E -= B;
		if (!find(A, C, E)) 
		{
			puts("IMPOSSIBLE");
			continue;
		}
		bool flag1 = false;
		bool flag2 = false;
		bool flag3 = false;
		int len = A + C + E;
		for (int i = 0; i < len; ++i) {
			printf("%c", S[i]);
			if (!flag1 && S[i] == 'R') {
				flag1 = true;
				for (int j = 1; j <= D; ++j) {
					printf("GR");
				}
			}
			if (!flag2 && S[i] == 'Y') {
				flag2 = true;
				for (int j = 1; j <= F; ++j) {
					printf("VY");
				}
			}
			if (!flag3 && S[i] == 'B') {
				flag3 = true;
				for (int j = 1; j <= B; ++j) {
					printf("OB");
				}
			}
		}
		puts("");
	} 
	return 0;
} 
