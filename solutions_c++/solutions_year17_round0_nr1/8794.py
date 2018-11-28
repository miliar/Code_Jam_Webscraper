#include<stdio.h>
#include<fstream>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<iostream>
#include<vector>
#include<cassert>
#include<sstream>
#include<map>
#include<set>
#include<stack>
#include<queue>
#include<algorithm>
using namespace std;
#define pb push_back
#define mp make_pair
#define clr(x) x.clear()
#define sz(x) ((int)(x).size())
#define F first
#define S second
#define REP(i,a,b) for(i=a;i<b;i++)
#define rep(i,b) for(i=0;i<b;i++)
#define rep1(i,b) for(i=1;i<=b;i++)
#define pdn(n) printf("%d\n",n)
#define sl(n) scanf("%lld",&n)
#define sd(n) scanf("%d",&n)
#define pn printf("\n")
typedef pair<int,int> PII;
typedef vector<PII> VPII;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef long long LL;
#define MOD 1000000007
void flip(int i, int K, vector<bool>& s) {
    int temp = i;
    for(int j = i; j < temp + K; j++) {
        s[j] = !s[j];
    }
}
int main() {
    int T, K;
    ifstream ip;
    ofstream of;
    ip.open("A-large.in");
    of.open("output.op");
    ip>>T;
    int ansc = 1;
    while(T-- >0){
        vector<bool> s;
        bool flag = true;
        string t;
        ip>>t;
        int K;
        ip>>K;
        int i;
        int siz = t.size();
        REP(i,0,siz) {
            if(t[i] == '+')
                s.pb(true);
            else
                s.pb(false);
        }
        int ans = 0;
        for(i = 0; i <= siz - K - 1; i++) {
            if(s[i])
                continue;
            else {
                flip(i, K, s);
                ans++;
            }
        }
        bool tt = s[siz - K];
        flag = true;
        for(i = siz - K + 1; i < siz; i++) {
            if( tt != s[i]) {
                flag = false;
                break;
            }
        }
        of<<"CASE #"<<ansc<<": ";
        if(!flag)
            of<<"IMPOSSIBLE"; 
        else {
            if(!tt)
                of<<ans+1;
            else
                of<<ans;
        }   
        of<<endl;
        ansc++;       
    }
    ip.close();
    of.close();
}
