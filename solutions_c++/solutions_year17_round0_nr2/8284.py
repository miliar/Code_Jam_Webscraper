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
        cout << d[i];
    }
    for(int i=0; i<l; i++) {
        if(d[i] != '+') {
            cout << " false" << endl;
            return false;
        }
    }
    cout << " true" << endl;
    return true;
}
 
int one() {
 
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
        cout << l << endl;
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
 
int two() {
 
    string path = "";
    fstream infile (path+"input", std::ios_base::in);
    fstream outfile (path+"output", std::ios_base::out);
    int n;
    string s;
 
    infile >> n;
 
    for(int i=1; i<=n; i++) {
        outfile << "Case #" << i << ": ";
        infile >> s;
        int l = s.length();
        if(l==1)
            outfile << s << endl;
        else {
            char *cstr = new char[l + 1];
            strcpy(cstr, s.c_str());
            char pre = cstr[0];
            int cut = 0;
            bool d = false;
            for (int j = 1; j < l; j++) {
                char c = cstr[j];
                if(c==pre) {
 
                }
                else if(c<pre) {
                    d=true;
                    if(pre=='1') {
                        for(int k=0; k<l-1; k++)
                            outfile << '9';
                        break;
                    }
                    else {
                        for (int k = 0; k < cut; k++) {
                            outfile << cstr[k];
                        }
                        pre--;
                        outfile << pre;
                        for (int k = cut+1; k < l; k++)
                            outfile << '9';
                        break;
                    }
                }
                else {
                    pre = c;
                    cut = j;
                }
            }
            if(!d)
                outfile << s;
            outfile << endl;
        }
    }
    infile.close();
    outfile.close();
}
 
int main() {
 
    two();
 
    return 0;
}