#include <iostream>
#include <map>

using namespace std;

map<string,size_t> memory;
size_t K;

size_t min_number(const string& S) {
    if(memory.find(S) == memory.end()) {
        memory[S] = INT_MAX; //We avoid loops
        size_t min = INT_MAX;
        for(size_t start = 0; start + K <= S.size(); start++) {
            string new_S = S;
            for(size_t i = start; i < start + K; i++) {
                if(new_S[i] == '+') {
                    new_S[i] = '-';
                } else {
                    new_S[i] = '+';
                }
            }
            min = std::min(min, min_number(new_S) + 1);
        }
        memory[S] = min;
    }
    return memory[S];
}

int main() {
    size_t T;
    string S;
    cin >> T;
    for(size_t t = 1; t <= T; t++) {
        cin >> S >> K;
        memory = map<string,size_t>();
        memory[string(S.size(), '+')] = 0;
        size_t result = min_number(S);
        if(result == INT_MAX) {
            cout << "Case #" << t << ": IMPOSSIBLE\n";
        } else {
            cout << "Case #" << t << ": " << result << '\n';
        }
    }
    return EXIT_SUCCESS;
}
