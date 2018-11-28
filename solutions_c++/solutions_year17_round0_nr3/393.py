#include<iostream>
#include<vector>
#include<array>
using namespace std;


int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	
	int T;
	cin >> T;
	
	for(int TCASE = 1; TCASE <= T; TCASE++) {
		long long n, k;
		cin >> n >> k;
		k--;
		
		array<long long, 2> cnt = {1, 0};
		long long result;
		
		while(1) {
			long long nn = (n-1)/2;
			array<long long, 2> ncnt = {0, 0};
			
			if(cnt[1] > k) {
				result = n;
				break;
			}
			ncnt[n/2-nn] += cnt[1];
			ncnt[n-n/2-nn] += cnt[1];
			k -= cnt[1];
			
			if(cnt[0] > k) {
				result = n-1;
				break;
			}
			ncnt[(n-1)/2-nn] += cnt[0];
			ncnt[(n-1) - (n-1)/2 - nn] += cnt[0];
			k -= cnt[0];
			
			cnt = ncnt;
			n = nn;
		}
		
		cout << "Case #" << TCASE << ": " << result - result/2 << ' ' << result/2 << '\n';
	}
	
	return 0;
}

