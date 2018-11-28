//
//  main.cpp
//  Exercise
//
//  Created by Clyde Xu on 6/20/15.
//  Copyright (c) 2015 Clyde Xu. All rights reserved.
//

#include <algorithm>
#include <cmath>
#include <cstring>
#include <fstream>
#include <iostream>
#include <limits>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>

using namespace std;

int main(){
    int count;
    cin >> count;
    for (int i = 0; i < count; i++) {
        string content;
        cin >> content;
        int size = content.size();
        for (int i = 0; i < size - 1 ; i++) {
            if (content[i] > content[i + 1]) {
                for (int j = i + 1; j < size; j++)
                    content[j] = '9';
                content[i]--;
                for (int j = i; j > 0; j--) {
                    if (content[j] < content[j - 1]) {
                        content[j] = '9';
                        content[j - 1]--;
                    } else
                        break;
                }
                break;
            }
        }
        if (content[0] == '0')
            content = content.substr(1);
        cout << "Case #" + to_string(i + 1) + ": " + content + "\n";
    }
}
