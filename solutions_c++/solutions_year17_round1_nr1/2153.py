#include <bits/stdc++.h>
using namespace std;

#define EACH(i,c) for(__typeof((c).begin()) i = (c).begin();i!=(c).end();i++)
#define FOR(i,a,b)  for(int i=(a);i<(b);i++)
#define dbg(e)  cout<<(#e)<<" : "<<e<<endl
#define set(v,i) memset(v,i,sizeof(v))
#define all(x) x.begin(),x.end()
#define sz(x) int((x).size())
#define REP(i,n) FOR(i,0,n)
#define pb  push_back
#define mp make_pair

typedef long long LL;

LL test;
vector<string> input;
int h, w;

bool isAll(string x) {
    REP(i, sz(x)) if (x[i] != '?') return false;
    return true;
}

string flowToRight(string x) {
    char last = ' ';
    REP(j, w) {
        if (x[j] != '?') last = x[j];
        if (x[j] == '?' && last != ' ') x[j] = last;
    }
    return x;
}

vector<string> flowToBottom(vector<string> x) {
    string last = "?";
    REP(i, h) {
        if (!isAll(x[i])) last = x[i];
        if (isAll(x[i]) && !isAll(last)) x[i] = last;
    }
    return x;
}

int main() {
    cin >> test;
    REP(tt, test) {
        input.clear();

        cin >> h >> w;
        //REP(i, h) cin >> input[i];
        string ip;
        REP(i,  h) {
            cin >> ip;
            input.pb(ip);
        }

        //cout << "processing individual columns" << endl;
        REP(i, h) {
            input[i] = flowToRight(input[i]);
            reverse(all(input[i]));
            //cout << input[i] << endl;
            input[i] = flowToRight(input[i]);
            reverse(all(input[i]));
            //cout << input[i] << endl;
        }
        input = flowToBottom(input);
        reverse(all(input));
        input = flowToBottom(input);
        reverse(all(input));

        cout << "Case #" << tt + 1 << ":" << endl;
        REP(i, h) cout << input[i] << endl;
    }
    return 0;
}
