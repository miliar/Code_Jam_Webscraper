#include <bits/stdc++.h>
using namespace std;

#define fi          "input.txt"
#define fo          "output.txt"
#define fileopen    freopen(fi,"r",stdin);freopen(fo,"w",stdout)
#define FOR(i,l,r)  for(int i=(int)(l);i<=(int)(r);i++)
#define FORD(i,l,r) for(int i=(int)(l);i>=(int)(r);i--)
#define xy          pair<int64,int>
#define int64       long long
#define ld          long double
#define X           first
#define Y           second
#define pb          push_back
#define init(a,v)   memset(a,v,sizeof(a))
#define Sz(s)       (int)(s.size())
#define EL          cout<<endl
#define digit(x)    ('0'<=x&&x<='9')
#define forever     while (true)
#define ran(l,r)    ((1LL*rand()*rand())%((int)(r)-(int)(l)+1)+(int)(l))

const int OO = (int) 2e9+5;
const int MOD = (int) 1e9+7;
const long double Pi = 3.141592653589793238;
const int N = (int) 5e2+5;

char s[N][N];
int x[2][26],y[2][26],chars[26],n,m,nc;
bool has[26];

void expandTop(int idx) {
    int left = y[0][idx];
    int right = y[1][idx];
    int top = x[0][idx];
    bool stop = false;
    while (!stop && top>1) {
        FOR(i,left,right) {
            if (s[top-1][i]!='?' && s[top-1][i]!=(char)('A'+idx)) {
                stop = true;
                break;
            }
        }
        if (!stop) {
            FOR(i,left,right) {
                s[top-1][i] = (char)('A'+idx);
            }
            top-=1;
        }
    }
    x[0][idx] = top;
}

void expandLeft(int idx) {
    int top = x[0][idx];
    int bot = x[1][idx];
    int left = y[0][idx];
    bool stop = false;
    while (!stop && left>1) {
        FOR(i,top,bot) {
            if (s[i][left-1]!='?' && s[i][left-1]!=(char)('A'+idx)) {
                stop = true;
                break;
            }
        }
        if (!stop) {
            FOR(i,top,bot) {
                s[i][left-1] = (char)('A'+idx);
            }
            left-=1;
        }
    }
    y[0][idx] = left;
}

void expandRight(int idx) {
    int top = x[0][idx];
    int bot = x[1][idx];
    int right = y[1][idx];
    bool stop = false;
    while (!stop && right+1<=m) {
        FOR(i,top,bot) {
            if (s[i][right+1]!='?' && s[i][right+1]!=(char)('A'+idx)) {
                stop = true;
                break;
            }
        }
        if (!stop) {
            FOR(i,top,bot) {
                s[i][right+1] = (char)('A'+idx);
            }
            right+=1;
        }
    }
    y[1][idx] = right;
}

void solve(int _case) {
    cin>>n>>m;
    nc = 0;
    FOR(i,0,25) {
        x[0][i] = y[0][i] = OO;
        x[1][i] = y[1][i] = 0;
    }
    init(has,false);
    FOR(i,1,n) cin>>(s[i]+1);
    FOR(i,1,n) FOR(j,1,m) {
        if (s[i][j]!='?') {
            if (!has[s[i][j]-'A']) {
                chars[++nc] = s[i][j]-'A';
                has[s[i][j]-'A'] = true;
            }
            int val = s[i][j]-'A';
            if (s[i][j]=='C') {
                n++;n--;
            }
            x[0][val] = min(x[0][val],i);
            x[1][val] = max(x[1][val],i);
            y[0][val] = min(y[0][val],j);
            y[1][val] = max(y[1][val],j);
        }
    }
    FOR(idx,1,nc) {
        int c = chars[idx];
        FOR(i,x[0][c],x[1][c])
            FOR(j,y[0][c],y[1][c])
                s[i][j] = (char)('A'+c);
    }
    FOR(i,1,n) {
        FOR(j,1,m) {
            if (s[i][j]!='?' && has[s[i][j]-'A']) {
                has[s[i][j]-'A'] = false;
                expandTop(s[i][j]-'A');
                expandLeft(s[i][j]-'A');
                expandRight(s[i][j]-'A');
            }
        }
    }
    FOR(i,1,n) FOR(j,1,m)
        if (s[i][j]=='?')
            s[i][j]=s[i-1][j];
    cout<<"Case #"<<_case<<":"<<endl;
    FOR(i,1,n) {
        FOR(j,1,m) cout<<s[i][j];
        EL;
    }
}

int main() {
    fileopen;
    int T;cin>>T;
    FOR(c,1,T) {
        solve(c);
    }
}
