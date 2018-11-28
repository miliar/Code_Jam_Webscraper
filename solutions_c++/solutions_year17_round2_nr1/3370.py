#include<iostream>
using namespace std;

int main() {
    double k,s, tiempo, d,n,t;
    cin >> t;
    
    for (int i = 1 ; i <=t; i++ ) {
        cin >> d >> n;

        cin >> k >> s;
        tiempo = (d-k)/s;
        for( int j = 1; j < n; j++ ) {
            cin >> k >> s;
            if( (d-k)/s > tiempo)
                tiempo = (d-k)/s;
        }
        printf("Case #%d: %.6f\n",i,d/tiempo);
        // cout << "Case " << i << ": " << d/tiempo << endl;
    }

    return 0;
}