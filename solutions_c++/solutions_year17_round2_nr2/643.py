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
const int N = (int) 2e5+5;

const int R = 0;
const int O = 1;
const int Y = 2;
const int G = 3;
const int B = 4;
const int V = 5;
const char c[6] = {'R','O','Y','G','B','V'};

int cnt[6],tmp[6],n;
int t[1000][6],nt=0;

string solve(int test) {
    cin>>n;
    FOR(i,0,5) {
        cin>>cnt[i];
        tmp[i]=cnt[i];
    }
    if (cnt[O]>0 && cnt[O]>cnt[B]-(cnt[R]+cnt[V]+cnt[Y]+cnt[G]>0)) {
        return "IMPOSSIBLE";
    }
    if (cnt[G]>0 && cnt[G]>cnt[R]-(cnt[O]+cnt[V]+cnt[Y]+cnt[B]>0)) {
        return "IMPOSSIBLE";
    }
    if (cnt[V]>0 && cnt[V]>cnt[Y]-(cnt[R]+cnt[O]+cnt[B]+cnt[G]>0)) {
        return "IMPOSSIBLE";
    }
    string o="B",g="R",v="Y";
    FOR(i,1,cnt[O]) {
        o+="O";
        if (cnt[B]>1) {
            cnt[B]--;
            o+="B";
        }
    }
    FOR(i,1,cnt[G]) {
        g+="G";
        if (cnt[R]>1) {
            cnt[R]--;
            g+="R";
        }
    }
    FOR(i,1,cnt[V]) {
        v+="V";
        if (cnt[Y]>1) {
            cnt[Y]--;
            v+="Y";
        }
    }
    cnt[G]=cnt[O]=cnt[V]=0;
    if (test==3) {
        n++;n--;
    }
    int mx=0,sum=0;
    FOR(i,0,2) {
        mx=max(mx,cnt[i*2]);
        sum+=cnt[i*2];
    }
    if (mx>1 && mx>sum-mx) {
        return "IMPOSSIBLE";
    }
    string res ="";
    int x,fst=-1;
    while (sum>0) {
        x = 0;
        if (fst!=-1)
            x=fst;
        while (res.size()>0 && c[x]==res.back())
            x = (x+2)%6;
        FOR(i,0,2) {
            if (c[i*2]==res.back())
                continue;
            if (cnt[i*2]>cnt[x]) x = i*2;
        }
        if (fst==-1)
            fst=x;
        cnt[x]--;
        sum-=1;
        if (cnt[x]>0) {
            res+=c[x];
        } else {
            if (x==B) {
                res+=o;
            } else if (x==R) {
                res+=g;
            } else if (x==Y) {
                res+=v;
            }
        }
    }
    bool ok=true;
    FOR(i,0,Sz(res)-2) {
        char a = res[i];
        char b = res[i-1];
        if (a==b)
            ok=false;
        if (a=='O'&&b!='B')
            ok=false;
        if (a!='B'&&b=='O')
            ok=false;
        if (a=='G'&&b!='R')
            ok=false;
        if (a!='R'&&b=='G')
            ok=false;
        if (a=='V'&&b!='Y')
            ok=false;
        if (a!='Y'&&b=='V')
            ok=false;
    }
    FOR(i,0,Sz(res)-1) {
        if (res[i]=='R') cnt[R]++;
        if (res[i]=='O') cnt[O]++;
        if (res[i]=='Y') cnt[Y]++;
        if (res[i]=='G') cnt[G]++;
        if (res[i]=='B') cnt[B]++;
        if (res[i]=='V') cnt[V]++;
    }
    FOR(i,0,5) if (cnt[i]!=tmp[i]) {
        ok = false;
    }
    if ((int)res.size()!=n || !ok) {
        cout<<"Test "<<test<<" : ";
        FOR(i,0,5) cout<<tmp[i]<<" ";
        EL;
    }
    return res;
}

int main() {
    fileopen;
    int T;cin>>T;
    FOR(i,1,T) {
        string res=solve(i);
        if (res=="IMPOSSIBLE") {
            nt++;
            FOR(j,0,5)
                t[nt][j] = tmp[j];
        }
        printf("Case #%i: %s\n",i,res.c_str());
    }
//    cout<<nt<<endl;
//    FOR(i,1,nt) {
//        FOR(j,0,5) cout<<t[i][j]<<" ";
//        EL;
//    }
}
