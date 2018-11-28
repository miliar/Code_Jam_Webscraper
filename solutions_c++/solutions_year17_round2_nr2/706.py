#include <bits/stdc++.h>
using namespace std;

const int maxN = 1e3+100;

int n, k;
int m;
int a[6];
const char colors[] = {'R', 'O', 'Y', 'G', 'B', 'V'};
int result[maxN];
int cs[maxN];
int Os, Vs, Gs;

bool check() {
	if (a[1] + a[3] + a[5] > 0) 
		return false;
	m = a[0] + a[2] + a[4];
	if (m == 0 && ((Os>0 && Vs>0) || (Os>0 && Gs>0) || (Gs>0 &&Vs>0)))
		return false;

	for(int i=0; i<3; i++) cs[i] = i*2;
	for(int i=0; i<3; i++)
		for(int j=0; j<i; j++)
			if (a[cs[j]] > a[cs[j+1]])
				swap(cs[j], cs[j+1]);

	// for(int i=0; i<3; i++)
		// printf("%d\n", cs[i]);

	memset(result, 255, sizeof(result));
	for(int i=0; i<m; i+=2) {
		for(int j=0; j<3; j+=1)
			if (a[cs[j]]>0) {
				--a[cs[j]];
				result[i] = cs[j];
				break;
			}
	}
	for(int i=1; i<m; i+=2) {
		for(int j=0; j<3; j+=1)
			if (a[cs[j]]>0) {
				--a[cs[j]];
				result[i] = cs[j];
				break;
			}
	}

	// for(int i=0; i<m; i++) 
	// 	printf("%c -- ", colors[result[i]]);

	for(int i=1; i<m; i++)
		if (result[i] == result[i-1])
			return false;
	if (result[0] == result[m-1]) 
		return false;
	return true;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int test;
	cin >> test;
	for(int dem = 1; dem <= test; dem++) {
		cin >> n;
		for(int i=0; i<6; i++) {
			scanf("%d", &a[i]);
		}
		Os = min(a[1], a[4]);
		a[1] -= Os;
		a[4] -= Os;
		Gs = min(a[3], a[0]);
		a[3] -= Gs;
		a[0] -= Gs;
		Vs = min(a[5], a[2]);
		a[5] -= Vs;
		a[2] -= Vs;
		if (check()) {
			printf("Case #%d: ", dem);
			// cout << m;
			for(int i=0; i<m; i++) {
				printf("%c", colors[result[i]]);
				if (result[i] == 0)
					while ((Gs>0)) {
						printf("GR");
						Gs--;
					}
				if (result[i] == 2) 
					while (Vs>0) {
						printf("VY");
						Vs--;
					}
				if (result[i] == 4) 
					while (Os>0) {
						printf("OB");
						Os--;
					}
			}
			while (Os>0) {
				printf("OB");
				Os--;
			}
			while (Gs>0) {
				printf("GR");
				Gs--;
			}
			while (Vs>0) {
				printf("VY");
				Vs--;
			}
			cout << endl;
		} else {
			printf("Case #%d: IMPOSSIBLE\n", dem);
		}
	}
	fclose(stdin);
	fclose(stdout);
}