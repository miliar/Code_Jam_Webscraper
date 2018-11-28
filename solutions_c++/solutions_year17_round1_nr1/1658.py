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
        int row, col, first = -1;
        cin >> row >> col;
        vector<string> array(row);
        for (int j = 0; j < row; j++) {
            cin >> array[j];
            if (j == first + 1 && array[j].find_first_not_of('?') == string::npos) {
                first++;
            } else {
                if (array[j].find_first_not_of('?') == string::npos) {
                    array[j] = array[j - 1];
                } else {
                    char c = '\0';
                    int pos = 0, current;
                    while ((current = array[j].find_first_not_of('?', pos)) != string::npos) {
                        c = array[j][current];
                        while (pos <= current)
                            array[j][pos++] = c;
                    }
                    while (pos < col)
                        array[j][pos++] = c;
                }
            }
        }
        for (int j = 0; j <= first; j++)
            array[j] = array[first + 1];
        cout << "Case #" + to_string(i + 1) + ":" << endl;
        for (auto &line : array)
            cout << line << endl;
    }
}
