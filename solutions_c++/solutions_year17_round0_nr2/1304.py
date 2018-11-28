//
//  main.cpp
//  test
//
//  Created by 商占仝 on 2017/3/22.
//  Copyright © 2017年 bytedance. All rights reserved.
//

#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
using namespace std;

const int maxn = 1005;

char str[maxn];
int k, len;

int main(){
    //freopen("B-large.in", "r", stdin);
    //freopen("out.txt", "w", stdout);
    int T, cases = 0;
    scanf("%d", &T);
    while(T--){
        scanf("%s", str);
        len = (int)strlen(str);
        int pos = -1, rc = -1;
        for(int i = 0; i < len - 1; ++i){
            if(str[i] > str[i + 1]){
                pos = i;
                break;
            }
        }
        char *ans = str;
        if(pos != -1){
            for(int i = pos; i >= 0; --i){
                if(str[i] < str[pos]){
                    rc = i;
                    break;
                }
            }
            if(rc == -1){
                if(str[0] == '1'){
                    ans = str + 1;
                }
            }
            str[rc + 1]--;
            for(int i = rc + 2; i < len; ++i) str[i] = '9';
        }
        
        printf("Case #%d: %s\n", ++cases, ans);
    }
    return 0;
}
