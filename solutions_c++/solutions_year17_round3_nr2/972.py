#include <iostream>
#include <vector>
#include <stdio.h>
#include <algorithm>
#include <math.h>

using namespace std;

int main(){
	int T; cin >> T;
	for(int tc = 1; tc <= T; tc++){
		int Ac, Aj; cin >> Ac >> Aj;
		int C[Ac], D[Ac];
		int J[Aj], K[Aj];
		int mx = 0;
		int mn = 10000000;
		int Rmax, Rmin, Lmax, Lmin;
		for(int i = 0; i < Ac; i++){
			cin >> C[i] >> D[i];
			if(C[i] < mn){
				Lmax = D[i];
				Lmin = C[i];
				mn = C[i];
			}
			if(D[i] > mx){
				Rmax = D[i];
				Rmin = C[i];
				mx = D[i];
			}

		}
		mn = 10000000;
		mx = 0;
		for(int i = 0; i < Aj; i++){
			cin >> J[i] >> K[i];
			if(J[i] < mn){
				Lmax = K[i];
				Lmin = J[i];
				mn = J[i];
			}
			if(K[i] > mx){
				Rmax = K[i];
				Rmin = J[i];
				mx = K[i];
			}
		}

		if(Ac  == 1 || Aj == 1){
			printf("Case #%d: %d\n", tc, 2);
			continue;
		}

		//cout << Lmin << " " << Lmax << " " << Rmin << " " << Rmax << endl;
		if(Rmax - Lmin <= 720){
			printf("Case #%d: %d\n", tc, 2);
			continue;
		}
		if(1440 + Lmax - Rmin <= 720){
			printf("Case #%d: %d\n", tc, 2);
			continue;
		}
		printf("Case #%d: %d\n", tc, 4);
	}
	return 0;
}
			
