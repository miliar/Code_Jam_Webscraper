#include <cstdlib>
#include <iostream>
#include "set"
#include <map>
#include <iomanip>

using namespace std;

int main(int argc, char *argv[])
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int T,N;
    double D,S,K;
    cin >> T;

	double SS[1000];	
	double MIN;
//	std::map<int,int>::iterator IT = MAP.begin();

	int y;
    for (int T_i=0; T_i<T;T_i++){
		cin>> D >> N;
		
		MIN = -1;
		for (int N_i=0; N_i < N; N_i ++) {
			cin >> K >> S;
			if (S==0) {
				SS[N_i] = 0;
			} else {
				SS[N_i] = (D*S)/ (D-K) ;	
			}
			if (MIN==-1) MIN = SS[N_i];
			if (SS[N_i] < MIN) MIN = SS[N_i];
		}
		std::cout << std::fixed;
		if (MIN==0) {
        cout << "Case #" << T_i+1 << ": " << std::setprecision(6) << 0 << endl;
			
		} else {
        cout << "Case #" << T_i+1 << ": " << std::setprecision(6) << MIN << endl;
		}
    }
    return EXIT_SUCCESS;
}
