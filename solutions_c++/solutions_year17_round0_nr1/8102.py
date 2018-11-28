#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int minimumFlips(string s, int k) {
    int flips = 0;

    for (int i = 0; i < s.size()-k+1; i++) {
        if (s[i] == '-') {
            for (int j = i; j < i+k; j++) {
                if (s[j] == '-') {
                    s[j] = '+';
                }
                else {
                    s[j] = '-';
                }
            }
            flips++;
        }
    }
    
    for (int i = s.size()-k+1; i < s.size(); i++) {
        if (s[i] == '-') {
            return -1;
        }
    }
    
    return flips;
}

int main() {
    ifstream infile("A-large.in");
    ofstream outfile("A-large.out");
    int t, k, flips;
    string s;
    infile >> t;
    for (int i = 0; i < t; i++) {
        infile >> s;
        infile >> k;
        
        outfile << "Case #" <<  i+1 <<": ";

        flips = minimumFlips(s, k);
        
        if (flips == -1) {
            outfile << "IMPOSSIBLE" << endl;
        }
        else {
            outfile << minimumFlips(s, k) << endl;
        }
    }
    return 0;
}
