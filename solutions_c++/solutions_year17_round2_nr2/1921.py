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

int n;
int v[10];
string l = "ROYGBV";
int c[][3] = {{5,0,1} , {0,1,2} , {1,2,3} , {2,3,4} , {3,4,5} ,{4,5,0}};
int has[10];

bool can(int lst , int nw){
    loop(i,3){
        if(nw == c[lst][i])return 0;
    }
    return 1;
}

int mx(int lst , int f){
    int m = 0 , ret = -1;
    loop(i,6){
        if(!v[i])continue;
        if(!can(lst , i))continue;
        if(v[i] == m && has[i] > has[ret])
            ret = i;
        if(v[i] == m && has[i] == has[ret] && i == f)
            ret = i;
        if(v[i] > m){
            m = v[i];
            ret = i;
        }
    }

    assert(ret != -1);
    return ret;
}


void solve(){
    int f = 8 , lst = 8;
    while(n){
        int idx = mx(lst , f);
        printf("%c",l[idx]);
        v[idx]--;
        loop(j,3)has[c[idx][j]]--;
        if(f == 8)f = idx;
        lst = idx;
        n--;
    }
    puts("");
}


int main()
{

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	//ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);

    int t;
    sfi1(t);
    range(T,1,t){
        memset(has,0,sizeof has);
        sfi1(n);
        printf("Case #%d: ",T);
        if(n == 1){
            loop(i,6)if(v[i])printf("%c\n",l[i]);
        }
        loop(i,6)sfi1(v[i]);
        int mx = *max_element(v , v+6);
        if(mx > n - mx){
            puts("IMPOSSIBLE");
            continue;
        }

        loop(i,6)loop(j,3)has[c[i][j]] += v[i];
        solve();
    }



    return 0;
}
