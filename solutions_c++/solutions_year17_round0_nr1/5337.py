//
//  main.cpp
//  GoogleCodeJam2017
//
//  Created by Aniket p Ghanawat on 07/04/17.
//  Copyright © 2017 Aniket P Ghanawat. All rights reserved.
//

#include <iostream>
#include <vector>
#include <unordered_map>
#include <list>
#include <algorithm>
#include <string>
#include <cmath>

using namespace std;

void solutionA(){
    int T,K,count;
    string S;
    unsigned long len;
    bool flg;
    cin >> T;
    for(int i = 1; i <= T; i++){
        cin >> S;
        cin >> K;
        count = 0;
        len = S.length();
        for(int l,j = 0; j < len; j+=K){
            while(S[j] == '+') j++;
            if(j<len){
                flg =false;
                for(l = 0; l < K; l++){
                    if(S[j+l] == '+') continue;
                    else flg = true;
                }
                if (flg){
                    for(l = 0; l < K; l++){
                        if(S[j+l] == '+') S[j+l] = '-';
                        else S[j+l] = '+';
                    }
                    if(j+l > len){
                        count = -1;
                        break;
                    }
                    count++;
                    j -= K;
                }
            }
        }
       // cout << S << " " << K << "\t";
        cout << "Case #"<<i<<": ";
        if(count >= 0) cout << count << endl;
        else cout << "IMPOSSIBLE" << endl;
    }
    
}

int main(int argc, const char * argv[]) {
    if (argc == 2){
        switch((int)argv[1][0]){
            case 'A':solutionA();
                break;
                
            default:cout << " Problem not solved yet :P";
        }
    }
    else
        cout << "Specify Problem to solve";
    return 0;
}
