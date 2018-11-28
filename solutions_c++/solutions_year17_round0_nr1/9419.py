#include <iostream>
#include <iomanip>
#include <cmath>
#include <limits>
#include <vector>
#include <algorithm>
#include <map>
#include <queue>
#include <bits/stdc++.h>
#include <fstream>


using namespace std;


int main() {
    ofstream myfile;
    myfile.open ("toSubmit.txt");
    int t;
    cin >> t;
    for (int z = 0; z < t; ++z) {
        string pancake;
        int flag = 0;
        cin >> pancake;
        int ans = 0;
        int k;
        cin >> k;
        int i = 0;
        while (i < pancake.size()) {
            if(pancake[i] == '-'){
                if((i + k) > pancake.size()){
                    flag = 1;
                    cout << "IMPOSIBLE" << endl;
                    break;
                }
                for (int l = i; l < i+k; ++l) {
                    if (pancake[l] == '-') {
                        pancake[l] = '+';
                    }
                    else {
                        pancake[l] = '-';
                    }
                }
                ans++;
            }
            i++;
        }
        if (flag == 0){
            myfile << "Case #"<< z+1 << ':' << " "<< ans << endl;
        }else if (flag == 1){
            myfile << "Case #"<< z+1 << ':' << " "<< "IMPOSSIBLE" << endl;
        }
    }
    myfile.close();
    return 0;
}