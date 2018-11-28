#include <iostream>
#include <bitset>
#include <string>
#define N 1000
#define endl '\n'
#define jizz cin.tie(0);ios_base::sync_with_stdio(0);
using namespace std;
bitset<N+5> in;
int f[1005],n;
int check(int k){
	memset(f,0,sizeof(f));
	int sum = 0;
	int ans = 0;
	for(int i = 0 ; i + k-1 < n ; i++){
		if((in[i] + sum) % 2 != 1){
			f[i] = 1;
			sum++;
			ans++;
		}
		if(i - k + 1 >= 0){
			sum -= f[i-k+1];
		}
	}
	for(int i = n-k+1 ; i < n ; i++){
		if((in[i] + sum) % 2 != 1){
			return -1;
		}
		if(i - k + 1 >= 0){
			sum -= f[i-k+1];
		}
	}
	return ans;
}
int main(){jizz
	int T,t = 1;cin >> T;
	while(T--){
		string s;cin >> s;
		n = s.length();
		for(int i = 0 ; i < s.length(); i++){
			if(s[i] == '-'){
				in[i] = 0;
			}else{
				in[i] = 1;
			}
		}int K;cin >> K;
		int flag = check(K);
		cout << "Case #" << t++ << ": ";
		flag >= 0 ? cout << flag << endl : cout << "IMPOSSIBLE" << endl;
	}
}