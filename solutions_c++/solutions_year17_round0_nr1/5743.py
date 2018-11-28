
#include <vector>
#include <iostream>
#include <string>
#include <sstream>
#include <fstream>
#include <cstdio>

using namespace std;

void flip(string& p, int i){
    if(p[i] == '+') p[i] = '-';
    else p[i] = '+';
}

int solve(string& pan, int k){
    int c = 0;
    for(int i = 0; i < pan.length()-k+1; ++i){
        if(pan[i] == '-'){
            for(int j = i; j < i+k; ++j){
                flip(pan, j);
            }
            ++c;
        }
    }

    for(int i = pan.length()-k; i < pan.length(); ++i){
        if(pan[i] == '-') return -1;
    }

    return c;
}

int main(int len, const char** args){
    string file;
        
    if(len > 1){
        file = string(args[1]);
    }
    else{
        file = "tiny.in";
    }

    ifstream fh(file.c_str());

    string line;
    fh >> line;
    int n = stoi(line);

    string pans;
    string k;
    char buf[2048];

    ofstream out(file + ".out");
    for(int i = 0; i < n; ++i){
        fh >> pans;
        fh >> k;
        int r = solve(pans, stoi(k));

        stringstream ss;
        ss<< "Case #" << i+1 << ": " << (r == -1? "IMPOSSIBLE" : to_string(r).c_str()) << endl;
        string ans = ss.str();
        cout << ans;
        out << ans;
        
        //printf("Case #%i: %s\n", i+1, r == -1? "IMPOSSIBLE" : to_string(r).c_str());
        //vsnprintf(buf, sizeof(buf), "Case #%i: %s\n", i+1, r == -1? "IMPOSSIBLE" : to_string(r).c_str());
    }

    return 0;
}
