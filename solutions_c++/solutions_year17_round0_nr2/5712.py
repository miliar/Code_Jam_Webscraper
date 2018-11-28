
#include <vector>
#include <iostream>
#include <string>
#include <sstream>
#include <fstream>
#include <cstdio>

using namespace std;

string solve(vector<int>& n){
    for(int i = n.size()-1; i >= 1; --i){
        if(n[i] < n[i-1]){
            n[i] = 9;
            n[i-1]--;

            // FWD propagate
            for(int j = i+1; j < n.size(); j++){
                if(n[j] < n[i]){
                    n[j] = n[i];
                }
                else{
                    break;
                }
            }
        }
    }

    stringstream ss;
    for(int i = 0; i < n.size(); ++i){
        if(i==0 && n[i] == 0) continue;
        ss << n[i];
    }

    return ss.str(); 
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

    string num;
    ofstream out(file + ".out");
    for(int i = 0; i < n; ++i){
        fh >> num;
        vector<int> vn;
        for(int i = 0; i < num.length(); ++i){
            char c = num[i];
            vn.push_back(c - '0');
        }

        string ans = solve(vn);

        stringstream ss;
        ss<< "Case #" << i+1 << ": " << ans << endl;
        string sans = ss.str();
        cout << sans;
        out << sans;
    }

    return 0;
}
