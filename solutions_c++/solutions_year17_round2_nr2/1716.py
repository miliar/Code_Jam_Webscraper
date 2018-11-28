#include <bits/stdc++.h>
#include <fstream>
#define rep(i, n) for(ll i=0; i<n; i++)
#define all(x) x.begin(),x.end()
#define pb push_back
#define xx first
#define yy second
#define mp madke_pair
#define mod 1000000007
#define st string
#define vi vector<int>
#define vs vector<st>
#define mii madp<int,int>
#define pii pair<int,int>
#define vpii vector<pii>

typedef long long ll;
typedef unsigned long long ull;

using namespace std;

int main() {
	int t;
	cin>>t;
  ofstream myfile;
 myfile.open ("stable.txt");
	for(int j=0; j<t; j++) {
		int N, r, O, y, G, B, V;
		cin>>N>>r>>O>>y>>G>>B>>V;

		char a[N+1];
		rep(i, N)
			a[i] = '*';
		a[N] = '\0';
		float mad = ceil((float)N/2);
		if(r > mad || B > mad || y > mad) {
			//printf("Case #%d: IMPOSSIBLE\n", j+1);
      myfile<<"Case #"<<j+1<<": IMPOSSIBLE\n";
			continue;
		}
		if(r >= B && r >= y) {
			int st = 0;
			rep(i, r) {
				a[st] = 'R';
				st = (st + 2)%N;
			}
			if(B >= y) {
				st = (st - 1)%N;
				rep(i, B) {
					while(a[st] != '*' || a[(st-1)%N] == 'B') {
						st = (st+1)%N;
					}
					a[st] = 'B';
				}

				rep(i, y) {
					while(a[st] != '*' || a[(st-1)%N] == 'Y') {
						st = (st+1)%N;
					}
					a[st] = 'Y';
				}
			}
			else {
				st = (st - 1)%N;
				rep(i, y) {
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
		else if(B >= r && B >= y) {
			int st = 0;
			rep(i, B) {
				a[st] = 'B';
				st = (st + 2)%N;
			}
			if(r >= y) {
				st = (st - 1)%N;
				rep(i, r) {
					while(a[st] != '*' || a[(st-1)%N] == 'R') {
						st = (st+1)%N;
					}
					a[st] = 'R';
				}

				rep(i, y) {
					while(a[st] != '*' || a[(st-1)%N] == 'Y') {
						st = (st+1)%N;
					}
					a[st] = 'Y';
				}
			}
			else {
				st = (st - 1)%N;
				rep(i, y) {
					while(a[st] != '*' || a[(st-1)%N] == 'Y') {
						st = (st+1)%N;
					}
					a[st] = 'Y';
				}

				rep(i, r) {
					while(a[st] != '*' || a[(st-1)%N] == 'R') {
						st = (st+1)%N;
					}
					a[st] = 'R';
				}
			}
		}
		else {
			int st = 0;
			rep(i, y) {
				a[st] = 'Y';
				st = (st + 2)%N;
			}
			if(B >= r) {
				st = (st - 1)%N;
				rep(i, B) {
					while(a[st] != '*' || a[(st-1)%N] == 'B') {
						st = (st+1)%N;
					}
					a[st] = 'B';
				}

				rep(i, r) {
					while(a[st] != '*' || a[(st-1)%N] == 'R') {
						st = (st+1)%N;
					}
					a[st] = 'R';
				}
			}
			else {
				st = (st - 1)%N;
				rep(i, r) {
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
			myfile<<"Case #"<<j+1<<": IMPOSSIBLE\n";
		}
		else {
			myfile<<"Case #"<<j+1<<": "<<a<<"\n";
		}
	}
	return 0;
}
