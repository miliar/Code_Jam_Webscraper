#include <fstream>
#include <string>
#include <bitset>
#define EGAL 0
#define ORICE 1
#define SETORICE 2
using namespace std;

inline string putString(long long N) {
    string sol;

    while (N) {
        sol += ('0' + (N % 10));
        N /= 10;
    }

    for (int i = 0 ; i < (sol.size() / 2) ; ++i) {
        char c = sol[i];
        sol[i] = sol[sol.size() - i - 1];
        sol[sol.size() - i - 1] = c;
    }

    return sol;
}

inline string largest_tidy(string N) {
    if (N.size() == 1)
        return N;

    string sol = N;
    int stare = EGAL;
    int ind = 1;

    while (ind < N.size()) {
        if (stare == EGAL) {
            if (N[ind] >= sol[ind - 1]) {
                sol[ind] = N[ind];
                ++ind;
            }
            else
                stare = SETORICE;
        }
        else if (stare == SETORICE){
            if (N[ind] > '0' && (ind == 0 || (N[ind] - 1) >= sol[ind - 1])) {
                sol[ind] = N[ind] - 1;
                stare = ORICE;
                ++ind;
            }
            else
                --ind;
        }
        else
            sol[ind++] = '9';
    }

    int start = 0;
    while (start < N.size() && sol[start] == '0')
        ++start;

    string output;
    for (int i = start ; i < N.size() ; ++i)
        output += sol[i];

    return output;
}

int main () {
    ifstream cin("B.in");
    ofstream cout("B.out");

    int T;
    cin >> T;

    for (int tst = 1 ; tst <= T ; ++tst) {
        long long N;
        cin >> N;
        cout << "Case #" << tst << ": " << largest_tidy(putString(N)) << "\n";
    }

    return 0;
}
