#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    int n;
    int temp;
    int smallcase[100];
    string s;
    string tempS;

    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> smallcase[i];
    }


    for (int i = 0; i < n; i++) {
        for (int j = 0; j < smallcase[i]; j++) {
            temp = smallcase[i] - j;
            s = to_string(temp);
            tempS = s;
            sort(tempS.begin(), tempS.end());
            if (!tempS.compare(s)) {
                cout << "Case #" << i + 1 << ": " << temp << endl;
                break;
            }
        }

    }

}