
#include <iostream>
#include <vector>
#include <string.h>
#include <stdlib.h>
#include <climits>
#include <algorithm>
#include <cmath>
#include <queue>
#include <map>
#include <stdio.h>

#define LL unsigned long long
using namespace std;
int const maxN = 10000 + 100;
int const maxM = 100000 + 5000;
int T, n,m;
string s;

int main(){
//    freopen("B-small-attempt0.in", "r", stdin);
//    freopen("oy.txt","w",stdout);
    scanf("%d",&T);
    int t = 0;
    while(T--){
        t++;
        cin >> s;
        char maxX;
        int index= -1;
        bool isNonDe = true;
        for (int i =0; i < s.length() - 1; i++) {
            
            if(index == -1 && s[i] >= s[i+1]){
                maxX = s[i];
                index = i;
            }
            if(s[i] > s[i+1]){
                isNonDe = false;
                break;
            }
        }
        if(isNonDe){
            printf("Case #%d: %s\n",t,s.c_str());
        }else{
            for (int i = s.length() - 1; i > index; i--) {
                s[i] = '9';
            }
            if(s[index] != '0'){
                s[index] -= 1;
            }else{
                while(s[index]==0){
                    s[index] = 9;
                    index--;
                }
                s[index]-=1;
            }
            if(s[0]=='0'){
//                string::iterator it = ;
                printf("Case #%d: %s\n",t, &s.at(1));
            }else
                printf("Case #%d: %s\n",t,s.c_str());
        }
    }
    
    return 0;
}

/*
 ---+-+--
 ++++-+--
 +++++-+-
 ++++++-+
 +++----+
 +++----+
 */