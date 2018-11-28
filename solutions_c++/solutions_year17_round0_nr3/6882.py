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
struct Part {
    LL left;
    LL right;
};
int main() {
    int T;
    cin>>T;
    int ansc = 1;
    LL N, K;
    while(T-- > 0) {
        cin>>N>>K;
        Part p1;
        p1.left = 0;
        p1.right = N + 1;
        vector<Part> parts;
        parts.pb(p1);
        LL i;
        for(i = 0; i < K; i++) {
            LL j;
            LL mInd = 0; 
            for(j = 1; j < parts.size(); j++) {
                if(parts[j].right - parts[j].left > parts[mInd].right - parts[mInd].left) {
                    mInd = j;
                }
            }
            LL mid = parts[mInd].left+ (parts[mInd].right- parts[mInd].left) / 2;
            if(i == K - 1) {
               cout<<"Case #"<<ansc<<": "<<parts[mInd].right - mid - 1<<" "<<mid - parts[mInd].left - 1;
               cout<<endl;
               break;
            }
            Part p2;
            p2.left = mid; p2.right = parts[mInd].right;
            parts.pb(p2);
            parts[mInd].right = mid;
        }
        ansc++;
    }
}
