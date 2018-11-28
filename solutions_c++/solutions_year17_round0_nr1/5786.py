#include <iostream>
#include <fstream>
#include <unordered_set>
#include <string>
#include <cmath>
#include <list>
#include <map>
#include <algorithm>
#include <iomanip>
#include <float.h>
using namespace std;

#define fori(n) for(int i=0; i<n; ++i)
#define forj(n) for(int j=0; j<n; ++j)

string solve(int N, ifstream& input, ofstream& output) {
    string s;
    int k, r = 0;
    input >> s >> k;
    fori(s.length()-k+1) {
        if(s.at(i) == '-') {
            forj(k) {
                s.at(i+j) = s.at(i+j) == '-' ? '+' : '-';
            }
            r++;
        }
    }

    for(int i=s.length()-k; i<s.length(); ++i) {
        if(s.at(i) == '-') {
            return "IMPOSSIBLE";
        }
    }
    return to_string(r);
}

int main()
{
    ifstream input("../GoogleJam/A-large.in");
    ofstream output;
    output.open("../GoogleJam/output.txt");
    if(!input.is_open()) exit(EXIT_FAILURE);
    int N;
    input >> N;
    fori(N) {
        output << "Case #" << (i+1) << ": " << solve(i, input, output) << endl;
    }

    input.close();
    output.close();

    cout << "DONE" << endl;
}
