#include<iostream>
#include<vector>
using namespace std;


int main() {
	int T;
	cin >> T;
	
	for(int TCASE = 0; TCASE < T; TCASE++) {
		int n, p;
		cin >> n >> p;
		
		vector<int> cnt(p, 0);
		for(int i=0;i<n;i++) {
			int c;
			cin >> c;
			
			cnt[c%p]++;
		}
		
		int result = 0;
		
		if(p == 2) {
			result = cnt[0] + cnt[1]/2 + cnt[1]%2;
		}
		if(p == 3) {
			result = cnt[0];
			
			int mn = min(cnt[1], cnt[2]);
			result += mn;
			cnt[1] -= mn;
			cnt[2] -= mn;
			
			result += (cnt[1]+cnt[2] + 2) / 3;
		}
		if(p == 4) {
			result = cnt[0];
			
			result += cnt[2]/2;
			cnt[2] %= 2;
			
			int mn = min(cnt[1], cnt[3]);
			result += mn;
			cnt[1] -= mn;
			cnt[3] -= mn;
			
			if(cnt[2]) {
				if(cnt[1] > 1) {
					cnt[1] -= 2;
					result++;
				}
				else if(cnt[3] > 1) {
					cnt[3] -= 2;
					result++;
				}
				else if((cnt[1] + cnt[3]) % 4 == 0)
					result++;
				
				cnt[2] = 0;
			}
			
			result += (cnt[1] + cnt[3]+3) / 4;
		}
		
		cout << "Case #" << TCASE+1 << ": " << result << '\n';
	}
	
	return 0;
}

