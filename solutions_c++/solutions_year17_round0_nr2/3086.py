#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int getOffIndex(string N) {
    for (int i=1; i<N.size(); i++) {
        if (N[i] - N[i-1] < 0) 
            return i;
    }
    return N.size();
}

string getLastTidy(string N) {
    if (N.size() == 1)
        return N;
    int off_index = getOffIndex(N);
    while (off_index != N.size()) {
        for (int i=off_index; i<N.size(); i++)
            N[i] = '9';
        int sub_index = off_index - 1;
        while (true) {
            if (N[sub_index] > '0') {
                N[sub_index] = (char)(N[sub_index] - 1);
                break;
            }
            else {
                N[sub_index] = '9';
                sub_index--;
            }
        }
        off_index = getOffIndex(N);
    }
    if (N[0] == '0')
        N = N.substr(1);
    return N;
}

int main(int argc, char* argv[]) {
    ifstream infile(argv[1]);
    ofstream outfile(argv[2]);
    int T;
    string N;
    infile >> T;
    for (int i=1; i<=T; i++) {
        infile >> N; 
        outfile << "Case #" << i << ": " << getLastTidy(N) << endl;
    }
    outfile.close();
    infile.close();
}
