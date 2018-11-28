//
//  main.cpp
//  round2
//
//  Created by didi on 2017/5/13.
//  Copyright © 2017年 didi. All rights reserved.
//

#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <math.h>
#include <iomanip>
using namespace std;

ifstream in("/Users/didi/Desktop/round2/round2/A-large.in");
ofstream out("/Users/didi/Desktop/round2/round2/A-large.out");

double f[210][210];

int deal_2(int* cnt){
    int ret = 0;
    ret += cnt[0];
    ret += ceil(1.0*cnt[1]/2);
    return ret;
}

int deal_3(int* cnt){
    int ret = 0;
    ret += cnt[0];
    ret += min(cnt[1],cnt[2]);
    int tmp = max(cnt[1],cnt[2])-min(cnt[1],cnt[2]);
    ret += ceil(1.0*tmp/3);
    return ret;
}

int deal_4(int* cnt){
    int ret = 0;
    ret += cnt[0];
    ret += min(cnt[1],cnt[3]);
    int re13 = max(cnt[1],cnt[3])-min(cnt[1],cnt[3]);
    
    int choose1 = cnt[2]/2;
    int re2 = cnt[2]%2;
    if (re2>0 && re13>1){
        choose1++;
        re2 = 0;
        re13 -= 2;
    }
    choose1 += re13/4;
    if (re2>0 || re13%4>0) choose1++;
    
    int choose2 = 0;
    if (re13/2<cnt[2]){
        choose2 += re13/2;
        re2 = cnt[2] - re13/2;
        choose2 += re2/2;
        if (re13%2>0 || re2%2>0) choose2++;
    }else{
        choose2 += cnt[2];
        re13 -= (2*cnt[2]);
        choose2 += re13/4;
        if (re13%4>0) choose2++;
    }
    
    ret += max(choose1, choose2);
    return ret;
}

void solve(int test){
    out << "Case #" << test << ": ";
    int cnt[4];
    for (int i=0; i<4; i++) cnt[i] = 0;
    int N, P;
    in >> N >> P;
    int G[110];
    for (int i=0; i<N; i++){
        in >> G[i];
        cnt[G[i]%P]++;
    }
    int ans = 0;
    switch (P) {
        case 2:
            ans = deal_2(cnt);
            break;
        case 3:
            ans = deal_3(cnt);
            break;
        case 4:
            ans = deal_4(cnt);
            break;
        default:
            break;
    }
    out << ans << endl;
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
