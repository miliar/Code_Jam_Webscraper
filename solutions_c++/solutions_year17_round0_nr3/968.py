#include <iostream>
#include <map>
using namespace std;

map<long long,long long> m;
int main(){
	ios_base::sync_with_stdio(false);
	int t; cin >> t;
	for (int i=0;i<t;i++){
		cout << "Case #" << i+1 << ": ";
		long long N,K; cin >> N >> K;
		m.clear();
		m[N]++;
		long long cn = 0;
		long long min,max;
		while (cn < K){
			map<long long, long long>::iterator it = --m.end();
			long long x = it->first; cn += it->second;
			
			if (x%2){
				min = max = x/2;
			} else {
				max = x/2;
				if (max >0) min = max-1; else min = max;
			}
			if (max > 0) m[max] += it->second;
			if (min > 0) m[min] += it->second;
			m.erase(it);
		}
		cout << max << " " << min << endl;
	}
}
