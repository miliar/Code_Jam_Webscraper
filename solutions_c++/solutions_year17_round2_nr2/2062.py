/*	In the name of God	*/
#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <cstring>
#include <cctype>
#include <string>
#include <algorithm>
#include <vector>
#include <iostream>
#include <sstream>
#include <bitset>
#include <map>
#include <set>
#include <queue>
#include <stack>

#define rep(i,n) for((i)=0;(i)<(n);(i)++)
typedef long long ll;

using namespace std;
int a[11],b[11];
char st[1101];
string m="ROYGBV";
int main() {
	int tc;
	int d, n, k, s;
	freopen("B-small-attempt4.in", "r", stdin);
	freopen("program.out", "w", stdout);
	cin >> tc;
	for (int ti = 0; ti < tc; ++ti) {
		cin >> n;
		for (int i = 0; i < 6; ++i) {
			cin >> a[i];
			b[i] = a[i];
		}
		bool f = 1;
		int x = 0;
		printf("Case #%d: ", ti + 1);
		for (int j = 0; j < 6; j += 2) {
			if (a[j] == a[(j + 3) % 6] && n == 2 * a[j]) {
				for (int i = 0; i < a[j]; ++i) {
					cout << m[j] << m[(j + 3) % 6];
				}
				cout << endl;
				f = 0;
			}
			a[j] -= a[(j + 3) % 6];
			x += a[j];
		}
		if (!f)
			continue;
		f = 1;
		for (int j = 0; j < 6; j++) {
			if (a[j] < 0) {
				f = 0;
			} else {
				if (a[j] && 2 * a[j] > x)
					f = 0;
			}
			j++;
			if (b[j] && b[j] >= b[(j + 3) % 6])
				f = 0;
		}
		if (!f) {
			printf("IMPOSSIBLE\n");
			continue;
		}
		int sc = 0;
		memset(st,0,sizeof st);
		
		int tmp = max(a[0], max(a[2], a[4]));
		for (int i = 0; i < 6; i+=2) {
			if (a[i]==tmp){
				for (int j = 0; j < 2*a[i]; j+=2) {
					st[j]=m[i];
				}
				a[i]=0;
				break;
			}
		}
		for (int i = 0; i < x; ++i) {
			if (st[i])
				continue;
			int j,tmp = max(a[0], max(a[2], a[4]));
			for (j = 0; j < 6; j+=2) {
				if (st[i]!=m[j] && a[j]==tmp){
					st[i]=m[j];
					a[j]--;
					break;
				}
			}
			if (j<6)
				continue;
			for (int j = 0; j < 6; j+=2) {
				if (st[i]!=m[j] && a[j]){
					st[i]=m[j];
					a[j]--;
					break;
				}
			}
		}
		
//		for (int i = 0; i < x; ++i) {
//			int j, tmp = max(a[0], max(a[2], a[4]));
//			for (j = 0; j < 6; j += 2) {
//				if ((!sc || st[sc - 1] != m[j]) && a[j] >= tmp) {
//					st[sc++] = m[j];
//					a[j]--;
//					for (int p = 0; p < a[(j + 3) % 6]; ++p) {
//						st[sc++] = m[(j + 3) % 6];
//						st[sc++] = m[j];
//					}
//					a[(j + 3) % 6] = 0;
//					break;
//				}
//			}
//			if (j<6)
//				continue;
//			for (j = 0; j < 6; j += 2) {
//				if (!sc || st[sc - 1] != m[j]) {
//					st[sc++] = m[j];
//					a[j]--;
//					for (int p = 0; p < a[(j + 3) % 6]; ++p) {
//						st[sc++] = m[(j + 3) % 6];
//						st[sc++] = m[j];
//					}
//					a[(j + 3) % 6] = 0;
//					break;
//				}
//			}
//		}
//
		
		cout << st << endl;
	}
	
	
	return 0;
}
