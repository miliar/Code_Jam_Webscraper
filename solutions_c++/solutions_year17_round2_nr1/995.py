
#include <iostream>
#include <vector>
#include <string>
#include <math.h>
#include <set>
#include <unordered_set>
#include <queue>
#include <cstdio>
#include <queue>
#include <stack>
#include <unordered_map>
#include <sstream>

#include <stdio.h>      /* printf, scanf, NULL */
#include <stdlib.h>

using namespace std;




int main(){


    int n; cin >> n;
    double des, hs;
    double src, speed;
    for (int i = 1; i <= n; ++i) {
        cin >> des >> hs;
        double temp = std::numeric_limits<double>::max();
        if (hs == 0) temp = 0;
        while (hs-- > 0) {
            cin >> src >> speed;
            double time = (des - src) / speed;
            double ex_speed = des / time;
            temp = min(temp, ex_speed);
        }

        // cout << temp << endl;
        printf("Case #%i: %6.6lf\n",i, temp);

    }
    
    
    return 0;
}