#include <stdio.h>
#include <stack>
#include <map>
#include <string.h>
#include <string>
#include <iostream>
#include <algorithm>
#include <iomanip>
#include <math.h>
#include <vector>
#include <set>
#include <queue>
#include <fstream>
using namespace std;
#define ll long long
#define mp make_pair
#define pb push_back
//#define ld long double
const double sn = 1e-6;
int t;
int main() {
	freopen("A-large.in","r",stdin);
	freopen("alarge.out", "w", stdout);
	scanf("%d", &t);
	for (int q = 1; q <= t; q++) {
		char arr[1005];
		int k;
		scanf("%s%d", arr, &k);
		int sz = strlen(arr);
		int res = 0;
		for (int i = 0; i < sz-k+1; i++) {
			if (arr[i] == '-') {
				res++;
				for (int j = 0; j < k; j++) {
					arr[i + j] = (arr[i + j] == '-' ? '+' : '-');
				}
			}
		}
		bool nv = false;
		for (int i = 0; i < sz; i++) {
			if (arr[i] == '-') {
				nv = true;
				break;
			}
		}
		printf("Case #%d: ", q);
		if (nv)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n", res);
	}
	return 0;
}