
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
map<string, int> visited;

char swapC (char a){
    if(a == '-')
        return '+';
    else return '-';
}

string replaceS(string a, int sI){
    string b = a;
    for (int i = sI; i < sI + n; i++) {
        b[i] = swapC(b[i]);
    }
    return b;
}

int main(){
//    freopen("input.txt", "r", stdin);
//        freopen("oy.txt","w",stdout);
    scanf("%d",&T);
    for (int t = 1; t <= T; t++) {
        cin >> s;
        scanf("%d",&n);
        visited.clear();
        queue<string> q;
        q.push(s);
        visited.insert(pair<string, int>(s,0));
        while(!q.empty()){
            string u = q.front();
            q.pop();
            for (int i = 0; i <= s.length() - n; i++) {
                string ts= replaceS(u, i);
                if(visited.find(ts)==visited.end()){
                    q.push(ts);
                    visited.insert(pair<string, int>(ts, visited.at(u) + 1));
                }
            }
        }
        string ans = "";
        for (int i = 0 ; i < s.length(); i++) {
            ans += '+';
        }
        if(visited.find(ans) != visited.end())
            printf("Case #%d: %d\n",t, visited.at(ans));
        else printf("Case #%d: IMPOSSIBLE\n", t);
        
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