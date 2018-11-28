#include<bits/stdc++.h>
#define PI acos(-1)
#define ll long long
#define eps 1e-9
#define PB push_back
#define EB emplace_back
#define F first
#define S second
#define MP make_pair
#define RS resize
#define BG begin
#define sf scanf
#define pf printf
#define optimize() ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define gcd(a,b) __gcd(a,b)
#define lcm(a,b) (a*(b/gcd(a,b)))
#define MOD 1000000007
#define fraction() cout.unsetf(ios::floatfield); cout.precision(6); cout.setf(ios::fixed,ios::floatfield);
#define harmonic(n) 0.577215664901532861 + log(n);

using namespace std;

typedef vector<ll>   vll;
typedef vector<int>   vi;
typedef pair<int,int>  pii;
typedef pair<ll,ll>   pll;
typedef vector<pii>  vpi;
typedef vector<vector<int> > vvi;
typedef vector<vector<ll> > vvl;
typedef vector<pll> vpl;

int dx[] = {+1 , -1 , 0 , 0};
int dy[] = {0 , 0 , +1 , -1};
int dx2[] = {+1 , -1 , 0 , 0 , +1 , +1 , -1 , -1};
int dy2[] = {0 , 0 , +1 , -1 , +1 , -1 , -1 , +1};

inline ll squ(ll x)
{
    return (x*x);
}

inline ll power(ll bs,ll k)
{
    ll x = 1LL,y = bs;
    if(k == 0) return 1LL;

    while(k > 0){
        if(k % 2) x *= y;

        y *= y;
        k /= 2;
    }

    return x;
}

#define MX 1010

int cl[MX],pr[MX];
int dp[7][MX][MX];
int n,a[7],b[7];

//R = 0,Or = 1,Y = 2,G = 3, B = 4,V = 5

bool cmp(int i,int j)
{
    if(i == 0){
        if(j != 1 && j != 5 && j != 0) return true;
        return false;
    }

    if(i == 1){
        if(j == 4) return true;
        return false;
    }

    if(i == 2){
        if(j != 1 && j != 2 && j != 3) return true;
        return false;
    }

    if(i == 3){
        if(j == 0) return true;
        return false;
    }
    if(i == 4){
        if(j == 0 || j == 1 || j == 2) return true;
        return false;
    }

    if(i == 5){
        if(j == 2) return true;
        return false;
    }
}

bool chk(){
   // printf("printing %d ",cl[0]);
    for(int i = 1; i < n; i++){
       // printf("%d ",cl[i]);
        if(cmp(cl[i],cl[i - 1]) == true && cmp(cl[i],cl[(i + 1) % n]) == true) continue;
       // printf("false \n");
        return false;
    }
    //printf("\n");
    return true;
}

int func(int c,int idx,int &dc)
{
    int i,j;
    //if(c != -1 && dp[c][idx][st] != -1) return dp[c][idx][st];
    if(idx >= n){
        if(chk() == true){
            dc = 1;
            return dc;
        }
        return 0;
    }

    for(i = 0; i < 6; i++){
        if(b[i] > 0 && (c == -1 || cmp(i,c))){
            if(dp[i][idx][b[i] - 1] == 0) continue;
            else if(dp[i][idx][b[i] - 1] == 1) return 1;
            b[i]--;
            cl[idx] = i;

            dp[i][idx][b[i]] = func(i,idx + 1,dc);

            if(dp[i][idx][b[i]] == 1){
               // printf("returning from %d %d %d: \n",i,idx,b[i]);
                return 1;
            }
            if(dc == 1) return 1;
            b[i]++;
        }
    }
    //printf("%d %d\n",c,idx);
    return 0;
}



int main()
{
    optimize();
    fraction();

    int tst,cs = 0,i,j,dc = -1;

    FILE *in,*out;
    in=fopen("inputs.txt","r");
    out=fopen("outputs.txt","w");

    fscanf(in,"%d",&tst);
    //printf()

    while(++cs <= tst){
        memset(dp,-1,sizeof(dp));
        fscanf(in,"%d",&n);
        dc = 0;
        for(i = 0;i < 6; i++) fscanf(in,"%d",&a[i]);

        for(i = 0;i < 6; i++) b[i] = a[i];
        //for(i = 0; i < 6; i++) printf("%d ",a[i]);
        //printf("\n\n\n");
        fprintf(out,"Case #%d: ",cs);
        dc = func(-1,0,dc);
        if(dc == 1){

            for(i = 0; i < n; i++){
                if(cl[i] == 0) fprintf(out,"R");
                if(cl[i] == 1) fprintf(out,"O");
                if(cl[i] == 2) fprintf(out,"Y");
                if(cl[i] == 3) fprintf(out,"G");
                if(cl[i] == 4) fprintf(out,"B");
                if(cl[i] == 5) fprintf(out,"V");
            }
        }

        else fprintf(out,"IMPOSSIBLE");

        fprintf(out,"\n");

        //printf("\n\n");
    }

    return 0;
}
