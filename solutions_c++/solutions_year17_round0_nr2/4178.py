#include <iostream>
#include <string> 

using namespace std;

string next(string num) {
    int last = 0;
    for (int j=0; j<num.length()-1; j++) {
        if (num[j] > num[j+1]) {
            if (num[last] != '1') {
                num[last] = num[last] - 1;
                return num.substr(0,last+1) + string(num.length()-last-1, '9');
            }
            else {
                return string(num.length()-1, '9');
            }
        }
        else if (num[j] < num[j+1]) {
            last = j+1;
        }
    }
    return num;
}

int main() {
    int n;
    cin >> n;
    for (int i=0; i<n; i++) {
        string num;
        cin >> num;
        cout << "Case #" << i+1 << ": " << next(num) << "\n";
    }
    return 0;
}