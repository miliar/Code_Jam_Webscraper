#include <bits/stdc++.h>
using namespace std;
#define rep(i,a,b) for(ll i = (a); i < (b); i++)
#define iter(it,c) for(__typeof((c).begin()) it = (c).begin(); it != (c).end();++it)
typedef long long ll;
typedef pair<ll,ll> ii;
typedef vector<ll> vi;
typedef vector<ii> vii;
const ll INF = ~(1<<31);
const double pi = acos(-1);

int main() {
	cin.sync_with_stdio(false);
    ofstream fout("ans.txt");
    ifstream fin("in.in");
    ll n;
    cin >> n;
    rep(i,0,n) {
        priority_queue<ll> k;
        ll m,q;
        cin >> m >> q;
        fout << "Case #" << i+1 << ": ";
        if(m <= q) fout << "0 0" << endl;
        else {
            map<ll,ll> got;
            got.clear();
            k.push(m-1);
            got[m-1]++;
            ll peps = q;
            q--;
            while(true) {
                ll at = k.top();
                k.pop();
                ll howmany = got[at];
                got.erase(at);
                if(howmany >= peps) { // found
                    if(at == 0) {
                        fout << "0 0" << endl;
                        break;
                    }
                    else {
                        ll want = at/2;
                        ll first = want;
                        ll second = at-want;
                        fout << second << " " << first << endl;
                        break;
                    }
                } else { // not found
                    peps -= howmany;
                    ll want = at/2;
                    ll first = want-1;
                    ll second = at-want-1;
                    if(got.find(first) != got.end()) {
                        got[first] += howmany;
                    } else {
                        got[first] = howmany;
                        k.push(first);
                    }
                    if(got.find(second) != got.end()) {
                        got[second] += howmany;
                    } else {
                        got[second] = howmany;
                        k.push(second);
                    }
                }
            }
        }
    }
	return 0;
}

