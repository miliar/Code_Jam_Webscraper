#include <iostream>
#include <iomanip> 
using namespace std;

int T;
long double D, N, speed, pos;
int main(){
	
	cin >> T;
	
	for(int t=1; t<=T; t++){
		cin >> D >> N;
		long double treq = 0;
		for(int i=0; i<N; i++){
			cin >> pos >> speed;
			treq = max(treq, (D - pos)/speed);
			//cout << "treq: " << treq;
		}
		long double ans = D / treq;
		
		cout << "Case #" << t << ": " << setprecision(9) << ans << endl;
	}
}
