#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>

using namespace std;

int T;

long long K,N;

int main(){
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	cin >> T;
	int cas = 0;
	while(T--){
		cin >> N >> K;
		printf("Case #%d: ",++cas);
		long long l = 1,r = N;
		long long ans = 0;
		while(K > 0){
			K--;
			
			long long mid = (l + r) >> 1;
			//cout << l << " " << mid << " " << r << endl;
			if(K == 0){
				ans = mid;
				break;
			}
			if(K % 2){
				l = mid + 1;
				K = (K + 1) / 2;
			}else{
				r = mid - 1;
				K = K / 2;
			}
		}
		//cout << ans << endl;
		//cout << l << " " << r << endl;
		cout << r - ans << " " << ans - l << endl;
	}
	return 0;
}
