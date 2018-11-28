#include <iostream>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <cstdio>

#define PI 3.1415926535898
#define MAX_SIZE 1010

using namespace std;

struct pancake{
    double radius;
    double height;
    double height_area;
};

pancake pancakes[MAX_SIZE];

int T, N, K;
double ans = 0;

bool compare(pancake a, pancake b) {
    return a.height_area > b.height_area;
}

void calc(){
    ans = 0;
    for(int i = 0; i < N; i++){
        bool unavailable[MAX_SIZE] = {0};
        unavailable[i] = true;
        for(int j = 0; j < N; j++){
            if(pancakes[j].radius > pancakes[i].radius + 0.1)
                unavailable[j] = true;
        }
        int c = 0;
        double area_sum = 0;
        for(int j = 0; j < N && c < K - 1; j++){
            if(!unavailable[j]){
                area_sum += pancakes[j].height_area;
                c++;
            }
        }
        if(c < K - 1)
            continue;
        area_sum += pancakes[i].height_area;
        area_sum += pancakes[i].radius * pancakes[i].radius * PI;
        if(area_sum > ans)
            ans = area_sum;
    }
}

int main(){
    cin >> T;
    for(int t = 1; t <= T; t++){
        cin >> N >> K;
        for(int i = 0; i < N; i++){
            cin >> pancakes[i].radius;
            cin >> pancakes[i].height;
            pancakes[i].height_area = 2 * PI * pancakes[i].radius * pancakes[i].height;
        }
        sort(pancakes, pancakes + N, compare);
        calc();
        printf("Case #%d: %.9lf\n", t, ans);
    }
    return 0;
}

