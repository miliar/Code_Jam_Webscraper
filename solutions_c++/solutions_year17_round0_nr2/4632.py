//arpit717
#include<bits/stdc++.h>

using namespace std;

typedef pair<int,int>   II;
typedef vector< II >      VII;
typedef vector<int>     VI;
typedef vector< VI > 	VVI;
typedef long long int 	ll;
typedef unsigned long long int ULL;

#define PB push_back
#define MP make_pair
#define F first
#define S second
#define SZ(a) (int)(a.size())
#define ALL(a) a.begin(),a.end()
#define SET(a,b) memset(a,b,sizeof(a))
#define LET(x,a) __typeof(a) x(a)

#define loop(i, begin, end) for (__typeof(end) i = (begin) - ((begin) > (end)); i != (end) - ((begin) > (end)); i += 1 - 2 * ((begin) > (end)))
//Works for forward as well as backward iteration

#define gu getchar
#define pu putchar
#define si(n) scanf("%d",&n)
#define dout(n) printf("%d\n",n)
#define sll(n) scanf("%lld",&n)
#define lldout(n) printf("%lld\n",n)

#define DRT() int t; si(t); while(t--)

#define PlUSWRAP(index,n) index = (index+1)%n		//index++; if(index>=n) index=0
#define MINUSWRAP(index,n) index = (index + n -1)%n 	//index--; if(index<0) index=n-1
#define ROUNDOFFINT(d) d = (int)((double)d + 0.5)	//Round off d to nearest integer

#define FLUSHN while(gu()!='\n')
#define FLUSHS while(gu()!=' ')

//#define TRACE

#ifdef TRACE
#define trace1(x)                cerr << #x << ": " << x << endl;
#define trace2(x, y)             cerr << #x << ": " << x << " | " << #y << ": " << y << endl;
#define trace3(x, y, z)          cerr << #x << ": " << x << " | " << #y << ": " << y << " | " << #z << ": " << z << endl;
#define trace4(a, b, c, d)       cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << endl;
#define trace5(a, b, c, d, e)    cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << " | " << #e << ": " << e << endl;
#define trace6(a, b, c, d, e, f) cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << " | " << #e << ": " << e << " | " << #f << ": " << f << endl;

#else

#define trace1(x)
#define trace2(x, y)
#define trace3(x, y, z)
#define trace4(a, b, c, d)
#define trace5(a, b, c, d, e)
#define trace6(a, b, c, d, e, f)

#endif

FILE *fin = freopen("B-small-attempt1.in","r",stdin);
FILE *fout = freopen("B-small-attempt1-out.txt","w",stdout);
//const int N = int(1e5)+10;
const int LOGN = 20;
const int INF = int(1e9);

vector<int> s;
void solve(){

	ll n,n2;
	int tmp;
	cin>>n;
	// cout<<n<<" --> ";
	n2=n;
	s.clear();
	while(n){
		tmp = n%10;
		s.push_back(tmp);
		n = n/10;
	}
	reverse(s.begin(),s.end());
	int loc=-1;

	loop(i,0,s.size()-1){
		if(s[i]>s[i+1]){
			loc = i;
			break;
		}
	}
	if(loc==-1)cout<<n2<<endl;
	else{
		loop(i,0,s.size()-1){
			if(s[i]>=s[i+1]){
				loc = i;
				break;
				}
		}
		if(s[loc]==1)loop(i,0,s.size()-1)cout<<9;
		else{
			s[loc]--;
			loop(i,0,s.size()){
				if(i>loc)cout<<9;
				else cout<<s[i];
			}
		}
		cout<<endl;
	}

}

int main()
{	
	int t;
	cin>>t;
	loop(i,1,t+1){
		cout<<"Case #"<<i<<": ";
		solve();
	}
  
    return 0;
}