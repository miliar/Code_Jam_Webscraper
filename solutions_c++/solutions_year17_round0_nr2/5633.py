#include<iostream>
#include<string>
using namespace std;
int main() {
    int n;
    cin >> n;
    cin.ignore();
    string number;
    int d[20];
    int length;
    for (int ca = 1; ca <= n; ++ca) {
        getline(cin, number);
        length = number.length();
        for (int i = 0; i < length; ++i)
            d[i] = (number[i] - '0');
        int k = length - 1;
        while (k > 0) {
            if (d[k - 1] > d[k]) {
                for (int i = k; i < length; ++i) d[i] = 9;
                d[k - 1]--;
            }
            k--;
        }
        cout << "Case #" << ca << ": ";
        int zeroFlag = true;
        for (int i = 0; i < length; ++i)
            if (d[i] == 0 && zeroFlag) continue;
            else {
                zeroFlag = false;
                cout << d[i];
            }
        cout << endl;
    }
}