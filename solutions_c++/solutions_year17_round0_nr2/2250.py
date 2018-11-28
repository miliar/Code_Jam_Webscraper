/// In the name of God
#include <bits/stdc++.h>
#define int long long
using namespace std;
typedef pair<int,int> pii;
typedef long long ll;
typedef long double ld;
typedef vector<int> vi;

#define y1 def1
#define X first
#define Y second
#define endl '\n'
#define all(o) o.begin(), o.end()
#define IOS ios::sync_with_stdio(0), cin.tie(0)
string tos(int x){
    string s;
    while(x){
        s += string(1, '0'+x%10);
        x/=10;
    }
    reverse(all(s));
    return s;
}
bool isval(string s){
    if(s[0] == '0') return 0;
    for(int i=1; i<s.size(); i++)
        if(s[i - 1] > s[i]) return 0;
    return 1;
}
string gg(int x){
    string s = tos(x);
    if(isval(s)) return s;
    int k = s.size();
    string jav;
    for(int len=0; len<k; len++){
        string t;
        for(int i=0; i<len; i++)
            t += s[i];
        if(s[len] == '0') continue;
        t += string(1, s[len] - 1);
        while(t.size() != s.size()) t += '9';
        if(isval(t))
            jav = max(jav, t);
    }
    if(jav != "") return jav;
    return string(k - 1, '9');
}
main(){
    IOS;
    freopen("BL.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T;
    cin >> T;
    for(int it=0; it<T; it++){
        int x;
        cin >> x;
        cout << "Case #" << it+1 << ": " << gg(x) << endl;
    }
}
