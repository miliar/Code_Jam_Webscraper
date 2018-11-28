#include <iostream>
#include <string>
#include <stdio.h>
#include <cmath>

using namespace std;

int main () {
	
	int T;
	int tc;
    unsigned long long int N, K;
	cin >> T;

    for (tc=1;tc<=T;tc++){

        cin >> N >> K;

        int l = 0;

        while (pow(2,l) - 1 < K ) {
            l++;
        }

        l--;
 
        unsigned long long int leftPeople = K - pow(2, l) + 1;
        unsigned long long int leftSlots = N - pow(2, l) + 1;
        unsigned long long int divs = pow(2, l);
        unsigned long long int gap = 0;
        while (gap*divs < leftSlots) {
            gap++;
        }

        gap--;

        unsigned long long int maxdivs = leftSlots - gap*divs;

        unsigned long long int pgap;
        unsigned long long int pmaxgap;
        unsigned long long int pmingap;
        if (maxdivs >= leftPeople) {
            pgap = gap+1;
        } else {
            pgap = gap;
        }

        pmingap = (pgap-1)/2;
        pmaxgap = pgap-1-pmingap;

        cout << "Case #" << tc << ": " << pmaxgap << " " << pmingap << endl;
    } 
	
	return 0;
}

