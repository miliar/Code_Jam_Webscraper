#include <iostream>
#include <string>
using namespace std;

string result(string n) {
    long i = 0;
    long len = n.size();
    if (len == 1)
        return n;

    while (i < len - 1) {
        if (n[i] > n[i + 1]) {
            if (n[i] == '0') {
                if (i > 0)
                    n[i] = '9';
            } else
                n[i++] = (char) (n[i] - 1);

            while (i < len) n[i++] = '9';
        }
        i++;
    }

    i = len - 1;
    while (i > 0) {
        if (n[i] < n[i - 1]) {
            n[i] = '9';
            if (n[i - 1] == '0') {
                n[i - 1] = '9';
            } else
                n[i - 1] = (char) (n[i - 1] - 1);
        }
        i--;
    }
    if (n[0] == '0')
        n.erase(0,1);
    return n;
}

int main(){
    int t;
    string n;
    cin >> t;
    for (int i=1; i<=t; ++i){
        cin >> n;
        cout << "Case #" << i << ": " << result(n) << endl;
    }
    return 0;
}