//
//  main.cpp
//  Codejam - Bathroom stalls
//
//  Created by Lucas Prieels on 8/04/17.
//  Copyright © 2017 Lucas Prieels. All rights reserved.
//

#include <iostream>
#include <queue>
#include <fstream>

using namespace std;

int main() {
    ofstream flux ("/Users/lucas/Documents/programmation'/C++/Codejam/Codejam - Bathroom stalls2/Codejam - Bathroom stalls2/output.out");
    int nbr;
    cin >> nbr;
    for(int i=0;i<nbr;i++) {
        int n,k;
        priority_queue<int> qu;
        cin >> n >> k;
        int j=1, left, right;
        int up = n;
        while(j<k+1 && up) {
            if(!qu.empty()) {
                up = qu.top();
                qu.pop();
            }
            if(up) {
                if(up%2==0) {
                    left = (up/2)-1;
                    right = up/2;
                }
                else {
                    left = right = (up-1)/2;
                }
            }
            
            qu.push(right);
            qu.push(left);
            j++;
        }
        flux << "Case #" << i+1 << ": " << right << " " << left << endl;
    }
    return 0;
}
