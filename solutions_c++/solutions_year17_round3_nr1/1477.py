// ༼∩ຈل͜ຈ༽つ━☆ﾟ.*･｡ﾟ .·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º> - code by: kdkdk

#define ONLINE_JUDGE //in case i forget to uncomment this, uncomment this.
#ifdef ONLINE_JUDGE
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <iomanip>

//#include <bits/stdc++.h>
#else
#include "stdc++.h"
#endif

#define int long long
using namespace std;

struct pancake {
    int radius, height;
};

bool operator<(const pancake & lhs, const pancake & rhs) {
    if(lhs.radius != rhs.radius) return lhs.radius < rhs.radius;
    return lhs.height < rhs.height;
}

double PI = atan(1)*4.;

vector<pancake> pancakes;
vector<double> dpArea;
double getNextBiggerPancake(int i, int totalLeft) {
    if(dpArea[i*(pancakes.size()+1) + totalLeft] != -1) return dpArea[i*(pancakes.size()+1) + totalLeft];
    
    double maxArea = 0;
    if(totalLeft == 1) return 2. * PI * pancakes[i].radius * pancakes[i].height + PI *  pancakes[i].radius * pancakes[i].radius;
    else if(totalLeft > 1) {
        for(int j = i+1; j <= pancakes.size()-totalLeft+1; ++j)  {
            double additionalArea = getNextBiggerPancake(j, totalLeft-1);
            double A = additionalArea + PI * 2. * pancakes[i].radius * pancakes[i].height + PI *  pancakes[i].radius * pancakes[i].radius - PI *  pancakes[j].radius * pancakes[j].radius;
            if(maxArea < A) maxArea = A;
        }
    }
    dpArea[i*(pancakes.size()+1) + totalLeft] = maxArea;
    return maxArea;
}

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
#ifndef ONLINE_JUDGE
    freopen("/Users/kdkdk/Desktop/input.txt", "r", stdin);
    //freopen("/Users/kdkdk/Desktop/output.txt", "w", stdout);
#endif
    int t; cin >> t;
    for(int c = 1; c <= t; ++c) {
        int n, k; cin >> n >> k;
        pancakes = vector<pancake>(n);
        dpArea = vector<double>(pancakes.size() * pancakes.size() + 2,-1);
        for(int i = 0; i < n; ++i) cin >> pancakes[i].radius >> pancakes[i].height;
        sort(pancakes.begin(), pancakes.end());
        reverse(pancakes.begin(),pancakes.end());
        
        vector<double> areaDP(k+1,-1); //maximal area with k pancakes
        
        double maxA = 0;
        for(int i = 0; i <= n - k; ++i) {
            double A = getNextBiggerPancake(i, k); //it's not always optimal to start with the lowest pancake
            if(maxA < A) maxA = A;
        }
        std::cout << std::fixed;
        std::cout << std::setprecision(9);
        cout << "Case #" << c << ": " << maxA << endl;
        
    }
}
