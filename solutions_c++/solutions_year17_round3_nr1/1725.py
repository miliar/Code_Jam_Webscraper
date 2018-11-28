#include<iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

struct pancake {
    long long r, h;
};

bool compare(pancake a, pancake b) {
    return a.r < b.r;
}

int main() {
    int testCases;
    cin >> testCases;
    for (int testCase = 1; testCase <= testCases; ++testCase) {
        int n, k;
        cin >> n >> k;
        vector<pancake> input(n);
        for (int i = 0; i < input.size(); ++i) {
            cin >> input[i].r >> input[i].h;
        }
        sort(input.begin(), input.end(), compare);
        priority_queue<long long, std::vector<long long>, std::greater<long long>> qProd;
        long long prodSum = 0;
        long long MaxArea = 0;
        for (int i = 0; i < input.size(); ++i) {
            if (qProd.size() < k) {
                qProd.push(input[i].r * input[i].h);
                prodSum += input[i].r * input[i].h;
                MaxArea = input[i].r * input[i].r + 2 * prodSum;
            } else {
                prodSum += (input[i].r * input[i].h) - qProd.top();
                qProd.pop();
                qProd.push(input[i].r * input[i].h);
                MaxArea = max(MaxArea, input[i].r * input[i].r + 2 * prodSum);
            }
        }
        float m = MaxArea;
        m = (float) (m * 3.14159265359);
        printf("Case #%d: %f\n", testCase, m);

    }
}