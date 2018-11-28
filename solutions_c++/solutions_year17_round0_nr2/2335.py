#include <cstdio>
#include <vector>
#include <algorithm>
#include <iostream>
#include <utility>
#include <string>

using namespace std;

typedef long long lint;

int main() {
    int t;
    scanf("%d", &t);
    lint n;
    for(int CASE = 1; CASE <= t; CASE++) {
        scanf("%lld", &n);
        string l = to_string(n);
        for(int i = 1; i < l.length(); i++) {
            if(l[i] < l[i-1]) {
                int j = i-1;
                while(j > 0 && l[j-1] == l[i-1]) j--;
                l[j]--;
                for(int k = j+1; k < l.length(); k++) l[k] = '9';
                break;
            }
        }
        printf("Case #%d: %lld\n", CASE, stoll(l));
    }
    return 0;
}