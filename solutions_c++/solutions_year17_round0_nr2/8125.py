#include <iostream>
#include <string>
#include <fstream>
#include <math.h>
#include <vector>

using namespace std;

string allNine(int n) {
    string nine = "";
    
    for (int i = 0; i < n; i++) {
        nine += '9';
    }
    
    return nine;
}

string lastTidy(string n) {
    
    string number = "123456789";

    char last = n[0];
    string tidy = "";

    for (int i = 0; i < n.size(); i++) {
        if (n[i] == last) {
        }
        else if (n[i] > last) {
            last = n[i];
        }
        else {
            int lastIndex = tidy.size()-1;

            tidy[lastIndex]--;

            if (lastIndex-1 >= 0) {
                if (tidy[lastIndex-1] > tidy[lastIndex]) {
                    for (int j = 0; j < lastIndex; j++) {
                        tidy[j]--;
                    }
                    tidy[lastIndex] = '9'; 
                }
            }
            
            if (tidy[0] == '0') {
                return allNine(n.size()-1);
            }

            return tidy + allNine(n.size()-tidy.size());
        }
        tidy += last;
    }
    
    return tidy;
}

int main() {
    ifstream infile("B-small-attempt1.in");
    ofstream outfile("B-small-attempt1.out");
    int t;
    string n;
    infile >> t;
    for (int i = 0; i < t; i++) {
        infile >> n;
        
        outfile << "Case #" <<  i+1 <<": ";

        outfile << lastTidy(n) << endl;
    }
    return 0;
}
