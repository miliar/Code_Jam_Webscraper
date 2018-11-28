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

struct Part{
    int l, r, id;
};

bool cmp(Part p1, Part p2){
    return p1.l < p2.l;
}

signed main(){
    int tnum;
	cin >> tnum;
	for(int ti = 1; ti <= tnum; ti++){
        int ac, aj;
        cin >> ac >> aj;
        vector<P> dc(ac), dj(aj);
        vector<Part> dt;
        int timec = 0, timej = 0;
        rep(i, 0, ac){
            int l, r;
            cin >> l >> r;
            dc[i].first = l;
            dc[i].second = r;
            timec += r - l;
            dt. push_back((Part){l, r, 0});
        }
        rep(i, 0, aj){
            int l, r;
            cin >> l >> r;
            dj[i].first = l;
            dj[i].second = r;
            timej += r - l;
            dt. push_back((Part){l, r, 1});
        }
        sort(all(dc));
        sort(all(dj));
        sort(all(dt), cmp);
        dt. push_back((Part){dt[0].l + 1440, dt[0].r + 1440, dt[0].id});
        int ans = 0;
        int change = 0;
        int preid = dt[0].id;
        vector<int> inv[2];
        int invsum[2] = {};
        rep(i, 1, dt.size()){
            int nowid = dt[i].id;
            if(nowid == preid){
                inv[nowid]. push_back(dt[i].l - dt[i - 1].r);
                invsum[nowid] += dt[i].l - dt[i - 1].r;
            }else{
                change++;
                preid = nowid;
            }
        }
        ans = change;
        rep(i, 0, 2){
            sort(all(inv[i]));
            reverse(all(inv[i]));
        }
        // cout << timec << " " << invsum[0] << " " << timec + invsum[0] << endl;
        if(timec + invsum[0] > 720){
            int rest = timec + invsum[0] - 720;
            // cout << "!" << rest << endl;            
            rep(i, 0, inv[0].size()){
                rest -= inv[0][i];
                ans += 2;
                if(rest <= 0) break;
            }
        }else if(timej + invsum[1] > 720){
            int rest = timej + invsum[1] - 720;
            // cout << "!!" << rest << endl;
            
            rep(i, 0, inv[1].size()){
                rest -= inv[1][i];
                ans += 2;
                if(rest <= 0) break;
            }
        }
		cout << "Case #" << ti << ": " << ans << endl;
	}
}