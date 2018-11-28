/*
ID: Alaudddin
PROG: 
LANG: C++
*/

#include <algorithm> 
#include <cctype> 
#include <cmath> 
#include <cstdio> 
#include <cstdlib> 
#include <cstring> 
#include <deque> 
#include <iostream> 
#include <list> 
#include <map> 
#include <numeric> 
#include <queue> 
#include <set> 
#include <sstream> 
#include <stack> 
#include <string> 
#include <vector>

using namespace std; 

#define fo(i,j,n) for(i=j;i<n;++i)
#define Fo(i,j,n) for(i=n-1;i>=j;--i)
#define foo(i,j,v) fo(i,j,sz(v))
#define Foo(i,j,v) Fo(i,j,sz(v))
#define li(v) v.begin(),v.end()
#define sz(v) ((int)v.size())
#define CLR(a,v) memset((a),(v),sizeof(a))
#define inf 1000000001
typedef long long Long;
//typedef __int64 Long;
#define pi (2*acos(0))
#define eps 1e-9

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

template<class T>
T gcd(T a,T b) { if(a < b)return gcd(b,a); if(b==0)return a; return gcd(b,a%b); }

string s;

void calc()
{
	cin >> s;
	Long ans = 0;
	int i,j; foo(i,0,s)s[i] -= '0';
	foo(j,1,s)if(s[j-1] > s[j])
	{
		foo(i,j,s)s[i] = 9;
		Fo(i,0,j)
		{
			s[i]--;
			if(i > 0 && s[i-1] > s[i])
			{
				s[i] = 9;
			}
			else break;
		}
	}
	
	foo(i,0,s)ans = (ans * 10) + s[i];
	cout << ans;
}

int main()
{
	freopen("E://input.txt","r",stdin);
	//freopen("E://output.txt","w",stdout);
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

