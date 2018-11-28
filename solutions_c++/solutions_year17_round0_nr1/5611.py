//
//  main.cpp
//  Google code jam - Oversized pancake flipper
//
//  Created by Lucas Prieels on 8/04/17.
//  Copyright © 2017 Lucas Prieels. All rights reserved.
//

#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, const char * argv[]) {
    ifstream fluxi("/Users/lucas/Documents/programmation'/C++/Codejam/Google code jam - Oversized pancake flipper/Google code jam - Oversized pancake flipper/input.in.txt");
    ofstream flux("/Users/lucas/Documents/programmation'/C++/Codejam/Google code jam - Oversized pancake flipper/Google code jam - Oversized pancake flipper/output.out.txt");
    int nbr;
    fluxi >> nbr;
    for (int i=0; i<nbr; i++){
        string a;
        int b;
        fluxi >> a >> b;
        int cpt=0;
        bool broke=false;
        for (int j=0; j<a.length(); j++){
            if (a[j]=='-' && j+b<=a.length()){
                a[j]='+';
                cpt++;
                for (int k=j; k<j+b; k++){
                    if (a[k]=='-'){
                        a[k]='+';
                    }
                    else{
                        a[k]='-';
                    }
                }
            }
            else if (a[j]=='-' && j+b>a.length()){
                flux << "Case #" << i+1 << ": IMPOSSIBLE" << endl;
                broke=true;
                break;
            }
        }
        if (!broke){
            flux << "Case #" << i+1 << ": " << cpt << endl;
        }
        broke=false;
    }
    return 0;
}
