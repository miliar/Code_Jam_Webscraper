#include <iostream>
using namespace std;

typedef long long LL;

int main(){
	LL N, K, segs, k, large, small, nlarge, nsmall;
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t){
		cin >> N >> K;
		segs = 1; k = 0; large = small = N; nlarge = 0; nsmall = 1;
		while(k + segs < K){
			k += segs;
			N -= segs;
			segs = 2*segs;
			small = (small-1)/2;
			large = large/2;
			if (large == small){
				nlarge = 0; nsmall = N/small;
			}else{
				nlarge = N % segs;
				nsmall = segs - nlarge;
			}
		}
		//cout << k << ", " << N << ", " << small << " (" << nsmall << "), " << large << " (" << nlarge << ")" << endl;
		if (k + nlarge < K) cout << "Case #" << t << ": " << small/2 << " " << (small-1)/2 << endl;
		else cout << "Case #" << t << ": " << large/2 << " " << (large-1)/2 << endl;
	}
}