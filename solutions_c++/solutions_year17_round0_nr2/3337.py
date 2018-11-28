#include "string"
#include "iostream"
#include "fstream"
#include "algorithm"
#include <cstring>

using namespace std;

#define FILE "B-large"

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


template <class T>
int numDigits(T number)
{
    int digits = 0;
    if (number < 0) digits = 1; // remove this line if '-' counts as a digit
    while (number) {
        number /= 10;
        digits++;
    }
    return digits;
}


string solve() {
    int ans = 0;

    string numstr;
    unsigned long long number;
    
    int ndigs = 0;
    char newdigits[20];
    char c;
    bool cangoup = false;

    string s;
    //getline(cin, s);
    //cin.ignore();
    while (true) {
        c = cin.get();
        if (c < 48 || c > 57) { break; }
        newdigits[ndigs] = c - 48;
        ndigs++;
        // cout << c;
    }
    
    // cout << endl;

    do {
        cangoup = false;
        for (int i = 0; i < ndigs-1; i++) {
            if (newdigits[i] > newdigits[i+1]) {
                if (cangoup) {
                    newdigits[i+1] = 9;
                }
                else {
                    newdigits[i]--;
                    newdigits[i+1] = 9;
                    cangoup = true;
                }          

                // for (int j = 0; j < ndigs; j++) {
                //     cout << to_string(newdigits[j]);
                // }
                // cout << endl;
            }
        }
    } while (cangoup);

    bool foundfirstdig = false;
    for (int i = 0; i < ndigs; i++) {
        if (foundfirstdig) {
            cout << to_string(newdigits[i]);
        }
        else {
            if (newdigits[i] != 0) {
                foundfirstdig = true;
                cout << to_string(newdigits[i]);
            }
        }
    }
    return "";
}