#include<stdio.h>
#include<bits/stdc++.h>
using namespace std;
typedef long long LL;

FILE *fin = fopen("in.txt", "r");
FILE *fout = fopen("out1.txt", "w");

LL cnt = 0;	
LL arr[4686828];
void bt(int curr, LL val, int prev) {
	if (curr == 18) {
		arr[cnt++] = val; 
		return;
	}
	for (int i = prev; i <= 9; i++) {
		bt(curr + 1, val * 10 + i, i);
	}
}
int main() {  
	
	bt(0, 0, 0);
	
	int TC = 0;
	LL val;
	fscanf(fin, "%d", &TC);
	for (int t = 0; t < TC; t++) {
		fscanf(fin, "%I64d", &val);
		LL lo = 0, hi = cnt - 1, ans;
		while (lo <= hi) {
			LL mid = lo + (hi - lo) / 2;
			if (arr[mid] <= val) {
				ans = mid;
				lo = mid + 1;
			}
			else {
				hi = mid - 1;
			}
		}
		fprintf(fout, "Case #%d: %I64d\n", t + 1, arr[ans]);
	}
  	return 0;
}
