/// In the name of God
#include <bits/stdc++.h>
//#define int long long
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
string res = "IMPOSSIBLE";
string get(int c1,int c2,int c4){
    vector<pii> p;
    if(c1 < 0 || c2 < 0 || c4 < 0) return res;
    p.push_back({c1, 1});
    p.push_back({c2, 2});
    p.push_back({c4, 4});
    sort(all(p));
    int n = c1 + c2 + c4;
    if(p.back().X * 2 > n){
        //cout << "WAY" << endl;
        return res;
    }
    vector<char> v;
    for(int i=0; i<3; i++)
        for(int j=0; j<p[i].X; j++)
            v.push_back('0' + p[i].Y);
    int cur = 0;
    vi pos;
    string s = string(n, '0');
    if(n % 2 == 1){
        for(int i=0; i<n; i++){
            s[cur] = v.back();
            v.pop_back();
            cur = (cur + 2) % n;
        }
        return s;
    }
    for(int i=0; i<n; i+=2){
        s[i] = v.back();
        v.pop_back();
    }
    for(int i=1; i<n; i+=2){
        s[i] = v.back();
        v.pop_back();
    }
    return s;
}
int cnt[10];
map<int,char> mp;

string conv(string s){
    if(s == res) return s;
    string t;
    for(int i=0; i<s.size(); i++)
        t += mp[s[i] - '0'];
    return t;
}
int main(){
    IOS;
    mp[1] = 'R';
    mp[3] = 'O';
    mp[2] = 'Y';
    mp[6] = 'G';
    mp[4] = 'B';
    mp[5] = 'V';
    freopen("BS.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T;
    cin >> T;
    for(int it=0; it<T; it++){
        int n;
        cin >> n;
        cin >> cnt[1] >> cnt[3] >> cnt[2] >> cnt[6] >> cnt[4] >> cnt[5];
        cnt[4] -= cnt[3];
        cnt[2] -= cnt[5];
        cnt[1] -= cnt[6];
        //cout << cnt[4] << " " << cnt[2] << " " << cnt[1] << endl;
        //cout << cnt[1] << " " << cnt[2] << " " << cnt[4] << ":D" << endl;
        string ans = get(cnt[1], cnt[2], cnt[4]);
        //cout << "haha" << ans << endl;
        cout << "Case #" << it + 1 << ": ";
        if(ans == res){
            cout << res << endl;
            continue;
        }
        //cout << "HAHA" << ans << endl;
        if((cnt[3] && !cnt[4]) || (cnt[5] && !cnt[2]) || (cnt[6] && !cnt[1])){
            cout << res << endl;
            continue;
        }
        for(int i=1; i<=4; i*=2){
            if(cnt[i ^ 7] == 0) continue;
            int p;
            int N = ans.size();
            for(int j=0; j<ans.size(); j++)
                if(ans[j] == char('0' + i))
                    p = j;
            string tt;
            tt += char('0' + (i ^ 7));
            tt += char('0' + (i ^ 0));
            string lef = ans.substr(0, p);
            string rig = ans.substr(p+1, N - p);
            for(int j=0; j<cnt[i ^ 7]; j++)
                lef += tt;
            lef += rig;
            ans = lef;
        }
        cout << conv(ans) << endl;
    }
}
