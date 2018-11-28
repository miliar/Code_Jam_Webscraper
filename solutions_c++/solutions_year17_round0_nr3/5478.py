#include <bits/stdc++.h>
using namespace std;
const int MAX = 1010;
string s;
int N, K, is[MAX], l[MAX], r[MAX];
int main(){
	int t; cin >> t;
	int cs = 0;
	while(t--){
		++cs;
		cin >> N >> K;
		++N; ++N;
		for(int i=1; i<=N; ++i) is[i] = 0;
		is[1] = 1, is[N] = 1;
		int final = 0, x = 0, y = 0;
		for(int i=1; i<=K; ++i){
			for(int j=1; j<=N; ++j){
				if(is[j] == 1) l[j] = 0;
				else l[j] = l[j - 1] + 1;
			}
			for(int j=N; j>0; --j){
				if(is[j] == 1) r[j] = 0;
				else r[j] = r[j + 1] + 1;
			}
			int chosen = 0, count = 0, maxi = 0;
			for(int j=1; j<=N; ++j){
				if(is[j] == 0){
					int val = min(l[j], r[j]);
					if(val > maxi){
						maxi = val;
						count = 1;
						chosen = j;
					}
					else if(val == maxi){
						++count;
					}
				}
			}
			if(count == 1){
				is[chosen] = 1;
				final = chosen;
				x = max(l[chosen], r[chosen]);
				y = min(l[chosen], r[chosen]);
				// cout << chosen << endl;
			}
			else{
				int chosen2 = 0, count2 = 0, maxi2 = 0;
				for(int j=1; j<=N; ++j){
					if(is[j] == 0){
						if(min(l[j], r[j]) == maxi){
							int val = max(l[j], r[j]);
							if(val > maxi2){
								maxi2 = val;
								chosen2 = j;
							}
						}
					}
				}
				is[chosen2] = 1;
				final = chosen2;
				x = max(l[chosen2], r[chosen2]);
				y = min(l[chosen2], r[chosen2]);
				// cout << chosen2 << endl;
			}
		}
		cout << "Case #" << cs << ": ";
		cout << x-1 << ' ' << y-1 << endl;
	}
}