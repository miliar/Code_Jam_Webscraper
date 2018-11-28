#include<bits/stdc++.h>
#define rep(i, a, b) for(int i = a; i <= b; i++)
#define ll long long
#define ms(x, y) memset(x, y ,sizeof(x))
using namespace std;

void output(ll tmp) {
	if(tmp % 2 == 1)
		cout << tmp / 2 << ' ' << tmp / 2 << endl;
	else
		cout << tmp / 2 << ' ' << tmp / 2 - 1 << endl;
}

ll n[2000], m[2000];
ll k;
int main () {
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	int tc;
	cin >> tc;
	rep(tt, 1, tc) {
		cin >> n[1] >> k;
		m[1] = 1;
		n[2] = m[2] = 0;
		printf("Case #%d: ", tt);
		for(int i = 1;; i += 2) {
			k -= m[i+1];
			if(k <= 0) {
				output(n[i+1]);
				break;
			}
			k -= m[i];
			if(k <= 0) {
				output(n[i]);
				break;
			}
			if(n[i] % 2 == 0 && n[i+1] % 2 == 0) {
				if(m[i+1] != 0)
					printf("ERROR");				
			}
			if(n[i] % 2 == 1 && n[i+1] % 2 == 1) {
				if(m[i+1] != 0)
					printf("ERROR");				
			}
			else if(n[i] % 2 == 0) {
				n[i+2] = n[i] / 2 - 1;
				n[i+3] = n[i] / 2;
				m[i+2] = m[i];
				m[i+3] = m[i] + 2 * m[i+1];
			}
			else if(n[i] % 2 == 1) {
				n[i+2] = n[i] / 2;
				n[i+3] = n[i] / 2 + 1;
				m[i+2] = m[i] * 2 + m[i+1];
				m[i+3] = m[i+1];
			}
		}
	}
	return 0;
}