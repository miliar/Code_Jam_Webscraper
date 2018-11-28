#include <iostream>
#include <bits/stdc++.h>
using namespace std;
typedef vector<int> vi;
typedef string sg;
int main(){
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T;
    cin >> T;
    for(int i = 1;i <= T;i++){
        string s;
        int k;
        cin >> s >> k;
        int len = s.length();
        vi ct;
        ct.assign(k+10,0);
        for(int j = 0;j < len;j++){
            if(s[j] == '-') ct[j%k] ^= 1;
        }
        bool im = false;
        for(int j = 0;j < k - 1; j++){
            if(ct[j] != ct[j+1]) im = true;
        }
        if(im){
            printf("Case #%d: IMPOSSIBLE\n",i);
            continue;
        }
        else{
            int ans = 0,pre = -1,mark = 0;
            queue<int> q;
            for(int j = 0; j < len; j++){
                if(pre == -1){
                    if(s[j] == '-'){
                        mark++;
                        ans++;
                        pre = j;
                        continue;
                    }
                    else{
                        continue;
                    }
                }
                else{
                    //clear marker
                    if(j - pre >= k){
                        pre = -1;mark--;
                    }
                    if((s[j] == '+' && mark % 2 == 1) || (s[j] == '-' && mark % 2 == 0)){
                        q.push(j);
                        mark++;
                        ans++;
                    }
                    if(!q.empty() && pre == -1){
                        pre = q.front();
                        q.pop();
                    }
                }
            }
            printf("Case #%d: %d\n",i,ans);
        }
    }
    return 0;
}
