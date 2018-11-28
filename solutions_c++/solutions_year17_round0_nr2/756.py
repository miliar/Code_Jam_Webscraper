#include <iostream>
#include <string>

#define show(X) cout << #X << " = " << X << endl
using namespace std;

int main() {
    int T;
    cin >> T;
    for (int tt=1; tt<=T; ++tt) {
        int d[100] = {};
        string str;
        cin >> str;
        for (int i=0, j=str.length()-1; j>=0; ++i, --j) {
            d[i] = str[j] - '0';
        }
        int index = str.length() - 1;
        while (index > 0 && d[index] <= d[index-1]) index--;
        if (index > 0) {
            while (d[index] == d[index+1]) index++;
            d[index]--;
            for (int i=0; i<index; ++i)
                d[i] = 9;
        }
        cout << "Case #" << tt << ": ";
        index = 0;
        while (d[index]) index++;
        for (int i=index - 1; i>=0; --i)
            cout << d[i];
        cout << endl;
    }
    return 0;
}

