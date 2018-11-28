//
//  main.cpp
//  codejam03
//
//  Created by hyspace on 4/8/17.
//  Copyright © 2017 hyspace. All rights reserved.
//

#include <iostream>
#include <string>
#include <sstream>
#include <map>

using namespace std;

typedef unsigned long long num;


void add_insert(map<num, num, greater<num>>& remain, pair<num, num> value){
    auto it = remain.find(value.first);
    if(it == remain.end()){
        remain.insert(value);
    }else{
        it->second += value.second;
    }
}

num cal(num count, num step){
    map<num, num, greater<num>> remain;
    remain.insert(pair<num, num>(count, 1));
    num current = 0;
    while (remain.size() > 0) {
        auto i = remain.begin();
        current = i->first;
        num c = i->second;
        
        if(step < c){
            break;
        }else{
            step -= c;
            remain.erase(i);
            if(current % 2){
                num next = current / 2;
                num next_c = c * 2;
                add_insert(remain, pair<num, num>(next, next_c));
            }else{
                num next1 = current / 2;
                num next2 = current / 2 - 1;
                add_insert(remain, pair<num, num>(next1, c));
                add_insert(remain, pair<num, num>(next2, c));
            }
        }
    }
    return current;
}

int main(int argc, const char * argv[]) {
    int num_cases;
    cin >> num_cases;
    for(int i = 0; i < num_cases; ++i){
        num count, step;
        cin >> count;
        cin >> step;
        
        
        cout << "case #" << i + 1 << ": ";
        
        num size = cal(count, step - 1);
        num min_max = size % 2 ? size / 2 : size / 2 - 1;
        num max_min = size / 2;
        cout << max_min << ' ' << min_max << endl;
    }
    return 0;
}
