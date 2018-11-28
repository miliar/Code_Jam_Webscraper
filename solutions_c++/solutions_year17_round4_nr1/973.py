#include<cstdio>
#include<iostream>
#include<algorithm>
#include<vector>
#include<stack>
#include<queue>
#include<set>
#include<map>
#include<cstring>
#include<string>
#include<cmath>
#include<complex>
#include<ctime>
#include<functional>

using namespace std;

typedef long long ll;
typedef pair<ll,ll> pii;
typedef vector<ll> vi;
typedef vi::iterator vit;
typedef set<ll> si;
typedef si::iterator sit;
typedef vector<pii> vpi;
typedef pair<int, char> pci;
typedef vector<pci> vpci;

#define sq(x) ((x)*(x))
#define all(x) (x).begin(),(x).end()
#define cl(x) memset(x,0,sizeof(x))
//#define LL "%I64d"
#define LL "%lld"
#define RLL(x) scanf(LL,&(x))

int g[111];
int dyn[4][111][111][111];
int pos[4];
void test(int T)
{
	int n, p;
	cl(pos);
	cl(dyn);
	scanf("%d%d", &n, &p);
	for(int i=0; i<n; ++i)
	{
		scanf("%d", g+i);
		++pos[g[i]%p];
	}
	dyn[0][pos[1]][pos[2]][pos[3]] = pos[0] + 1;
	for(int i = 100; i >= 0; --i)
		for(int j = 100; j >= 0; --j)
			for(int k = 100; k >= 0; --k)
				for(int d = 3; d >=0; --d)
					if(dyn[d][i][j][k])
					{
						int nx = dyn[d][i][j][k];
						if(d == 0)
							++nx;
						if(i)
							dyn[(d+p-1)%p][i-1][j][k] = max(dyn[(d+p-1)%p][i-1][j][k], nx);
						if(j)
							dyn[(d+p-2)%p][i][j-1][k] = max(dyn[(d+p-2)%p][i][j-1][k], nx);
						if(k)
							dyn[(d+p-3)%p][i][j][k-1] = max(dyn[(d+p-3)%p][i][j][k-1], nx);
					}
    int res = 0;
	for(int i = 0; i < 4; ++i)
		res = max(res, dyn[i][0][0][0]);
    printf("Case #%d: %d\n", T, res-1);
}

int main()
{
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
	int n;
    cin>>n;
    for(int i = 0; i < n; ++i)
        test(i+1);
    return 0;
}
