#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    for(int i = 1; i <= n; i++) {
        string n;
        cin >> n;
        unsigned long long inum = stoull(n), buff = inum;
        for(unsigned long long j = 10; inum / j != 0; j *= 10) {
            int a = (buff - buff / 10 * 10);
            buff /= 10;
            int b = (buff - buff / 10 * 10);
            if(a < b) {
                inum /= j;
                inum *= j;
                inum--;
                buff--;
            }
        }
        cout << "Case #" << i << ": " << inum << endl;
    }
    return 0;
}
