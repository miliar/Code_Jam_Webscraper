#include<stdio.h>
#include<fstream>
#include<stdlib.h>
#include<string>
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
bool check(LL n){
    ostringstream ss;
    ss<<n;
    string s = ss.str();
    char t = s[0];
    int i;
    REP(i, 0, s.length()) {
        if(s[i] > t)
            t = s[i];
        else if(s[i] < t) 
            return false;
    }
    return true;
}
int main() {
    int T;
    cin>>T;
    int ansc = 1;
    while(T-- > 0){
        LL n;
        cin>>n;
        bool flag = false;
        while(n >= 0){
            flag = check(n);
            if(flag)
                break;
            n--;
        }
        if(flag)
            cout<<"Case #"<<ansc<<": "<<n<<endl;
        ansc++;
    }
}
