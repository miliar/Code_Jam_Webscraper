#include<iostream>

using namespace std;

bool isTidy(int x) {
    int prev = x % 10;
    x /= 10;
    int curr;
    while (x) {
        curr = x % 10;
        if (curr > prev)
            return false;
        prev = curr;
        x /= 10;
    }
    return true;
}

int main() {
    int T;
    cin >> T;
    
    int N;
    for (int i = 0; i < T; ++i) {
        cin >> N;
        while (N > 0) {
            if (isTidy(N--)) {
                cout << "Case #" << i + 1 << ": " << N + 1 << endl;
                break;
            }
        }
        
    }
    
    return 0;
}