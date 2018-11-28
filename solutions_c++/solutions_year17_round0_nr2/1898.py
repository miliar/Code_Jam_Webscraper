#include <iostream>
#include <cstring>

using namespace std;

int main() {
    int nt, tc, i, j;
    char num[25];

    cin >> nt;
    for (tc = 1; tc <= nt; tc++) {
        cout << "Case #" << tc << ": ";
        
        cin >> num;
        int len = strlen(num);
        int drop = -1;
        int found = 0;
        for (i = 0; i < len - 1; i++) {
            if (i == 0 || num[i] != num[i - 1])
                drop = i;
            if (num[i] > num[i + 1]) {
                found = 1;
                break;
            }
        }
        if (found) {
            num[drop] = num[drop] - 1;
            for (i = drop + 1; i < len; i++) {
                num[i] = '9';
            }
            cout << (num[0] == '0' ? num + 1 : num) << endl;
        } else {
            cout << num << endl;
        }
    }
    return 0;
}
