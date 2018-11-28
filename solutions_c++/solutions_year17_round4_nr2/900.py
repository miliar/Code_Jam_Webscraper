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
typedef vector<int> vi;
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

vi mas[1001];

int shift(int size, int sh)
{
	int answ = 0;
	int f,s;
	for(int i=0; i < size; ++i)
	{
		f = -1;
		s = -2;
		if(i < mas[0].size())
			f = mas[0][i];
		int id = (-i+sh+size) % size;
		if(0 <= id && id < mas[1].size())
			s = mas[1][id];
		if(s == f)
		{
			if(s == 0)
				return (int) 1e9;
			++answ;
		}
	}
	return answ;
}

int bshift(int size, int sh)
{
	int answ = 0;
	int f,s;
	for(int i=0; i < size; ++i)
	{
		f = -1;
		s = -2;
		if(i < mas[0].size())
			f = mas[0][i];
		int id = (i+sh+size) % size;
		if(0 <= id && id < mas[1].size())
			s = mas[1][id];
		if(s == f)
		{
			if(s == 0)
				return (int) 1e9;
			++answ;
		}
	}
	return answ;
}

int shiftall(int size)
{
	int answ = 1e9;
	for(int i = 0; i < size; ++i)
	{
		answ = min(answ, shift(size, i));
		answ = min(answ, bshift(size, i));
	}
	return answ;
}

void test(int T)
{
	int n,m,c;
	scanf("%d%d%d",&n,&c,&m);
	for(int i = 0; i < 1001; ++i)
		mas[i].clear();
	for(int i=0; i<m; ++i)
	{
		int p,b;
		scanf("%d%d",&p,&b);
		mas[b-1].push_back(p-1);
	}
	sort(mas[0].begin(), mas[0].end());
	sort(mas[1].begin(), mas[1].end());
	int l = int(max(mas[0].size(), mas[1].size()))-1;
	int r = m;
	while(l+1 < r)
	{
		int s = (l+r)/2;
		int p = shiftall(s);
		if(p <= 1000000)
			r = s;
		else
			l = s;
	}
    printf("Case #%d: %d %d\n", T, r, shiftall(r));
}

int main()
{
    freopen("b.in", "r", stdin);
    freopen("b.out", "w", stdout);
	int n;
    cin>>n;
    for(int i = 0; i < n; ++i)
        test(i+1);
    return 0;
}
