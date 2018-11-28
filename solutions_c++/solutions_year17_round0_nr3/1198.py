#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <map>

using namespace std;
typedef long long int LL;
int lvof(LL k){
	int lv = 0;
	while(k>1){
		k/=2;
		lv++;
	}
	return lv;
}
int main() {
	int t;
	cin >> t;
	for(int fm=1;fm<=t;fm++){
		LL Nx,Ny,V=1,N,k,x,y;
		cin >> N >> k;
		int lv = lvof(k);
		x = N;
		y = N;
		if(k > 1){
			if(N%2 == 0){
				x = N/2;
				y = N/2 - 1;
			}
			else {
				x = y = (N-1)/2;
			}
			Nx = Ny = 1;
			k -= V;
			for(int i=1;i<lv;i++){
				LL tempy = y;
				LL tempx = x;
				V *= 2;
				k -= V;
				if(x%2 == 0 && y%2 == 0){
					x = tempx/2;
					y = tempx/2 - 1;
					Nx += Ny;
					Ny = Nx;
				}
				else if(x%2 == 0 && y%2 == 1){
					x = tempx/2;
					y = tempx/2 - 1;
					Ny *= 2;
					Ny += Nx;
				}
				else if(x%2 == 1 && y%2 == 0){
					x = (tempx-1)/2;
					y = tempy/2 - 1;
					Nx *= 2;
					Nx += Ny;
				}
				else if(x%2 == 1 && y%2 == 1){
					y = x = (tempx-1)/2;
					Nx *= 2;
					Ny *= 2;
				}
			}
			//cout << x << " : " << y << endl;
		}
		cout << "Case #" << fm << ": ";
		if(k <= Nx){
			if(x%2 == 0)cout << x/2 << " " << x/2-1;
			else cout << (x-1)/2 << " " << (x-1)/2;
			cout << "\n";
		}
		else {
			if(y%2 == 0)cout << y/2 << " " << y/2-1;
			else cout << (y-1)/2 << " " << (y-1)/2;
			cout << "\n";
		}
		
	}
	return 0;
}