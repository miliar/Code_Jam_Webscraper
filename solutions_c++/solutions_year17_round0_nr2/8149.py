#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

void run() {
	ll T;
	cin >> T;
	for(int t = 0; t < T; t++) {
		ll N;
		cin >> N;	

		while(true) {
			ostringstream ss;
			ss << N;
			string s = ss.str();

			ll over = 1;
			ll base = 1;
			for(int i = s.size()-2; i >= 0; i--) {
				if(s[i] > s[i+1]) {
					//printf("%d %lld ", i, N);
					
					N -= base*(s[i+1]-'0'+1);
		
					for(i = i+2; i < s.size(); i++) {
						base /= 10;
						N += base*('9'-s[i]);
					}					

					over = 0;
					//printf("%lld\n", N);
					break;
				}

				base *= 10;
			}

			if(over) break;
		}	 

		printf("Case #%d: %lld\n", t+1, N);
	}


}

int main() {
	run();
}
