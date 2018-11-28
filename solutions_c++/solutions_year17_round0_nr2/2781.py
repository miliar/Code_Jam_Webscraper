#include <bits/stdc++.h>
using namespace std;
#define rep(i,a,b) for(int i = (a); i < (b); i++)
#define iter(it,c) for(__typeof((c).begin()) it = (c).begin(); it != (c).end();++it)
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef long long ll;
const int INF = ~(1<<31);
const double pi = acos(-1);

bool checkzero(vi k) {
    rep(i,0,k.size()) if(k[i] == 0) return true;
    return false;
}

int lower(vi k, int at) {
    int mn = INF;
    for(int i = at-1; at >= 0; at--) mn = min(mn,k[i]);
    return mn;
}
bool valid(vi k) {
    reverse(k.begin(), k.end());
    vi ne = k;
    sort(ne.begin(), ne.end());
    rep(i,0,k.size()) if(k[i] != ne[i]) return false;
    return true;
}
ofstream fout("ans.txt");
void draw(vi k) {
    for(int i = k.size()-1; i >= 0; i--) {
        if((i == k.size()-1 && k[i] == 0)) continue;
        else fout << k[i];
    }
    fout << endl;
}

int main() {
	cin.sync_with_stdio(false);
    int n;
    cin >> n;
    rep(i,0,n) {
        string s;
        cin >> s;
        fout << "Case #" << i+1 << ": ";
        vi k;
        rep(a,0,s.size()) k.push_back(s[a]-'0');
        reverse(k.begin(), k.end());
        while(true) {
            rep(a,0,k.size()) {
                if(valid(k)) break;
                int mn = lower(k,a);
                if(mn < k[a]) {
                    k[a]--;
                    rep(z,0,a) k[z] = 9;
                    if(valid(k)) break;
                }
            }
            break;
            if(valid(k)) break;
        }
        draw(k);
    }
	return 0;
}

