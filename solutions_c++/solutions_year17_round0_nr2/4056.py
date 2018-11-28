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
typedef long long ll;

int t, it;
ll n;

bool isTidy(ll m){
    int old = 9;
    while (m>0){
        if (m%10 > old) return false;
        old = m%10;
        m /= 10;
    }
    return true;
}

string toString(ll n){
    string ans = "";
    while (n>0){
        ans += (n%10 + '0');
        n/=10;
    }
    int sz = ans.size();
    for (int i=0; i<sz/2; i++) swap(ans[i], ans[sz-1-i]);
    return ans;
}

ll toNumber(string temp){
    ll ans = 0;
    for (int i=0; i<(int) temp.size(); i++){
        ans = ans * 10 + (temp[i] - '0');
    }
    return ans;
}

ll Solve(ll n){
    if (isTidy(n)) return n;
    string temp = toString(n);
    bool isFound = false;
    for (int i=1; i<int(temp.size()); i++){
        if (isFound) temp[i] = '9';
        else{
            if (temp[i] < temp[i-1]){
                temp[i] = '9';
                temp[i-1] = (temp[i-1]-'0'+9)%10 + '0';
                isFound = true;
            }
        }
    }
    return Solve(toNumber(temp));
}

int main(){
    freopen("input.txt", "r", stdin);
    #ifdef ONLINE_JUDGE
        freopen("B.txt", "w", stdout);
    #endif // ONLINE_JUDGE
    ios_base::sync_with_stdio(false);
    cin>>t;
    while (t--){
        cin>>n;
        cout<<"Case #"<<++it<<": ";
        cout<<Solve(n)<<endl;
    }
    #ifdef ONLINE_JUDGE
        fclose(stdout);
    #endif // ONLINE_JUDGE
    return 0;
}

