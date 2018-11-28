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

string solve(ifstream& input, ofstream& output) {
    string N;
    input >> N;
    int i = 1;
    while(i < N.length()) {
        if(i > 0 && N.at(i) < N.at(i-1)) {
            if(N.at(i) == '0') {
                N = N.substr(0, i) + string(N.length()-i, '9');
                N.at(i-1)--;
                i--;
            }
            else N.at(i)--;
        }
        else i++;
    }
    forj(N.length())
        if(N[j] != '0') {
            i =j;
            break;
        }
    return N.substr(i);
}

int main()
{
    ifstream input("../GoogleJam/B-large.in");
    ofstream output;
    output.open("../GoogleJam/output.txt");
    if(!input.is_open()) exit(EXIT_FAILURE);
    int N;
    input >> N;
    fori(N) {
        output << "Case #" << (i+1) << ": " << solve(input, output) << endl;
    }

    input.close();
    output.close();

    cout << "DONE" << endl;
}
