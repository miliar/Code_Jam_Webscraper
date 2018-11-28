#include <iostream>
#include <stdio.h>

using namespace std;


int main() {
    int T, N, c=0;
    double D, K, S, low, temp;

    cin >> T;

    while(T) {
        T--;
        c++;
        low=-1;

        cin >> D >> N;

        while(N) {
            N--;
            cin >> K >> S;

            temp=D/((D-K)/S);
            if(low>temp || low==-1) low=temp;
        }

        printf("Case #%d: %.6f\n", c, low);
    }

    return 0;
}

