
#include <vector>
#include <iostream>
#include <string>
#include <sstream>
#include <fstream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <set>
#include <exception>
#include <utility>
#include <tuple>
#include <map>
#include <unordered_map>

using namespace std;

struct St {
    int TLx = 0;
    int TLy = 0;

    int BRx = 0;
    int BRy = 0;
    char let = '#';
};

bool expand(int TLx, int TLy, int BRx, int BRy, St& student, vector<vector<char>>& square){
    St snew{student.TLx + TLx, student.TLy + TLy, student.BRx + BRx, student.BRy + BRy, student.let}; 

    //cout << "student: " << snew.let << endl;
    if(snew.TLx < 0 || snew.TLx >= square.size()) return false;
    if(snew.BRx < 0 || snew.BRx >= square.size()) return false;
    if(snew.TLy < 0 || snew.TLy >= square[0].size()) return false;
    if(snew.BRy < 0 || snew.BRy >= square[0].size()) return false;

    bool perfect = true;
    for(int i = snew.TLx; i <= snew.BRx; ++i){
        for(int j = snew.TLy; j <= snew.BRy; ++j){
            if(square[i][j] != snew.let && square[i][j] != '?') return false;

            if(square[i][j] == '?'){
                perfect = false;
            }
        }
    }

    if(perfect) return false;

    for(int i = snew.TLx; i <= snew.BRx; ++i){
        for(int j = snew.TLy; j <= snew.BRy; ++j){

            //cout << "color " << i <<", " << j << ": " << snew.let  << endl;
            square[i][j] = snew.let;
        }
    }

    student = snew;
    return true;
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
    int ncases = stoi(line);

    string num;
    ofstream out(file + ".out");
    for(int i = 0; i < ncases; ++i){
        string sr,sc;
        fh >> sr;
        fh >> sc;
        int r = stoi(sr);
        int c = stoi(sc);

        vector<vector<char>> square;
        unordered_map<char, St> students;

        string iR;
        for(int i = 0; i < r; ++i){
            fh >> iR;

            //cout << "--" << endl;
            //cout<< iR << endl;
            //cout << "--" << endl;

            square.push_back(vector<char>());
            for(int j = 0; j < c; ++j){
                square[i].push_back(iR[j]);

                if(square[i][j] != '?'){
                    students[square[i][j]] = St{ i, j, i , j, square[i][j] };
                }
            }
        }

        for(auto& student: students){
            while(expand(-1, 0, 0, 0, student.second, square)){}
            while(expand(0, -1, 0, 0, student.second, square)){}
            while(expand(0, 0, 1, 0, student.second, square)){}
            while(expand(0, 0, 0, 1, student.second, square)){}
        }


        stringstream ss;
        ss<< "Case #" << i+1 << ":" << endl;

        for(int i = 0; i < square.size(); ++i){
            for(int j = 0; j < square[i].size(); ++j){
                ss << square[i][j];
            }
            ss <<endl;
        }

        string sans = ss.str();
        cout << sans;
        out << sans;
    }

    return 0;
}
