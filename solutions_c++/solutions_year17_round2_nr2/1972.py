/*
ID: Tariqul
PROG:
LANG: C++
*/

#include <bits/stdc++.h>

using namespace std;

#define fo(i,j,n) for(i=j;i<n;++i)
#define Fo(i,j,n) for(i=n-1;i>=j;--i)
#define foo(i,j,v) fo(i,j,sz(v))
#define Foo(i,j,v) Fo(i,j,sz(v))
#define li(v) v.begin(),v.end()
#define sz(v) ((int)v.size())
#define CLR(a,v) memset((a),(v),sizeof(a))

typedef long long Long;
//typedef __int64 Long;
#define pi (2*acos(0))
#define eps 1e-9

const int imax = 1e9+7;
const Long lmax = 1e18;

#define two(X) (1<<(X))
#define twoL(X) (((Long)(1))<<(X))
#define contain(S,X) (((S)&two(X))!=0)
#define containL(S,X) (((S)&twoL(X))!=0)

char BUFFER[100000 + 5];
bool readn(int &n)	{ return scanf("%d",&n) == 1; }
bool readl(Long &n)	{ return scanf("%I64d",&n) == 1; }
bool readd(double &n){ return scanf("%lf",&n) == 1; }
bool reads(string &s){ s = ""; int n = scanf("%s",BUFFER); if(n == 1)s = BUFFER; return n == 1; }
bool readln(string &s){ char *valid = gets(BUFFER); if(valid)s = BUFFER; return ((bool)valid); }

// std::getline(std::cin, name);

template<class T>
T gcd(T a,T b) { if(a < b)swap(a,b); if(b==0)return a; return gcd(b,a%b); }

string s = "RYB",ans;

bool good(char ch1, char ch2, int n, vector<pair<int,int> > v)
{
	if(v[ch1].first == 0)return false;
	if(v[ch2].first == 0)return false;
	ans[0] = s[ch1]; ans[n-1] = s[ch2];
	int i,k; v[ch1].first--; v[ch2].first--;
	n -= 2; i = 0;
	while(n--)
	{
		sort(li(v));
		Fo(k,0,3)if(v[k].first > 0)
		{
			if(s[v[k].second] != ans[i])
			{
				int id = v[k].second;
				char ch = s[id];
				ans[++i] = ch;
				v[k].first--;
				break;
			}
		}
		if(k < 0)return false;		
	}
	n = sz(ans);
	if(ans[n-2] == ans[n-1])return false;
	return true;
}

vector<pair<int,int> > v(3);

void calc()
{
	int n,r,y,b,m,i,j; 
	fo(i,0,3)v[i].second = i; 
	cin >> n >> v[0].first >> m >> v[1].first >> m >> v[2].first >> m;
	ans.resize(n); 
	fo(i,0,3)fo(j,0,3)if(i != j)
	{
		if(good(i,j,n,v))
		{
			cout << ans;
			return;
		}
	}
	cout << "IMPOSSIBLE";
}

int main()
{
    ios_base::sync_with_stdio(0);
	freopen("E://input.txt","r",stdin);
	freopen("E://output.txt","w",stdout);
	int Case,t;
	scanf("%d",&t);
	fo(Case,1,t+1)
	{
		printf("Case #%d: ",Case);
        calc();
		cout << endl;
	}
	return 0;
}

