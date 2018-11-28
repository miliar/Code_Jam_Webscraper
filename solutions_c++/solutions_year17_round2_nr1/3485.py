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
    cout.precision(6);
    for (int i = 0; i < cases; i++) {
        double time = 0.0;
        long D, N;
        cin >> D >> N;
        for (int j = 0; j < N; j++) {
            int start, speed;
            cin >> start >> speed;
            double current = (double)(D - start) / speed;
            if (current > time)
                time = current;
        }
        double result = D / time;
        cout << "Case #" + to_string(i + 1) + ": " << fixed << result << endl;
    }
}
