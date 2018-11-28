#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <memory>

using namespace std;

int length(const long long &n) {
    if(n == 0) return 1;
    int i = 0;
    long long t = n;
    while(t > 0) {
        t = t / (long long) 10;
        ++i;
    }
    return i;
}

// 98765
int getDigit(int i, int length, const long long &n) {
    long long t = n;
    while((length - i) > 1) {
        t = t / (long long) 10;
        ++i;
    }
    return t % 10;
}

long long tenth(int pow) {
    if(pow == 0) return 1;
    else return 10*tenth(pow-1);
}

int main() {
    int t;
    cin >> t;
    for(int ts = 1; ts <= t; ++ts) {
        cout << "Case #" << ts << ": ";
        
        long long n;
        
        cin >> n;
        if(n < 10) {
            cout << n << endl;
            continue;
        }

        int len = length(n);
        int prev = getDigit(0, len, n);
        long long curr = 0;
        int p = 0;
        bool inorder = true;
        for(int i = 1; i < len; ++i) {
            int temp = getDigit(i, len, n);
            
            if(temp != prev) {
                curr = curr * 10 + prev;
            }
            if(temp < prev) {
                long long x = tenth(len - p - 1);
                curr = curr*x -1;
                inorder = false;
                break;
            } else if (temp > prev) {
                p = i;
                prev = temp;
            }
        }
        cout << (inorder ? n : curr) << endl;
    }
}
