#include <iostream>
#include <cstring>
using namespace std;

int main() {
    int nt;
    cin >> nt;
    char n[20];
    char* pointer;
    for (int i = 0; i < nt; ++i) {
        cin >> n;
        for (int p = strlen(n) - 1; p > 0; --p) {
            if (n[p] < n[p-1] || '0' == n[p]) {
                for (int s = p; s < strlen(n); ++s) {
                    n[s] = '9';
                }
                n[p-1] = n[p-1] - 1;
            }
        }
        pointer = ('0' == n[0]) ? &n[1] : n;
        cout << "Case #" << i + 1 << ": " << pointer << endl;
    }
    return 0;
}