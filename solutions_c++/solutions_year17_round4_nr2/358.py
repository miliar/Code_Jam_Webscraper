#include <bits/stdc++.h>
using namespace std;

#define loop(i,n) for(int i = 0;i < int(n);i++)
#define rloop(i,n) for(int i = int(n);i >= 0;i--)
#define range(i,a,b) for(int i = int(a);i <= int(b);i++)
#define SZ(c) int(c.size())
#define ALL(c) c.begin(), c.end()
#define RALL(c) c.rbegin(), c.rend()
#define PI acos(-1)
#define pb push_back
#define mp make_pair
#define fr first
#define sc second
#define sfi1(v) scanf("%d",&v)
#define sfi2(v1,v2) scanf("%d %d",&v1,&v2)
#define sfi3(v1,v2,v3) scanf("%d %d %d",&v1,&v2,&v3)
#define sfll1(v) scanf("%I64d",&v);
#define sfll2(v1,v2) scanf("%I64d %I64d",&v1,&v2)
#define sfll3(v1,v2,v3) scanf("%I64d %I64d %I64d",&v1,&v2,&v3)

typedef vector<int> vi;
typedef vector<pair<int,int> > vii;
typedef long long ll;
typedef pair<int, int> pii;

const int N = 1005;
int cust[N] , seat[N];
int p[N] , b[N];
int n , c , m;

bool valid(int trips){
    range(i,1,n)seat[i] = trips;
    loop(i,m)
        seat[p[i]]--;
    int free = 0;
    range(i,1,n){
        if(seat[i] < 0 && abs(seat[i]) > free)
            return 0;
        free += seat[i];
    }
    return 1;
}

int col(int trips){
    range(i,1,n)seat[i] = trips;
    loop(i,m)
        seat[p[i]]--;
    int ret = 0;
    range(i,1,n){
        if(seat[i] < 0)
            ret -= seat[i];
    }

    return ret;
}

int bs(int s, int e){
    while (s < e){
        int mid = (s + (e - s) / 2);
        if (valid(mid))
            e = mid;
        else
            s = mid + 1;
    }

    return s;
}

int main()
{


	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	//ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);

    int t;
    sfi1(t);
    range(T,1,t){
        sfi3(n,c,m);
        memset(cust,0,sizeof cust);
        loop(i,m)sfi2(p[i],b[i]);
        loop(i,m)cust[b[i]]++;
        int mn = 0;
        range(i,1,c)mn = max(mn , cust[i]);
        int ans = bs(mn,N);
        printf("Case #%d: %d %d\n",T,ans,col(ans));
    }


    return 0;
}
