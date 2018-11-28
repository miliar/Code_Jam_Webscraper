#include <iostream>
#include <string>
using namespace std;
int main() {
    int T;
    long long n;
    string s;
    cin >> T;
    for(int i = 0; i < T; i++) {
        cin >> n;
        s = to_string(n);
        for (int j = s.length() - 1; j >= 0; j--) {
            // Se c'è una cifra più piccola di me alla mia dx
            for (int k = j + 1; k < s.length(); k++)
                if (s[j] > s[k]) {
                    s[j]--;
                    for (int z = j + 1; z < s.length(); z++)
                        s[z] = '9';
            }
        }
        cout << "Case #" << i + 1 << ": " << stoll(s, nullptr) << endl;
    }
}
