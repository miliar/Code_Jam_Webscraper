//
// Created by Ki Ageng Satria Pamungkas on 4/8/17.
//
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <fstream>
#include <algorithm>
using namespace std;

int main(){
    int T;
    long long int N;
    int Nlist[17];
    string s,x;
    cin >> T;
    ofstream myfile;
    myfile.open ("output.txt");
    for (int i = 0; i < T ; ++i) {
        cin >> N;
        s = to_string(N);
        for (int j = 0; j <s.length() ; ++j) {
            int y = s[j] - 48;
            Nlist[j]= y;
        }
        x ="";
        for (int j = s.length()-1; j >=0 ; --j) {
            if(j != 0) {
                if (Nlist[j] < Nlist[j -1]) {
                    Nlist[j-1] -= 1;
                    for (int k = j; k <s.length() ; ++k) {
                        Nlist[k]=9;
                    }
                }
            }
        }
        for (int j = 0; j <s.length() ; ++j) {
            x = x+to_string(Nlist[j]);
        }
        N = stol(x);
        x = to_string(N);
        myfile<<"Case #"<<i+1<<": "<< x <<"\n";
    }
    myfile.close();
}

