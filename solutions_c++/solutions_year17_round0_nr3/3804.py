#include <bits/stdc++.h>
using namespace std;

typedef vector<int> vi;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef pair<int,ii> iii;
typedef vector<pair<ii,int>> viii;
typedef vector<vi> vvi;
typedef vector<vii> vvii;
typedef map<int,int> mii;
typedef map<char,int> mci;
typedef priority_queue<int> pqi;
typedef priority_queue<ii> pqii;
typedef priority_queue<int,vi,greater<int>> pqmini;
typedef priority_queue<ii,vii,greater<ii>> pqminii;
typedef long long lli;

#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define si(n) scanf("%d",&n)
#define iout(n) printf("%d\n",n)
#define slli(n) scanf("%lld",&n)
#define lliout(n) printf("%lld\n",n)
#define FOR(i,n) for(int i=0;i<n;i++)

#define EPS 10e-9
#define PI 3.14159265359
#define EULER 2.7182818284
#define MOD 1000000007

//global variables
lli N,K;
lli INF=LLONG_MAX-(lli)INT_MAX;
lli MX[70]={0};
lli H=0;
//end global variables

void preprocess(void){
	return;
}

lli maxl(lli a,lli b){
    return (a>b)?a:b;
}

lli minl(lli a,lli b){
    return (a>b)?b:a;
}

void preCalc(void){
    FOR(i,70){
        MX[i]=0;
    }
    MX[0]=N;
    lli TN=N>>1;
    int i=1;
    while(TN){
        MX[i++]=TN;
        TN>>=1;
    }
    H=i-1;//N is at 0 height
}

pair<lli,lli> solve(lli TK){
    if(TK==0){
        lli P=(N+1)/2;
        return mp(N-P,P-1);
    }
    lli mx,mn;
    lli LOG=(lli)(log2((long double)TK)+EPS);
    lli START=1LL<<LOG;
    //lliout(START);
    LOG++;
    //lliout(LOG);
    lli MAX=MX[LOG];
    //lliout(MAX);
    lli LOGN=H;
    lli STARTN=1LL<<H;
    //lliout(STARTN);
    //lliout(LOGN);
    lli DIFF=N-STARTN;
    lli EFF=START<<1LL;
    //MAX+=(DIFF)/EFF;
    DIFF=DIFF%EFF;
    //lliout(DIFF);
    if(DIFF<START){
        mn=MAX-1;
        if(TK>DIFF+START){
            mx=MAX-1;
        }
        else{
            mx=MAX;
        }
    }
    else{
        mx=MAX;
        if(TK>DIFF){
            mn=MAX-1;
        }
        else{
            mn=MAX;
        }
    }
    if(mx<0){
        mx=0;
    }
    if(mn<0){
        mn=0;
    }
    return mp(mx,mn);
}

int main(void){
	//freopen("output.txt","w",stdout);
	//freopen("input.txt","r",stdin);
	preprocess();
	int t;
	si(t);
//	t=1;
	for(int z=1;z<=t;z++){
		printf("Case #%d: ",z);
        slli(N);
        slli(K);
        preCalc();
        pair<lli,lli> ans=solve(K);//first is max second is min
        printf("%lld %lld\n",ans.fi,ans.se);
	}
	return 0;
}
