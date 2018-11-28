#include <iostream>
#include <vector>
#include <cstring>
#include <set>
#include <unordered_set>
#include <map>
#include <unordered_map>
#include <string>
#include <iomanip>
#include <cmath>
#include <algorithm>
#include <queue>
#include <stdlib.h>
#include <time.h>
#include <stdio.h>

using namespace std;

string tidy (string str){
    int lastBigger;
    string returnString;
    lastBigger = str[0];
    for(int i = 0; i != str.size() - 1; ++i){
        if(str[i + 1] > str[i]){
            lastBigger = str[i + 1];
        }
        if(str[i] > str[i + 1]){
            if(lastBigger == str[0]){
                if(str[0] == '1'){
                    for(int j = 0; j != str.size() - 1; ++j){
                        returnString += '9';
                    }
                    return returnString;
                } else{
                    str[0]--;
                    for(int j = 1; j != str.size(); ++j){
                        str[j] = '9';
                    }
                    return str;
                }
            }
            for(int j = 0; j != str.size(); ++j){
                if(str[j] == lastBigger){
                    str[j]--;
                    for(int k = j + 1; k != str.size(); ++k){
                        str[k] = '9';
                    }
                    return str;
                }
            }
        }
    }
    return str;
}

int main(){

    int t;
    string str;
    cin >> t;
    vector <string> cases;
    vector <string> outCases;
    for(int i = 0; i != t; ++i){
        cin >> str;
        cases.push_back(str);
    }
    for(int i = 0; i != t; ++i){
        outCases.push_back(tidy(cases[i]));
    }
    for(int i = 0; i != t; ++i){
        cout << "Case #" << i + 1 << ": " << outCases[i] << "\n";
    }

    return 0;
}
