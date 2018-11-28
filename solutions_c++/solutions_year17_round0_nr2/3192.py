#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <algorithm>

using namespace std;

int T;
string N;

string::size_type sz = 0;

bool isTidy(string N) {
    string sorted = N;
    sort(sorted.begin(), sorted.end());
    return N == sorted;
}

string lastTidy(string N) {
    if(N.size() == 1 || isTidy(N)) {
        return N;
    }
    
    string end = lastTidy(N.substr(1));
    if(end[0] < N[0]) {
        N[0]--;
        int l = end.size();
        for(int i = 0; i < l; i++) {
            end[i] = '9';
        }
    }
    
    return N[0] + end;
}

int main() {
    ifstream in("inB.txt");
    ofstream out("outB.txt");
    
    in >> T;
    
    for(int t = 1; t <= T; t++) {
        in >> N;
        
        string x = lastTidy(N);
        x.erase(0, x.find_first_not_of('0'));
        
        out << "Case #" << t << ": " << x << endl;
    }
    
    return 0;
}
