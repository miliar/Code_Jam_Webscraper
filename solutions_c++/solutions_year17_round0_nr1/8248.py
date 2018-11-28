/* 
 * File:   main.cpp
 * Author: mehmetfatihuslu
 *
 * Created on April 12, 2014, 4:56 PM
 */
#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>
 
using namespace std;
 
bool isAllPlus(char d[], int l) {
    for(int i=0; i<l; i++) {
        //cout << d[i];
    }
    for(int i=0; i<l; i++) {
        if(d[i] != '+') {
   
            return false;
        }
    }
    
    return true;
}
 
int main() {
 
    string path = "";
    fstream infile (path+"input", std::ios_base::in);
    fstream outfile (path+"output", std::ios_base::out);
    int n;
    int k;
    string s;
    infile >> n;
 
    for(int i=1; i<=n; i++) {
 
        outfile << "Case #" << i << ": ";
 
        infile >> s;
        infile >> k;
 
        int l = s.length();
        
        char *cstr = new char[l + 1];
        strcpy(cstr, s.c_str());
 
        int flip = 0;
 
        for(int j=0; j<l-k+1; j++) {
            if(cstr[j]=='-') {
                for(int m=j; m<j+k; m++) {
                    cstr[m] = cstr[m] == '+' ? '-' : '+';
                }
                flip++;
            }
        }
 
        if(isAllPlus(cstr,l))
            outfile << flip << endl;
        else
            outfile << "IMPOSSIBLE" << endl;
    }
 
    infile.close();
    outfile.close();
 
    return 0;
}
