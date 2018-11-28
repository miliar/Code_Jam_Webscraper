#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>

using namespace std;

int main(){
	int T;
	cin >> T;
	int index = 0;

	while (index++ < T){
		long long N, K;
		
		cin >> N >> K;
		
		long long step = 1;
		while(K > step)
		{
			K -= step;
			step *= 2;
			N -= step/2;
		}
		//cout << N << ", " << K << ", " << step << endl;
		long long ans = N / step;
		if(K <= N%step)ans ++;

		cout << "Case #" << index << ": " << ans/2 << ' ' << (ans-1)/2 << endl;
	}
}
