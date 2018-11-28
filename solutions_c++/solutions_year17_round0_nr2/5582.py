//
//  main.cpp
//  Codejam - Tidy numbers
//
//  Created by Lucas Prieels on 8/04/17.
//  Copyright © 2017 Lucas Prieels. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main(int argc, const char * argv[]) {
    ofstream flux ("/Users/lucas/Documents/programmation'/C++/Codejam/Codejam - Tidy numbers/Codejam - Tidy numbers/output.out");
    long long int nbr;
    cin >> nbr;
    for (long long int i=0; i<nbr; i++){
        long long int a;
        cin >> a;
        string b=to_string(a);
        long long int size=b.length();
        long long int last=b[size-1];
        bool ok=false;
        for (long long int j=size-2; j>=0; j--){
            int z=b[j];
            if (last<z){
                b[j]--;
                for (long long int k=j+1; k<size; k++){
                    b[k]='9';
                }
                ok=true;
            }
            last=z;
            if (ok){
                j=size-1;
                ok=false;
                last=b[size-1];
            }
        }
        long long int w=atoll(b.c_str());
        flux << "Case #
        " << i+1 << ": " << w << endl;
    }
    return 0;
}
