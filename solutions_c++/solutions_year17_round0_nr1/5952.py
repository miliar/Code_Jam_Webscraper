#include <iostream>
#include <string>
using namespace std;

int main() {
    int T;
    cin >> T;
    for(int t = 1; t <= T; ++t) {
        cout << "Case #" << t << ": ";

        string pancakes;
        int n, f = 0, j = 0;
        std::string::iterator i;

        cin >> pancakes >> n;
        for(i = pancakes.begin(); i < pancakes.end(); ++i) {
            if(*i == '+') continue;
            ++f;
            for(j = 0; j < n; ++j) {
                if(i + j >= pancakes.end()) {
                    cout << "IMPOSSIBLE";
                    goto end;
                }
                *(i + j) = *(i + j) == '-' ? '+' : '-';
            }
        }
        cout << f;
      end:
        cout << endl;
    }
    return 0;
}
