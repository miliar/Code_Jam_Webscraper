#include <iostream>

using namespace std;




int main() {
	int T; cin >> T;
	
	long long N,K;

	long long A,B,a,b;
	long long Ai,Bi,ai,bi;
	long long Z,mn,mx;
	for(int t = 0; t < T; t++) {
		cin >> N >> K;
		
		A = N, Ai = 1;
		B = N, Bi = 0;


		while(K>0) {
		
		//cout << "K= " << K << endl;
		//cout << "A=" << A << ",B=" << B << endl;
		//cout << "Ai=" << Ai << ",Bi=" << Bi << endl;


			if (Ai + Bi >= K) {

				if (K <= Ai) {
					Z = A;
				} else {
					Z = B;
				}

				//cout << "Z=" << Z << endl;

				if (Z%2) {
					mn=mx=Z/2;
				} else {
					mx = Z/2;
					mn = mx - 1;
				}



				cout << "Case #" << t+1 << ": " << mx << " " << mn << endl;

				break;
			} else {
				K -= Ai + Bi;
			}

			//cout << endl << ">>>>> ";

			if(A%2) 
			{
				a = A/2; ai = Ai * 2 + Bi; 
				b = A/2 - 1; bi = Bi;

			} else {
				a = A/2; 		ai = Ai;
				b = A/2 - 1; 	bi = Ai + Bi*2;

			}
			
			//cout << endl;
			A = a; Ai = ai;
			B = b; Bi = bi;
			//cout << A << " " << B << endl;
			//cout << Ai << " " << Bi << endl;
		}
	}
	return 0;
}