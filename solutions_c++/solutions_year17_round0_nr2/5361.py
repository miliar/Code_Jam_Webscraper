#include <iostream>

using namespace std;


int main() {
    size_t T;
    string N;
    cin >> T;
    for(size_t t = 1; t <= T; t++) {
        cin >> N;
        for(size_t i = N.size() - 1; i > 0; i--) {
            if(N[i - 1] > N[i]) {
                N[i - 1]--;
                for(size_t j = i; j < N.size(); j++) {
                    N[j] = '9';
                }
            }
        }
        cout << "Case #" << t << ": " << atoll(N.c_str()) << '\n';
    }
    return EXIT_SUCCESS;
}
