//
//  main.cpp
//  codejam1a1
//
//  Created by hyspace on 4/14/17.
//  Copyright © 2017 hyspace. All rights reserved.
//


#include <iostream>
#include <string>
#include <sstream>
#include <map>
#include <vector>

using namespace std;



void cut(vector<string>& cake){
    for(string& s: cake){
        char last = '?';
        for(char &c:s){
            if(c != '?'){
                last = c;
                break;
            }
        }
        if(last == '?') continue;
        
        for(char &c:s){
            if(c != '?'){
                last = c;
            }else{
                c = last;
            }
        }
    }
    for(int i = 1; i < cake.size(); ++i){
        for(int j = 0; j < cake[i].size(); ++j){
            if(cake[i][j] == '?'){
                cake[i][j] = cake[i - 1][j];
            }
        }
    }
    for(int i = cake.size() - 2; i >= 0; --i){
        for(int j = 0; j < cake[i].size(); ++j){
            if(cake[i][j] == '?'){
                cake[i][j] = cake[i + 1][j];
            }
        }
    }
}

int main(int argc, const char * argv[]) {
    int num_cases;
    cin >> num_cases;
    for(int i = 0; i < num_cases; ++i){
        int count, step;
        cin >> count;
        cin >> step;
        vector<string> data;
        for(int j = 0; j < count; ++j){
            string row;
            cin >> row;
            data.push_back(row);
        }
        cut(data);
        
        cout << "case #" << i + 1 << ": " << endl;
        
        for(string& s: data){
            cout << s << endl;
        }
    }
    return 0;
}
