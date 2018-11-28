#include <iostream>
using namespace std;
bool checker(unsigned long long int s) {
     long long int curr, prev = -1;
    
    do {
        curr = s%10;
        s /= 10;
        if (prev != -1 && prev < curr)
            return false;
        prev = curr;
    } while (s);
    return true;
}
int main() {
    int t;
    unsigned long long int a;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        cin >> a;
        while(!checker(a) && (a > 0)) {
            a -= 1;
        }
        cout << "Case #" << i << ": " << a << endl;
    }
    return 0;
}
