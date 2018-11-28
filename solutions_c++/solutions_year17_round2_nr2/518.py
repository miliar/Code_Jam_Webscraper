#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <queue>
#include <cstring>
#include <string>
#include <sstream>
#include <vector>
#define ffor(_a,_f,_t) for(int _a=(_f),__t=(_t);_a<__t;_a++)
#define all(_v) (_v).begin() , (_v).end()
#define sz size()
#define pb push_back
#define SET(__set, val) memset(__set, val, sizeof(__set))
#define FOR(__i, __n) ffor (__i, 0, __n)
#define syso system("pause")
#define mp make_pair

using namespace std;

int main() {
  freopen("Bs.out","wt", stdout);
  freopen("Bs.in","r", stdin);
  int tests;
  cin >> tests;
  scanf("\n");
  
  FOR (test, tests){
    cout << "Case #" << (test + 1) << ": ";
    int N, R, O, Y, G, B, V;
    cin >> N >> R >> O >> Y >> G >> B >> V;
    if (R <= N / 2 && B <= N / 2 && Y <= N / 2) {
    	string ret;
    	FOR (i, N)
				ret = ret + " ";
    	FOR (i, R)
				ret[2 * i] = 'R';
			char ch1 = 'B', ch2 = 'Y';
			int left1 = B, left2 = Y;
			if (left1 < left2) {
				swap(left1, left2);
				swap(ch1, ch2);
			}
			int pos = 2 * R - 1;
			if (pos < 0)
				pos = 0;
			int left = (N - pos + 1) / 2;
			while (left) {
				if (left1) {
					ret[pos] = ch1;
					left1--;
				}
				else {
					ret[pos] = ch2;
					left2--;
				}
				pos += 2;
				left--;
			}
			while (left1 || left2) {
				FOR (i, N)
					if (ret[i] == ' ') {
						pos = i;
						break;
					}
				if (left1) {
					ret[pos] = ch1;
					left1--;
				}
				else {
					ret[pos] = ch2;
					left2--;
				}
			}
			cout << ret;
		}
		else
			cout << "IMPOSSIBLE";
    cout << "\n";
  }
  return 0;
}
