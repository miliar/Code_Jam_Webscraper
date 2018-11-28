//
//  main.cpp
//  Dolphin
//
//  Created by Mahmud on 22/04/17.
//  Copyright Â© 2017 Mahmud. All rights reserved.
//

#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <numeric>
#include <algorithm>
#include <functional>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <cassert>
#include <iomanip>
#include <ctime>
#include <sstream>
#include <istream>

using namespace std;

const int me = 1025;

int T, N;
long double D;
long double t[me];
pair<long double, long double> horses[me];

int main(int argc, const char * argv[]) {
    //ios_base::sync_with_stdio(0);
    //cin.tie(0);
    freopen("A-small-attempt2.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    
    cin >> T;
    for(int c = 0; c < T; c ++){
        cin >> D >> N;
        for(int i = 0; i < N; i ++)
            cin >> horses[i].first >> horses[i].second;
        sort(horses, horses + N);
        long double speed = D / ((D - horses[0].first) / horses[0].second);
        for(int i = N - 1; i >= 0; i --){
            if(i == N - 1)
                t[i] = (D - horses[N - 1].first) / horses[N - 1].second;
            else{
                if(horses[i].second >= horses[i - 1].second){
                    t[i] = (D - horses[i].first) / horses[i].second;
                }
                else{
                    long double reach = (horses[i].first - horses[i - 1].first) / (horses[i - 1].second - horses[i].second);
                    if(horses[i].first + reach * horses[i].first > D)
                        t[i] = (D - horses[i].first) / horses[i].second;
                    else t[i] = reach + t[i + 1];
                }
            }
            speed = min(speed, D / t[i]);
        }
        cout << "Case #" << c + 1 << ": ";
        cout.precision(6);
        cout << fixed << speed << endl;
    }
    
    return 0;
}
