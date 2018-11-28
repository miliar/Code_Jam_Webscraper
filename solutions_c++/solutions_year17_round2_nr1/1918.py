#include <iostream>
using namespace std;

int main(){
    cout.precision(17);
	int T;
	cin >> T;
	for(int ii = 0; ii < T; ii++){
        int D, N;
        cin >> D >> N;

        int tt;
        long double max = 0, tmp;
        int Ki, Si;
        for(int i = 0; i < N; i++){
            cin >> Ki >> Si;
            
            tt = (D - Ki);
            tmp = tt / (long double)Si;

            if(tmp > max) max = tmp;
        }
        //if (ii < 40) continue;
        //cout << "tmp " << tmp << " " << Ki << " Si" << Si << " " << D  << " " << max << "\n";
		cout << "Case #" << ii+1 << ": ";
        cout << (long double)D / (long double)max;
        cout << "\n";
	}
	return 0;
}
