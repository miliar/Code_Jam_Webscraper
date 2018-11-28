//
// Created by ruby on 8/04/17.
//
#include <cstdio>
#include <string>
using namespace std;
int n;

bool tidy(int i){
    string s = to_string(i);
    for (int j = 1; j < s.length(); ++j){
        if (s[j] < s[j-1]){
            return false;
        }
    }
    return true;
}
int main(){
    scanf("%d\n", &n);
    int num;
    for (int i = 0; i < n; ++i){
        scanf("%d\n", &num);
        for (int j = num; j >= 0; --j){
            if (tidy(j)){
                printf("Case #%d: %d\n", i+1, j);
                break;
            }
        }
    }
    return 0;
}
