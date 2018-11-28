#include <bits/stdc++.h>
using namespace std;

string toStr(long long x){
    string ans = "";
    while(x){
        ans = (char)(x%10 + 48) + ans;
        x/=10;
    }
    return ans;
}

void solve(string& st, int x){
    if(x==0 || st[x-1]<=st[x]) return;
    for(int i=x; i<st.size(); i++) st[i] = '9';
    x--;
    while(st[x]=='0'){
        st[x] = '9';
        x--;
    }

    st[x] = (char)((int)(st[x])-1);
    solve(st, x);
}

int main(){
    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t = 0;
    cin >> t;
    for(int i=1; i<=t; i++){
        long long n;
        cin >> n;
        string st = toStr(n);
        for(int j=1; j<st.size(); j++){
            if(st[j-1]>st[j]){
                solve(st, j);
            }
        }
        int j = 0;
        while(st[j]=='0') j++;
        st = st.substr(j, st.size());
        cout << "Case #" << i << ": " << st << endl;
    }
    return 0;
}
