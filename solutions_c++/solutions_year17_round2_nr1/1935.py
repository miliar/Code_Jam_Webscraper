#include <iostream>
#include <queue>
#include <string>
#include <sstream>
#include <vector>
#include <map>
using namespace std;


void _main(){
	unsigned D, N;
	cin >> D >> N;

    vector<unsigned> K(N, 0);
    vector<unsigned> S(N, 0);
    long double maxTime = 0.0;

    for(unsigned i=0; i<N; i++)
        cin >> K[i] >> S[i];

    for(unsigned i=0; i<N; i++)
        if(((D - K[i]) / (S[i]/1000.)) > maxTime)
            maxTime = (long double)(D - K[i]) / (long double)(S[i]/1000.);

    long double speed = (long double)D / maxTime;

    cout << std::fixed;
    cout << (long double)speed*1000. << endl;
}







int main(){
    unsigned caseNo;
    cin >> caseNo;

    cout.precision(6);

    for(unsigned i=1; i<=caseNo; i++){
		cout << "Case #" << i << ": ";
		_main();
    }
    return 0;
}







