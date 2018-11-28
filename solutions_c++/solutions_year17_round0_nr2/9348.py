#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long ll;
//ll dp[19][10];
char str[20];

int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	cin>>T;
	ll n;
	for (int t=1;t<=T;t++){
		cin>>n;
		sprintf(str,"%lld",n);
		int len = strlen(str);
		int m = 0;
		int now = -1;
		int pre = 0;
		ll ans = 0;
		for (int i=0;i<len;i++){
			if (str[i] < m + '0'){
				now = i;
				break;
			}
			else{
				ans = ans * 10 + str[i] - '0';
				if (str[i] > m + '0'){
					pre = i;
					m = str[i] - '0';
				}
			}	
		}
		if (now != -1){
			for (int i=1;i<now-pre;i++){
				ans /= (ll)10;
			}
			ans -= (ll)1;
			for (int i=pre+1;i<len;i++){
				ans = ans * 10 + 9;
			}
		}
		cout << "Case #"<< t << ": " << ans << endl;
		
	}
	
	return 0;
} 
