#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string>
#include <algorithm>
#include <map>
#include <set>
#include <queue>

using namespace std;

typedef long long ll;

struct state {
	ll H1, A1, H2, A2, len;
	state(ll a, ll b, ll c, ll d, ll e) {
		H1 = a;
		A1 = b;
		H2 = c;
		A2 = d;
		len = e;
	}
	string getstring() {
		return to_string(H1) + "-" + to_string(A1) + "-" + to_string(H2) + "-" + to_string(A2);
	}
};

int main() {
	int T;
	cin >> T;
	for (int t=1;t<=T;t++) {
		ll H1, A1, H2, A2, B, D, origH;
		cin >> H1 >> A1 >> H2 >> A2 >> B >> D;
		origH = H1;
		queue<state> Q;
		map<string, int> MP;

		state st = state(H1, A1, H2, A2, 0);
		Q.push(st);
		string s = st.getstring();

		MP[s] = 1;

		ll ans = -1;
		while (!Q.empty()) {
			state cur = Q.front();
			Q.pop();

			H1 = cur.H1;
			A1 = cur.A1;
			H2 = cur.H2;
			A2 = cur.A2;
			ll len = cur.len;

			//cout << "CURRENT: " + cur.getstring() << "\tLENGTH: " << len <<endl;

			if (H2 - A1 <= 0) {
				ans = len+1;
				break;
			}

			state temp = state(H1-A2, A1, H2-A1, A2, len+1); // attack
			if (temp.H1 > 0) {
				s = temp.getstring();
				//cout << "ATTACK: " + s << endl;
				if (MP[s] == 0) {
					MP[s] = 1;
					Q.push(temp);
				}
			}
			temp = state(H1-A2, A1+B, H2, A2, len+1); // buff
			if (temp.H1 > 0) {
				s = temp.getstring();
				//cout << "BUFF: " + s << endl;
				if (MP[s] == 0) {
					MP[s] = 1;
					Q.push(temp);
				}
			}
			temp = state(H1-max(0LL,A2-D), A1, H2, max(0LL, A2-D), len+1); // debuff
			if (temp.H1 > 0) {
				s = temp.getstring();
				//cout << "DEBUFF: " + s << endl;
				if (MP[s] == 0) {
					MP[s] = 1;
					Q.push(temp);
				}
			}
			temp = state(origH-A2, A1, H2, A2, len+1); //cure
			if (temp.H1 > 0) {
				s = temp.getstring();
				//cout << "CURE: " + s << endl << endl;
				if (MP[s] == 0) {
					MP[s] = 1;
					Q.push(temp);
				}
			}

		}
		if (ans > 0) printf("Case #%d: %lld\n", t, ans);
		else printf("Case #%d: IMPOSSIBLE\n", t);
	}
}