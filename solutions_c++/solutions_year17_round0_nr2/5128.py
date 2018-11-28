#include<stdio.h>
#include<math.h>
#include<string.h>
#include<stdlib.h>
 
#include<iostream>
#include<vector>
#include<map>
#include<string>
#include<set>
#include<queue>
#include<stack>
#include<algorithm>
using namespace std;
 
#define fori(a,b) for(i = a; i <= b; i++)
#define forj(a,b) for(j = a; j <= b; j++)
#define fork(a,b) for(k = a; k <= b; k++)
#define scani(a) scanf("%d",&a);
#define scanlli(a) scanf("%lld", &a);
#define scanc(c) scanf("%c",&c);
#define scans(s) scanf("%s", s);
#define mp(a,b) make_pair(a, b)
#define ll(a) (long long int)(a)
#define vi vector<int>
#define vc vector<char>
#define vs vector<string>
#define println printf("\n");
#define sz(v) v.size()
#define len(s) s.length()
#define max(a,b) ((a > b) ? a : b)
#define min(a,b) ((a < b) ? a : b)

int main () {
	int t, te; 
	long long int n;
	scani(t)
	for (int te = 1; te <= t; te++) {
		scanlli(n)
		int arr[20] = {0};
		long long int temp = n;
		int index = 0;
		while (temp > 0) {
			int d = temp % 10; 
			arr[index] = d;
			index++;
			temp = temp / 10; 
		}
		int len = index;
		for (int i = 0, j = len-1; i < j; i++, j--) {
			int tmp = arr[i];  
			arr[i] = arr[j];
			arr[j] = tmp;
		}
		bool tidy = false;
		while (!tidy) {
			tidy = true;
			for (int i = 1; i < len; i++) {
				if (arr[i] < arr[i-1]) {
					tidy = false;
					for (int j = i; j < len; j++) {
						arr[j] = 9;
					}
					int k = i-1;
					bool borrow = false;
					while (k >= 0) {
						if (arr[k] > 1) {
							arr[k]--;
							borrow = false;
							break;
						}
						borrow = true;
						arr[k] = 9;
						k--;
					}
					if (borrow) {
						arr[0] = 0;
					}
				}
			}
		}
		long long int res = 0LL;
		for (int i = 0; i < len; i++) {
			res = res * 10 + arr[i];
		}
		printf("Case #%d: %lld\n", te, res);
	}
	return 0;
}