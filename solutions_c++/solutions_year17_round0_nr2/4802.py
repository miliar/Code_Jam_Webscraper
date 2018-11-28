#include <iostream>
#include <string>
using namespace std;

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; ++i) {
        string tidy;
        cin >> tidy;
        int j = 0;
        for (; j < tidy.length() - 1; ++j)
            if (tidy[j] > tidy[j + 1]) {
                --tidy[j];
                break;
            }
        while(1) {
            if (!j || tidy[j - 1] <= tidy[j])
                break;
            --tidy[--j];
        }
        for (j += 1; j < tidy.length(); ++j)
            tidy[j] = '9';
        if (tidy[0] == '0') {
            j = 0;
            while(tidy[j + 1] == '0') {
                ++j;
            }
            tidy.erase(0, j + 1);
        }

        cout << "Case #" << i + 1 << ": " << tidy << endl;
    }
}
