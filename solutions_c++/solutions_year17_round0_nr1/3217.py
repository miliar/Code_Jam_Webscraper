#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;
#define MAX 510

int solve(string s, int k){
    int r=0;
    for(int i=0;i<s.size();i++){
        while(s[i]=='+'){
            i++;
        }
        if(i==s.size()){
            break;
        }
        r++;
        if(i+k>s.size()){
            return -1;
        }
        for(int j=i;j<k+i;j++){
            s[j] == '+' ? s[j]='-' : s[j]='+';
        }
    }
    int temp=(int)s.size();
    for(int i=temp-1;i>=temp-k;i--){
        if(s[i]=='-'){
            return -1;
        }
    }
    return r;
}

int main() {
    //freopen("/Users/d/Documents/A-large.in", "rt", stdin);
    int n;
    cin >> n;
    for(int i=1;i<=n;i++){
        string s;
        int k;
        cin >> s >> k;
        int ans=solve(s, k);
        cout << "Case #" << i << ": ";
        if(ans==-1){
            cout << "IMPOSSIBLE" << endl;
        } else {
            cout << ans << endl;
        }
    }
    return 0;
}
