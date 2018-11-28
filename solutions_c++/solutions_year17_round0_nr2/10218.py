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

bool tidy(long long int a){
    string b=to_string(a);
    long long int last=0;
    for (long long int i=0; i<b.length(); i++){
        if (b[i]<last){
            return false;
        }
        last=b[i];
    }
    return true;
}

int main(int argc, const char * argv[]) {
    ofstream flux ("/Users/lucas/Documents/programmation'/C++/Codejam/Codejam - Tidy numbers/Codejam - Tidy numbers/output.out");
    long long int nbr;
    cin >> nbr;
    for (long long int i=0; i<nbr; i++){
        long long int a;
        cin >> a;
        for (long long int j=a; j>=0; j--){
            if (tidy(j)){
                flux << "Case #" << i+1 << ": " << j << endl;
                break;
            }
        }
    }
    return 0;
}
