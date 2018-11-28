#include<bits/stdc++.h>

#define PB push_back
#define MP make_pair
#define F first
#define S second

#define FRI freopen("B-large.in","r",stdin)
//#define FRI freopen("B.in","r",stdin)
#define FRO freopen("B-large.out","w",stdout)
#define debug(args...) {dbg,args; cerr<<endl;}
#define DB(x) #x"=>",x
#define RAD(x) ((x*PI)/180)
#define NEX(x) ((x)==n-1?0:(x)+1)
#define PRE(x) ((x)==0?n-1:(x)-1)
#define DEG(x) ((x*180)/PI)

#define EPS 1e-12
#define INF 1000000007
#define MOD 1000000007
#define MAXN 100005
using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef long double LD;

const double PI=acos(-1.0);

struct debugger{
    template<typename T> debugger& operator , (const T& v){
        cerr<<v<<" ";
        return *this;
    }
}dbg;

bool isOkay(int n) {
    int i;
    vector<int>digits;
    while(n!=0) {
        digits.PB(n%10);
        n/=10;
    }
    reverse(digits.begin(),digits.end());
    for(i=0;i<digits.size()-1;i++) {
        if(digits[i]>digits[i+1]) {
            return false;
        }
    }
    return true;
}

void solve(int &kase) {
    LL n,i,j,k,trueNo=0,gotNo=0;
    vector<int>digits;
    cin>>n;
//    for(i=n;i>=1;i--) {
//        if(isOkay(i)) {
//            trueNo=i;
//            break;
//        }
//    }
    while(n!=0) {
        digits.PB(n%10);
        n/=10;
    }
    digits.PB(0);
    reverse(digits.begin(),digits.end());
    for(i=0;i<digits.size()-1;i++) {
        if(digits[i]>digits[i+1]) {
            for(j=i;j>=0;j--) {
                digits[j]--;
                if(digits[j]>=digits[j-1]) {
                    break;
                }
            }
            for(++j;j<digits.size();j++) {
                digits[j]=9;
            }
            break;
        }
    }
    printf("Case #%d: ",++kase);
    for(i=(digits[1]==0?2:1);i<digits.size();i++) {
        printf("%d",digits[i]);
//        gotNo*=10;
//        gotNo+=digits[i];
    }
//    if(trueNo!=gotNo) cout<<trueNo<<"!="<<gotNo;
    printf("\n");
}

int main() {
    FRI;
    FRO;
    int t=0,T;
    scanf("%d",&T);
    while(t<T) {
        solve(t);
    }
    return 0;
}
