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
    int cases;
    cin >> cases;
    for (int i = 0; i < cases; i++) {
        int slots, people;
        cin >> slots >> people;
        unordered_map<int, int> count;
        priority_queue<int> number;
        count[slots] = 1;
        number.push(slots);
        while (people > 1) {
            slots = number.top();
            if (count[slots] >= people)
                break;
            number.pop();
            int current = count[slots], left = slots / 2, right = (slots - 1) / 2;
            if (count.find(left) == count.end())
                number.push(left);
            count[left] += current;
            if (count.find(right) == count.end())
                number.push(right);
            count[right] += current;
            people -= current;
        }
        int num = number.top();
        cout << "Case #" + to_string(i + 1) + ": " + to_string(num / 2) + " " + to_string((num - 1) / 2) << endl;
    }
}
