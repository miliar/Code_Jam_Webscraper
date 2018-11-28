//
//  main.cpp
//  roundA
//
//  Created by didi on 2017/4/15.
//  Copyright © 2017年 didi. All rights reserved.
//

#include <iostream>
#include <string>
#include <fstream>
#include <vector>
using namespace std;

ifstream in("/Users/didi/Desktop/roundA/roundA/A-large.in");
ofstream out("/Users/didi/Desktop/roundA/roundA/A-large.out");

int check_end(string str, int start){
    int ret = -1;
    while (start+1<str.length() && str[start]==str[start+1] ) start++;
    ret = start;
    return ret;
}

int check(string str, int s, int e){
    int ret = 1;
    while (s <= e){
        if (str[s] != '?'){
            ret = 0;
            break;
        }
        s++;
    }
    return ret;
}

void solve(int test){
    out << "Case #" << test << ": " << endl;
    vector<string> map;
    int R,C;
    in >> R >> C;
    for (int i=0;i<R;i++){
        string str;
        in >> str;
        map.push_back(str);
    }
    vector<string> ans = map;
    int i = 0;
    int ctn = 1;
    while (ctn){
        ctn = 1;
        for (int j=0;j<C;j++){
            if (map[i][j] != '?'){
                ctn = 0;
                break;
            }
        }
        if (!ctn) break;
        i++;
    }
    int pre = i;
    while (i<R){
        string str = map[i];
        char now = '?';
        int j = 0;
        while (j<C){
            if (i>pre){
                int end = check_end(ans[i-1], j);
                if (check(str,j,end)){
                    for (int t=j;t<=end;t++){
                        ans[i][t] = ans[i-1][j];
                    }
                }else{
                    int t = j;
                    while (t<=end && map[i][t] == '?') t++;
                    for (int tmp=j;tmp<t;tmp++){
                        ans[i][tmp] = map[i][t];
                    }
                    now = map[i][t];
                    while (t<=end){
                        if (map[i][t] == '?'){
                            ans[i][t] = now;
                        }else{
                            now = ans[i][t];
                        }
                        t++;
                    }
                }
                j = end+1;
            }else{
                int t = j;
                while (t<C && map[i][t] == '?') t++;
                for (int tmp=j;tmp<t;tmp++){
                    ans[i][tmp] = map[i][t];
                }
                now = map[i][t];
                while (t<C){
                    if (map[i][t] == '?'){
                        ans[i][t] = now;
                    }else{
                        now = ans[i][t];
                    }
                    t++;
                }
                j += C;
            }
        }
        i++;
    }
    for (int i=0;i<pre;i++){
        for (int j=0;j<C;j++){
            ans[i][j]=ans[pre][j];
        }
    }
    for (int i=0;i<R;i++){
        out << ans[i] << endl;
    }
}

int main(int argc, const char * argv[]) {
    int test = 0,T;
    in >> T;
    while (test++<T){
        solve(test);
    }
    in.close();
    out.close();
    return 0;
}
