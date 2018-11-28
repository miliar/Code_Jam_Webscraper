#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>
#include <cstdio>
using namespace std;
typedef long long llint;

vector<int> vec;

void get_bit(vector<int> & vec, llint num) {
    vec.clear();
    while (num) {
        vec.push_back(num % 10);
        num /= 10;
    }
    reverse(vec.begin(), vec.end());
}

bool check(vector<int> & vec) {
    bool flag = true;
    for (int i = (int)vec.size()-1; i >= 1; i--) {
        if (vec[i] < vec[i-1]) {
            flag = false;
            break;
        }
    }
    return flag;
}

int main() {
    int t;
    scanf("%d", &t);
    for (int tt = 1; tt <= t; tt++) {
        llint num;
        scanf("%lld", &num);
        get_bit(vec, num);
        if (vec.size() == 1 || check(vec)) {
            printf("Case #%d: %lld\n", tt, num);
            continue;
        }
        while (!check(vec)) {
            for (int i = (int)vec.size()-1; i >= 1; i--) {
                if (vec[i] < 0 || vec[i] < vec[i-1]) {
                    vec[i] = 9;
                    vec[i-1]--;
                    for (int j = i+1; j < vec.size(); j++)
                        vec[j] = 9;
                }
            }
        }
        if (vec[0] <= 0)
            vec.erase(vec.begin());
        printf("Case #%d: ", tt);
        for (int i = 0; i < vec.size(); i++)
            printf("%d", vec[i]);
        putchar('\n');
    }
}
