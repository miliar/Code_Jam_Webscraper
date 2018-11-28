#include <bits/stdc++.h>
#define rep(i, a, n) for(int i = a; i < n; i++)
#define repb(i, a, b) for(int i = a; i >= b; i--)
#define all(a) a.begin(), a.end()
#define o(a) cout << a << endl
#define int long long
#define fi first
#define se second
using namespace std;
typedef pair<int, int> P;

// void InitRandom(){
//     int now=time(0);
//     srand(now);
// }

string change_to_s(int n){
    stringstream ss; ss<<n;
    return ss.str();
}

// bool check(int a){
//     string s = change_to_s(a);
//     rep(i, 1, s.size()){
//         if(s[i - 1] > s[i]) return false;
//     }
//     return true;
// }

// int test(int n){
//     for(int i = n; i >= 1; i--){
//         if(check(i)) return i;
//     }
// }

signed main(){
    // InitRandom();
    int t;
	cin >> t;
	for(int ti = 1; ti <= t; ti++){
        int n;
        cin >> n;
        string s = change_to_s(n);
        int l = s.size();
        string t = "";
        bool f = false;
        rep(i, 0, l){
            if(!f){
                if(i != l - 1 && s[i] > s[i + 1]){
                    f = true;
                    t += (s[i] - 1);
                }else{
                    t += s[i];
                }
            }else{
                t += '9';
            }
        }
        bool g = true;
        rep(i, 1, t.size()){
            if(t[i - 1] > t[i]) g = false;
        }
        if(!g){
            t = "";
            if(s[0] != '1') t += (s[0] - 1);
            rep(i, 1, s.size()) t += '9';
        }
        while(t[0] == '0'){
            t = t.substr(1);
        }
		cout << "Case #" << ti << ": " << t << endl;            
	}
}