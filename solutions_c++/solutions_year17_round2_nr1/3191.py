//
//  main.cpp
//  Codejam - Steed 2: cruise control
//
//  Created by Lucas Prieels on 22/04/17.
//  Copyright © 2017 Lucas Prieels. All rights reserved.
//

#include <iostream>
#include <iomanip>
#include <fstream>

using namespace std;

long double max(long double tps[], long double size){
    long double maxi=0;
    for (int i=0; i<size; i++){
        if (maxi<tps[i]){
            maxi=tps[i];
        }
    }
    return maxi;
}

int main() {
    ifstream fluxi("/Users/lucas/Documents/programmation'/C++/Codejam/Codejam - Steed 2: cruise control/Codejam - Steed 2: cruise control/input.in");
    ofstream fluxo("/Users/lucas/Documents/programmation'/C++/Codejam/Codejam - Steed 2: cruise control/Codejam - Steed 2: cruise control/output.out");
    long double tc;
    fluxi >> tc;
    for (int a=0; a<tc; a++){
        long double dist;
        int nbr;
        fluxi >> dist >> nbr;
        long double pos[nbr];
        long double vit[nbr];
        for (int i=0; i<nbr; i++){
            fluxi >> pos[i] >> vit[i];
        }
        long double tps[nbr];
        for (int i=0; i<nbr; i++){
            tps[i]=dist-pos[i];
            tps[i]/=vit[i];
        }
        long double tempsm=max(tps, nbr);
        fluxo << "Case #" << a+1 << ": " << fixed << setprecision(6) << dist/tempsm << endl;
    }
    return 0;
}
