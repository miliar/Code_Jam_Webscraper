#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef double ld;



void run() {
	ll T;
	cin >> T;


	for(int tc = 0; tc < T; tc++) {
		ll N, P;
		cin >> N >> P;
		
		vector<ll> al(N);
		for(int i = 0; i < N; i++) cin >> al[i];

		vector<ll> bl(N);

		for(int i = 0; i < N; i++) {
			bl[i] = al[i] % P;
		}

		sort(bl.begin(), bl.end());

		ll pairs = 0;
		
		vector<ll> vis(N, 0);
		for(int i = 0; i < N; i++) {
				if(vis[i]) continue;
				if(!bl[i]) {
					vis[i] = 1;
					continue;
				}
	
				for(int j = 0; j < N; j++) {
					if(!bl[j] || vis[j] || j == i) continue;

					if((bl[i]+bl[j]) % P == 0)  {
						vis[i] = 1;
						vis[j] = 1;
						//printf("add %d %d\n", i, j);
						pairs++;	
					}

					if(vis[j]) break;
				}
				if(vis[i]) continue;
		}

		for(int i = 0; i < N; i++) {
				if(P < 3) break;
				if(vis[i]) continue;
				if(!bl[i]) continue;
				for(int j = 0; j < N; j++) {
					if(!bl[j] || vis[j] || j == i) continue;
					for(int k = 0; k < N; k++) {
							if(!bl[k] || vis[k] || k == j || k == i) continue;
							if((bl[i]+bl[j]+bl[k]) % P == 0)  {
								vis[i] = 1;
								vis[j] = 1;
								vis[k] = 1;
								pairs += 2;
								//printf("add %d %d %d\n", i, j, k);
							}
							if(vis[k]) break;
					}
						if(vis[j]) break;
				}
				if(vis[i]) continue;
		}

		for(int i = 0; i < N; i++) {
		if(P < 4) break;
		if(vis[i]) continue;
		if(!bl[i]) continue;
			for(int j = 0; j < N; j++) {
				if(!bl[j] || vis[j] || j == i) continue;
				for(int k = 0; k < N; k++) {
						if(!bl[k] || vis[k] || k == i || k == j) continue;
						vector<ll>::iterator it = lower_bound(bl.begin(), bl.end(), P-bl[i]-bl[j]-bl[k]);
						int id = it-bl.begin();
			
						while(id < N && (vis[id] || id == i || id == j || id == k)) id++;
						
						if(id < N && (bl[id]+bl[i]+bl[j]+bl[k]) % P == 0) {
							vis[i] = 1;
							vis[j] = 1;
							vis[k] = 1;
							vis[id] = 1;
							pairs += 3;
							//printf("add %d %d %d %d\n", i, j, k, id);
						}
					
						if(vis[k]) break;
				}
				if(vis[j]) break;
			}
			if(vis[i]) continue;
		}

		ll over = 0;
		for(int i = 0; i < N; i++) over += vis[i] ^ 1;
		pairs += max(0LL, over-1);

		// if(over >= P) {
		// 	cout << "Error " << over  << endl;
		// 	for(int i = 0; i < N; i++) cout << vis[i] << " ";
		// 	cout << endl;
		// 	for(int i = 0; i < N; i++) cout << bl[i] << " ";
		// 	cout << endl;
		// }
		//

		//

		//cout << "over " << over << endl;						

		cout << "Case #" << tc+1 << ": " << N-pairs << endl;

		
		
	}
}

int main() {
	run();
}
