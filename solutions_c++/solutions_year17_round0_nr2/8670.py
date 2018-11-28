#include <iostream>
#include <string>
using namespace std;

bool is_tidy(int n){
    int max = 0;
    int n1, n2;
    n1 = n%10;
    while (n >= 10) {
        n = n/10;
        n2 = n%10;
        if ( n1 < n2 )
            return 0;
        n1 = n%10;
    }
    return 1;
}

int main () {
    int t, i, tmp;
    cin >> t;
    int *a = new int[t];
    for ( i = 0; i < t; i++ )
        cin >> a[i];
    for ( i = 0; i < t; i++ ){
        tmp = a[i];
        while ( a[i] ){
            if ( is_tidy ( a[i] )){
                cout << "Case #" <<i+1<<": "<< a[i] << endl;
                break;
            }
            a[i]--;
        }
    }

}
