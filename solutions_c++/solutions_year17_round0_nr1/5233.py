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
    int count, num;
    cin >> count;
    bitset<1000> pancake, target;
    for (int i = 0; i < count; i++) {
        unordered_set<bitset<1000>> used;
        queue<bitset<1000>> pancakes;
        pancake.reset();
        string current;
        cin >> current >> num;
        int size = current.size();
        for (int j = 0; j < size; j++) {
            if (current[j] == '-')
                pancake.set(j);
        }
        used.insert(pancake);
        pancakes.push(pancake);
        int step = 0, result = -1;
        while (!pancakes.empty()) {
            int number = pancakes.size();
            while (number--) {
                pancake = pancakes.front();
                pancakes.pop();
                if (pancake == target) {
                    result = step;
                    break;
                }
                for (int j = 0; j < num; j++)
                    pancake.flip(j);
                if (used.find(pancake) == used.end()) {
                    used.insert(pancake);
                    pancakes.push(pancake);
                }
                for (int j = num; j < size; j++) {
                    pancake.flip(j);
                    pancake.flip(j - num);
                    if (used.find(pancake) == used.end()) {
                        used.insert(pancake);
                        pancakes.push(pancake);
                    }
                }
            }
            step++;
        }
        if (result == -1) {
            cout << "Case #" + to_string(i + 1) + ": IMPOSSIBLE\n";
        } else
            cout << "Case #" + to_string(i + 1) + ": " + to_string(result) + "\n";
    }
}
