#include<bits/stdc++.h>
/*
ID: arun.ga1
LANG: C++
TASK: 
 */

using namespace std;

#define prime 1000000007
#define DEBUG(x) cout << '>' << #x << ':' << x << endl;
#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)
inline bool EQ(double a, double b) { return fabs(a-b) < 1e-9; }
const int INF = 1<<29;
typedef long long ll;
inline int two(int n) { return 1 << n; }
inline int test(int n, int b) { return (n>>b)&1; }
inline void set_bit(int & n, int b) { n |= two(b); }
inline void unset_bit(int & n, int b) { n &= ~two(b); }
inline int last_bit(int n) { return n & (-n); }
inline int ones(int n) { int res = 0; while(n && ++res) n-=n&(-n); return res; }
template<class T> void chmax(T & a, const T & b) { a = max(a, b); }
template<class T> void chmin(T & a, const T & b) { a = min(a, b); }

/////////////////////////////////////////////////////////////////////

char q;
char cake[30][30];
ll row,col;
ll i,j,y,z;
void fill(ll a, ll b, ll c , ll d , char e)
{
	ll s,f;
	for(s=a;s<=c;s++)
	{
		for(f=b;f<=d;f++)
		{
			cake[s][f]=e;
		}
	}
}
void fillr(ll a,ll b,ll c,ll d, char e)
{
	ll s,f,pnt,flag=0;
	for(f=d+1;f<col;f++)
	{
		for(s=a;s<=c;s++)
		{
			if(cake[s][f]!='?')
			{
				pnt = f;
				flag = 1;
				break;
			}
		}
		if(flag)
			break;
		if(f==col-1)
			pnt=col;
	}
	for(f=d+1;f<pnt;f++)
	{
		for(s=a;s<=c;s++)
		{
			cake[s][f]=e;
		}
	}
}
void filld(ll a,ll b,ll c,ll d, char e)
{
	ll s,f,pnt,flag=0;
	for(s=c+1;s<row;s++)
	{
		for(f=b;f<=d;f++)
		{
			if(cake[s][f]!='?')
			{
				pnt = s;
				flag = 1;
				break;
			}
		}
		if(flag)
			break;
		if(s==row-1)
			pnt=row;
	}
	for(s=c+1;s<pnt;s++)
	{
		for(f=b;f<=d;f++)
		{
			cake[s][f]=e;
		}
	}
}
void filll(ll a,ll b,ll c,ll d, char e)
{
	ll s,f,pnt,flag=0;
	for(f=b-1;f>=0;f--)
	{
		for(s=a;s<=c;s++)
		{
			if(cake[s][f]!='?')
			{
				pnt = f+1;
				flag = 1;
				break;
			}
		}
		if(flag)
			break;
		if(f==0)
			pnt=0;
	}
	for(f=b-1;f>=pnt;f--)
	{
		for(s=a;s<=c;s++)
		{
			cake[s][f]=e;
		}
	}
}
void fillu(ll a,ll b,ll c,ll d, char e)
{
	ll s,f,pnt,flag=0;
	for(s=a-1;s>=0;s--)
	{
		for(f=b;f<=d;f++)
		{
			if(cake[s][f]!='?')
			{
				pnt = s+1;
				flag = 1;
				break;
			}
		}
		if(flag)
			break;
		if(s==0)
			pnt=0;
	}
	for(s=a-1;s>=pnt;s--)
	{
		for(f=b;f<=d;f++)
		{
			cake[s][f]=e;
		}
	}
}
/*void filll(ll a,ll b,ll c,ll d, char e)
void fillu(ll a,ll b,ll c,ll d, char e)
void filld(ll a,ll b,ll c,ll d, char e)*/
int main()
{
	ios_base::sync_with_stdio(false); cin.tie(0);
	ll t,k;
	cin >> t;
	REP(k,t)
	{
		cout << "Case #" << k+1 << ": " << endl;
		cin >> row >> col;
		REP(i,row)
		{
			cin >> cake[i];
		}
		REP(i,row)
		{
			REP(j,col)
			{
				q = cake[i][j];
				REP(y,row)
				{
					REP(z,col)
					{
						if(cake[y][z]==q && q!='?')
						{
							fill(i,j,y,z,q);
							fillr(i,j,y,z,q);
							filll(i,j,y,z,q);
							//fillu(i,j,y,z,q);
							//filld(i,j,y,z,q);
						}
					}
				}

			}
		}
		REP(i,row)
		{
			REP(j,col)
			{
				q = cake[i][j];
				REP(y,row)
				{
					REP(z,col)
					{
						if(cake[y][z]==q && q!='?')
						{
							fillu(i,j,y,z,q);
							filld(i,j,y,z,q);
						}
					}
				}

			}
		}
		REP(i,row)
		{
			REP(j,col)
				cout << cake[i][j];
			cout << endl;
		}
	}
	return 0;
}

