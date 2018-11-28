#include "string"
#include "iostream"
#include "fstream"
#include "algorithm"
#include <cstring>
#include <set>
#include <map>

using namespace std;

#define FILE "C-small-1-attempt0"

#ifndef DEBUG
    #define DEBUG
#endif

#ifdef DEBUG
    #define D(x) cout << #x << " := " << x << endl;
#else
    #define D(x)
#endif

bool read_input();
string solve();

int main(int argc, char const *argv[]) {
#ifdef FILE
    cout << "INPUT:  " FILE ".in" << endl;
    std::ifstream in(FILE ".in");
    std::streambuf *cinbuf = std::cin.rdbuf(); //save old buf
    std::cin.rdbuf(in.rdbuf()); //redirect std::cin to in.txt!

    std::ofstream out(FILE ".txt");
    std::streambuf *coutbuf = std::cout.rdbuf(); //save old buf
    std::cout.rdbuf(out.rdbuf()); //redirect std::cout to out.txt!
#endif

    int test_cases; cin >> test_cases; cin.ignore();
    for (size_t Case = 1; Case <= test_cases; Case++) {
        cout << "Case #" << Case << ": ";
        cout << solve() << endl;
    }

#ifdef FILE
    std::cin.rdbuf(cinbuf);   //reset to standard input again
    std::cout.rdbuf(coutbuf); //reset to standard output again
    cout << "OUTPUT: " FILE ".txt" << endl;
#endif
    return 0;
}

string solve() {
    unsigned long long K, N;
    cin >> K;
    cin >> N;
    cin.ignore();

    set<unsigned long long>::iterator it;
    map<unsigned long long, unsigned long long> spacecounts;
    set<unsigned long long> spaces;

    unsigned long long a, b;

    spaces.insert(K+1);
    spacecounts.insert(pair<unsigned long long,unsigned long long>(K+1, 1));

    unsigned long long nabs = 1;

    for (unsigned long long i = 0; i < N; i+=nabs) {
        it = spaces.end();
        --it;
        unsigned long long largest = *it;

        a = (largest)/2;
        b = largest - a;

        spaces.insert(a);
        spaces.insert(b);

        if (spacecounts.at(largest) < N - i) {
            // can skip now
            nabs = spacecounts.at(largest);
            spaces.erase(it);
            spacecounts.erase(largest);
        }
        else {
            nabs = N - i;
        }

        if (spacecounts.find(a) == spacecounts.end()) {
            spacecounts.insert(pair<unsigned long long,unsigned long long>(a, nabs));
        }
        else {
            spacecounts.at(a) += nabs;
        }

        if (spacecounts.find(b) == spacecounts.end()) {
            spacecounts.insert(pair<unsigned long long,unsigned long long>(b, nabs));
        }
        else {
            spacecounts.at(b) += nabs;
        }
    }
    a--;
    b--;
    cout << max(a, b) << " " << min(a, b);
    

    return "";
}