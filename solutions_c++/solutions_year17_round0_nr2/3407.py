//
//  main.cpp
//  Tidy
//
//  Created by Guanyao Huang on 4/7/17.
//  Copyright © 2017 Guanyao Huang. All rights reserved.
//

#include <iostream>
#include <string>
using namespace std;
typedef unsigned long long ull;
int main(int argc, const char * argv[]) {
    // insert code here...
    int T;
    string N;
    cin >> T;
    for(int i=0; i<T; i++){
        cin >> N;
        string retV;
        int j = N.length()-1;
        bool exist = false;
        int lastIndex = N.length() - 1;
        for (j=N.length()-1; j>=1; j--){
            if(N[j] < N[j-1]){
                exist = true;
                lastIndex = j-1;
                while(lastIndex > 0 && N[lastIndex] == N[lastIndex-1]){
                    lastIndex--;
                    j--;
                }
            }
        }
        if(!exist)
            cout << "Case #" << i+1 << ": " << N <<endl;
        else{
            retV = N.substr(0, lastIndex);
            retV.append(1, (char)(N[lastIndex]-1));
            retV.append(N.length()-1-lastIndex, '9');
            if(retV[0] == '0')
                retV = retV.substr(1, retV.length() - 1);
            cout << "Case #" << i+1 << ": " << retV <<endl;
        }
    }
    return 0;
}
