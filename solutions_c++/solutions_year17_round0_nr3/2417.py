#include<iostream>
#include<map>

using namespace std;

int T;
long long N, K, k;

int main(){
	cin >> T;
	for(int t=1; t<=T; t++){
		cin >> N >> K;
		map<long long, long long> m;
		long long a, b, cnt;
		k = K;
		m[N] = 1ll;
		while(k>0){
			map<long long, long long>::reverse_iterator mx = m.rbegin();
			a = mx->first;
			cnt = mx->second;
			m.erase(a);
			if(a%2){
				b = a/2;
				a = b;
			}else{
				b = a/2-1;
				a = a/2;
			}
			if(m.count(a)) m[a] += cnt;
			else m[a] = cnt;
			if(m.count(b)) m[b] += cnt;
			else m[b] = cnt;
			k -= cnt;
		}
		cout << "Case #" << t << ": " << a << " " << b << "\n";
	}
	return 0;
}
