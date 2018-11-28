#include <bits/stdc++.h>


using namespace std;

int t,T;

long long n,ans,a;

bool isTidy(long long a){
    string s = to_string(a);
    int n = s.length();
    for(int i = 0; i < n-1; i++){
        if(s[i] > s[i+1]){
            return false;
        }
    }
    return true;
}

int main(){
     freopen("b.in", "r", stdin);
     freopen("b.out", "w", stdout);
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> T;
    for(int t = 1; t <= T; t++){
        cin >> n;
        ans = n;
        a = 1;
        while(!isTidy(ans)){
            a*=10;
            ans = ans - (ans%a) - 1;
        }
        cout << "Case #" << t << ": " << ans << endl;
    }
    return 0;
}
