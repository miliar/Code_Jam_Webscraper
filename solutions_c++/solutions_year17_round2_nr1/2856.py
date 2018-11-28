#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <cstdlib>
#include <float.h>
using namespace std;

int main(){
    ifstream fin ("A-large.in");
    ofstream fout ("1BoutputA.txt");
    int T, dest, n, k, s;
    double time(0);
    fin >> T;
    for (int i = 0; i < T; ++i) {
        fin >> dest >> n;
        for(int j = 0; j < n; j++){
            fin >> k >> s;
            if(static_cast<double>(dest-k)/s > time){
                cout << static_cast<double>(dest-k)/s << endl;
                time = static_cast<double>(dest-k)/s;
            }
        }
        fout.precision(12);
        fout << "Case #" << i+1 << ": " << dest/time << endl;
        time = 0;
    }
}

