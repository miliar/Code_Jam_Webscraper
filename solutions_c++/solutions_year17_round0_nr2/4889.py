//
// Created by brian on 4/7/2017.
//
#include <iostream>
#include <fstream>
#include <string>
using namespace std;
int main() {
    long N, T;
    string s = "";
    ifstream fin ("B-large.in");
    ofstream fout ("outputB.txt");
    char maxdig = '0'-1;
    fin >> T;
    for(int x = 0; x < T; x++){
        fin >> N;
        s = to_string(N);
        maxdig = s[0];
        for(int i = 1; i<s.length(); i++){
            if(s[i] > maxdig) {
                maxdig = s[i];
            }
            else if(s[i] == maxdig && i == s.length()-1){

            }
            else if (s[i] < maxdig){
                if(maxdig == '1'){
                    s[0] = '0';
                    for(int j = 1; j < s.length(); j++){
                        s[j] = '9';
                    }
                }
                else{
                    int k = i-1;
                    while(k > -1 && s[k] == maxdig){
                        k--;
                    }
                    s[k+1] = maxdig - 1;
                    for (int j = k+2; j < s.length(); j++) {
                        s[j] = '9';
                    }
                }
            }
        }
        fout << "Case #" << x+1 << ": " << stol(s) << endl;
    }
}
