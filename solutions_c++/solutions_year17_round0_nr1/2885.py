//
//  main.cpp
//  codejam01
//
//  Created by hyspace on 4/8/17.
//  Copyright © 2017 hyspace. All rights reserved.
//

#include <iostream>
#include <string>
#include <sstream>

using namespace std;

int cal(string& data, int size){
    int count = 0;
    for(size_t i = 0; i <= data.size() - size; ++i){
        if(data[i] == '+') continue;
        else{
            for(int j = 0; j < size; ++j){
                if(data[i + j] == '+'){
                    data[i + j] = '-';
                }else{
                    data[i + j] = '+';
                }
            }
            ++count;
        }
    }
    
    for(size_t i = data.size() - size; i < data.size(); ++i){
        if(data[i] == '-') return -1;
    }
    return count;
}

int main(int argc, const char * argv[]) {
    int num_cases;
    cin >> num_cases;
    for(int i = 0; i < num_cases; ++i){
        string data;
        int size;
        cin >> data;
        cin >> size;
        
        
        cout << "case #" << i + 1 << ": ";
        
        string data_rev(data);
        int count1 = cal(data, size);
        int count2 = cal(data_rev, size);
        if(count1 == -1 && count2 == -1){
            cout << "IMPOSSIBLE" << endl;
        }else if(count1 > 0 && count2 > 0){
            cout << min(count1, count2) << endl;
        }else{
            cout << max(count1, count2) << endl;
        }
    }
    return 0;
}
