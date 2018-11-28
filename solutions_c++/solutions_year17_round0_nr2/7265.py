#include <bits/stdc++.h>
using namespace std;
template <class T> int size(const T &x) { return x.size(); }

#define SCD(t) scanf("%d",&t)
#define forl(i,a,b) for (__typeof(a) i=(a); i<(b); ++i)
#define iter(it,c) for (__typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it)

typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

const int INF = ~(1<<31); // 2147483647
typedef long long ll;
typedef unsigned long long ull;
typedef long int li;   //int32
typedef unsigned long int uli;
typedef long long int lli;    //int64
typedef unsigned long long int ulli;

const double EPS = 1e-9;
const double pi = acos(-1);
typedef vector<vi> vvi;
typedef vector<vii> vvii;
template <class T> T smod(T a, T b) { return (a % b + b) % b; }
template<typename T, typename U> inline void amin(T &x, U y) { if(y < x) x = y; }
template<typename T, typename U> inline void amax(T &x, U y) { if(x < y) x = y; }


int main()
{

	#ifndef ONLINE_JUDGE
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	#endif
	int t;
	cin>>t;
	forl(u,0,t){
			string s;
			cin>>s;
			string ar=s;
			string ret="";
			int len=ar.length();
			int i=0;
			int ans=0;
			int x=0;
			for(i=0;i<len-1;i++)
			{
				if(ar[i]>ar[i+1])
				{
					ar[i]--;
					break;
				}
			}
			for(int j=i+1;j<len;j++)
				ar[j]='9';
			for(i=len-1;i>=1;i--)
			{
				if(ar[i]<ar[i-1])
				{
					ar[i]='9';
					ar[i-1]--;
				}
			}
			int j=0;
			while(ar[j]=='0')
				j++;
			while(j<len)
				ret=ret+ar[j++];		
		
	 cout<<"Case #"<<u+1<<": "<<ret<<endl;
	}

	return 0;
}

