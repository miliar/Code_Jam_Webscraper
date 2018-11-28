#include <bits/stdc++.h>

#define rep(i, n) for(ll i=0; i<n; i++)
#define all(x) x.begin(),x.end()
#define pb push_back
#define xx first
#define yy second
#define mp make_pair
#define mod 1000000007
#define st string
#define vi vector<int>
#define vs vector<st>
#define mii map<int,int>
#define pii pair<int,int>
#define vpii vector<pii>

typedef long long ll;
typedef unsigned long long ull;

using namespace std;



int main() {
	int t;
	cin>>t;
	for(int j=0; j<t; j++) {
		int N, R, O, Y, G, B, V;
		cin>>N>>R>>O>>Y>>G>>B>>V;

		// set<int> Rset, Yset, Bset;
		// int h = 1;
		// rep(i, R) {
		// 	Rset.insert(h++);
		// }

		// rep(i, O) {
		// 	Rset.insert(h);
		// 	Yset.insert(h++);
		// }

		// rep(i, Y) {
		// 	Yset.insert(h++);
		// }

		// rep(i, G) {
		// 	Yset.insert(h);
		// 	Bset.insert(h++);
		// }

		// rep(i, B) {
		// 	Bset.insert(h++);
		// }

		// rep(i, V) {
		// 	Rset.insert(h);
		// 	Bset.insert(h++);
		// }

		char a[N+1];
		rep(i, N)
			a[i] = '*';
		a[N] = '\0';
		float ma = ceil((float)N/2);
		if(R > ma || B > ma || Y > ma) {
			printf("Case #%d: IMPOSSIBLE\n", j+1);
			continue;
		}
		if(R >= B && R >= Y) {
			int st = 0;
			rep(i, R) {
				a[st] = 'R';
				st = (st + 2)%N;
			}
			if(B >= Y) {
				st = (st - 1)%N;
				rep(i, B) {
					while(a[st] != '*' || a[(st-1)%N] == 'B') {
						st = (st+1)%N;
					}
					a[st] = 'B';
				}

				rep(i, Y) {
					while(a[st] != '*' || a[(st-1)%N] == 'Y') {
						st = (st+1)%N;
					}
					a[st] = 'Y';
				}
			}
			else {
				st = (st - 1)%N;
				rep(i, Y) {
					while(a[st] != '*' || a[(st-1)%N] == 'Y') {
						st = (st+1)%N;
					}
					a[st] = 'Y';
				}

				rep(i, B) {
					while(a[st] != '*' || a[(st-1)%N] == 'B') {
						st = (st+1)%N;
					}
					a[st] = 'B';
				}
			}
		}
		else if(B >= R && B >= Y) {
			int st = 0;
			rep(i, B) {
				a[st] = 'B';
				st = (st + 2)%N;
			}
			if(R >= Y) {
				st = (st - 1)%N;
				rep(i, R) {
					while(a[st] != '*' || a[(st-1)%N] == 'R') {
						st = (st+1)%N;
					}
					a[st] = 'R';
				}

				rep(i, Y) {
					while(a[st] != '*' || a[(st-1)%N] == 'Y') {
						st = (st+1)%N;
					}
					a[st] = 'Y';
				}
			}
			else {
				st = (st - 1)%N;
				rep(i, Y) {
					while(a[st] != '*' || a[(st-1)%N] == 'Y') {
						st = (st+1)%N;
					}
					a[st] = 'Y';
				}

				rep(i, R) {
					while(a[st] != '*' || a[(st-1)%N] == 'R') {
						st = (st+1)%N;
					}
					a[st] = 'R';
				}
			}
		}
		else {
			int st = 0;
			rep(i, Y) {
				a[st] = 'Y';
				st = (st + 2)%N;
			}
			if(B >= R) {
				st = (st - 1)%N;
				rep(i, B) {
					while(a[st] != '*' || a[(st-1)%N] == 'B') {
						st = (st+1)%N;
					}
					a[st] = 'B';
				}

				rep(i, R) {
					while(a[st] != '*' || a[(st-1)%N] == 'R') {
						st = (st+1)%N;
					}
					a[st] = 'R';
				}
			}
			else {
				st = (st - 1)%N;
				rep(i, R) {
					while(a[st] != '*' || a[(st-1)%N] == 'R') {
						st = (st+1)%N;
					}
					a[st] = 'R';
				}

				rep(i, B) {
					while(a[st] != '*' || a[(st-1)%N] == 'B') {
						st = (st+1)%N;
					}
					a[st] = 'B';
				}
			}
		}

		int flag = 0;
		for(int i=0; i<N; i++) {
			if(a[i] == a[(i+1)%N]) {
				flag = 1;
				break;
			}
		}

		if(flag) {
			printf("Case #%d: IMPOSSIBLE\n", j+1);
		}
		else {
			printf("Case #%d: %s\n", j+1, a);
		}
	}
	return 0;
}