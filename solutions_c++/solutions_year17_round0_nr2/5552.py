#include <iostream>
#include <string>

using namespace std;

int main() {
    
    int t, d1, d2;
    unsigned long long int N, i;
    
    cin >> t;
    
    for (int ci = 1; ci <= t; ++ci) {
        
        cin >> N;
        
        bool tidy;
        int deep;
        while (N != 0) {
            tidy = true;
//            cout << "check " << N << endl;
            i = N;
            deep = 0;
            do {
                deep++;
                d2 = i % 10;
//                putchar('0' + d2);
                i /= 10;
                d1 = i % 10;
//                putchar('0' + d1);
                if (d1 > d2) {
                    tidy = false;
                    break;
                }
//                cout << "\t" << deep << endl;
            } while (i > 0);
//            cout << endl;
            if (tidy)
                break;
            else {
                i--;
                for (int j = 1; j <= deep; j++) {
                    i = i * 10 + 9;
                }
                N = i;
            }
        }
        cout << "Case #" << ci << ": " << N << endl;
    }
}