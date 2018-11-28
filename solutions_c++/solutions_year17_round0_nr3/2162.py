#include <iostream>

#define LL long long int

using namespace std;

int main() {
	int T,caseno=1;
	cin >> T;
	while(caseno<=T) {
		
		LL n,k,m,ans;
		cin >> n >> k;
		
		m=k;
		ans=n;
		while (m>1) {
			if (m%2==1) {
				if (ans%2==1) ans= (ans-1)/2;
				else ans=(ans/2)-1;	
			}
			else {
				if (ans%2==1) ans=(ans-1)/2;
				else ans=ans/2;
			}
			m=m/2;
		}
		
		cout << "Case #" << caseno << ": ";
		if (ans%2==0) {
			cout << ans/2 << ' ' << ans/2 -1 << '\n'; 
		}
		else cout << ans/2 << ' ' << ans/2 << '\n';
		
		caseno++;
	}
	return 0;
}
