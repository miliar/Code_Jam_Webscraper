#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <vector>
using namespace std;


int main() {
    int t;
    string n, cmp, n2;

    vector<char> v;
    ifstream inFile("B-small-attempt2.in.txt");
    ofstream outFile("output.txt");



    inFile >> t;

    for (int i = 1; i <= t; ++i) {
        inFile >> n;
        for(int j = stoi(n) ; j >=0 ; j--) {
            v.clear();
            cmp.clear();
            n2 = to_string(j);
           
            for(int k=0 ; k<n2.length() ; k++) {
                v.push_back(n2[k]);
            }
            sort(v.begin(),v.end());


            for(int k=0 ;k<v.size() ; k++) {
                cmp.push_back(v[k]);
            }
            
            if(n2 == cmp) {
                
                outFile << "Case #" << i <<": "<< cmp << endl;
                
                break;
            }
            
            
        }


    }
    inFile.close();
    outFile.close();
    return 0;
}