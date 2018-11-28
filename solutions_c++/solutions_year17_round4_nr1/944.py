#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <utility>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <queue>

using namespace std;

void go(int n,int p,vector<int> g,vector<int> mask) {
	int res = 0;
	for(int i = 0; i < n; i++) {
		if(g[i]%p==0) {
			res++;
			mask[i] = 0;
		}
	}
	for(int i = 0; i < n; i++) if(mask[i]) {
		for(int j = i+1; j < n; j++) if(mask[j]) {
			if((g[i]+g[j])%p==0) {
				res++;
				mask[i] = mask[j] = 0;
				break;
			}
		}
	}

	for(int i = 0; i < n; i++) if(mask[i]) {
		for(int j = i+1; j < n; j++) if(mask[j]) {
			for(int k = j+1; k < n; k++) if(mask[k]) {
				if((g[i]+g[j]+g[k])%p==0) {
					res++;
					mask[i] = mask[j] = mask[k] = 0;
					goto label1;
				}
			}
		}
label1:
		;
	}

	for(int i = 0; i < n; i++) if(mask[i]) {
		for(int j = i+1; j < n; j++) if(mask[j]) {
			if((g[i]+g[j])%2==0) {
				g[i] += g[j];
				mask[j] = 0;
				break;
			}
		}
	}

	for(int i = 0; i < n; i++) if(mask[i]) {
		for(int j = i+1; j < n; j++) if(mask[j]) {
			if((g[i]+g[j])%p==0) {
				res++;
				mask[i] = mask[j] = 0;
				break;
			}
		}
	}

	for(int i = 0; i < n; i++) if(mask[i]) {
		res++;
		break;
	}
	cout << res << endl;
	
}

void solve() {
	int n,p;
	cin >> n >> p;
	vector<int> g(n);
	vector<int> mask(n,1);
	for(int i = 0; i < n; i++) {
		cin >> g[i];
	}

	if(p==4) {
		go(n,p,g,mask);
		return;
	}

	int res = 0;
	for(int i = 0; i < n; i++) {
		if(g[i]%p==0) {
			res++;
			mask[i] = 0;
		}
	}
	for(int i = 0; i < n; i++) if(mask[i]) {
		for(int j = i+1; j < n; j++) if(mask[j]) {
			if((g[i]+g[j])%p==0) {
				res++;
				mask[i] = mask[j] = 0;
				break;
			}
		}
	}

	for(int i = 0; i < n; i++) if(mask[i]) {
		for(int j = i+1; j < n; j++) if(mask[j]) {
			for(int k = j+1; k < n; k++) if(mask[k]) {
				if((g[i]+g[j]+g[k])%p==0) {
					res++;
					mask[i] = mask[j] = mask[k] = 0;
					goto label1;
				}
			}
		}
label1:
		;
	}

	for(int i = 0; i < n; i++) if(mask[i]) {
		res++;
		break;
	}
	cout << res << endl;
	
}

int main() {
	ios::sync_with_stdio(false); cin.tie(0);
	int T;
	cin >> T;
	for(int t = 0; t < T; t++) {
		cout << "Case #" << t+1 << ": ";
		solve();
	}
}

