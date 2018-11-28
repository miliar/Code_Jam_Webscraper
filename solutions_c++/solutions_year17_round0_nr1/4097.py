#include <iostream>
#include <vector>
#include <string.h>
#include <string>
#include <map>
#include <stdio.h>
#include <stack>
#include <queue>
#include <deque>
#include <cmath>
#include <algorithm>
#define fs first
#define sc second
#define sqr(x) (x)*(x)
#define ONLINE_JUDGE
using namespace std;

int t,k,it=0;
string s;

void Solve(string s, int k, int it){
    int ans = 0;
    for (int i=0; i< int(s.size())-k+1; i++){
        if (s[i] == '-'){
            ans++;
            for (int j=i; j<i+k; j++){
                if (s[j] == '-') s[j] = '+';
                else s[j] = '-';
            }
        }
    }
    cout<<"Case #"<<it<<": ";
    for (int i=0; i< (int) s.size(); i++){
        if (s[i] == '-'){
            cout<<"IMPOSSIBLE"<<endl;
            return;
        }
    }
    cout<<ans<<endl;
}

int main(){
    freopen("input.txt", "r", stdin);
    #ifdef ONLINE_JUDGE
        freopen("A.txt", "w", stdout);
    #endif // ONLINE_JUDGE
    ios_base::sync_with_stdio(false);
    cin>>t;
    while (t--){
        cin>>s>>k;
        Solve(s,k,++it);
    }
    #ifdef ONLINE_JUDGE
        fclose(stdout);
    #endif // ONLINE_JUDGE
    return 0;
}
