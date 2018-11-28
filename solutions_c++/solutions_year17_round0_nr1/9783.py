#include<iostream>
#include<cstdio>
#include<string>
#include<queue>
#include<map>

using namespace std;

int main() {
    int tc, tt = 1;
    scanf("%d", &tc);
    while(tt <= tc) {
        string str;
        int k, min_steps = -1;
        cin >> str >> k; 
        queue<string> q;
        queue<int> ans;
        map<string, int> vis;
        q.push(str);
        ans.push(0);
        vis[str]++;
        while(!q.empty()) {
            string s = q.front(); q.pop();
            int moves = ans.front(); ans.pop();
            map<char, int> check;
            for(int i=0; i<(int)s.size(); i++) {
                check[s[i]]++;
            }
            if((int)check.size() == 1 and check.find('+') != check.end()) {
                min_steps = moves;
                break;
            }
            for(int i=0; i<=(int)s.size()-k; i++) {
                string low = "", mid = "", high = "";
                for(int j=0; j<i; j++) {
                    low += s[j];
                }
                for(int j=i+k; j<(int)s.size(); j++) {
                    high += s[j];
                }
                for(int j=i; j<i+k; j++) {
                    if(s[j] == '+') {
                        mid += '-';
                    } else {
                        mid += '+';
                    }
                }
                string child = low + mid + high;
                if(vis.find(child) == vis.end()) {
                    q.push(child);
                    ans.push(moves+1);
                    vis[child]++;
                }
            }
        }
        if(min_steps == -1) {
            printf("Case #%d: IMPOSSIBLE\n", tt);
        } else {
            printf("Case #%d: %d\n", tt, min_steps);
        }
        tt++;
    }
}
