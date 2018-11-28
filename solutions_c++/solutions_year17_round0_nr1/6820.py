#include<bits/stdc++.h>

using namespace std;
 
typedef long long LL;
typedef unsigned long long ULL;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<vector<int> > vvi;
 
#define GI ({int t;scanf("%d",&t);t;})
#define REP(i,a,b) for(int i=a;i<b;i++)
#define ALL(v) (v).begin(),(v).end()
#define TR(i,x) for(typeof(x.begin()) i=x.begin();i!=x.end();i++)
#define pb push_back
#define mp make_pair
#define INF (int)1e9
#define EPS (double)(1e-9)
#define PI (double)(3.141592653589793)
#define gc getchar
#define ff first
#define ss second

inline int read(){
	int n = 0, c = gc(), f = 1;
	while(c != '-' && (c < '0' || c > '9')) c = gc();
	if(c == '-') f = -1, c = gc();
	while(c >= '0' && c <= '9')
	n = (n<<3) + (n<<1) + c - '0', c = gc();
	return n * f;
}


int main()	{

freopen("A-large.in", "r", stdin);
freopen("A-large.out", "w", stdout);

int t,k,cas;
string s;
int i,j,cnt;

cin >> t;

for(cas = 1 ; cas <= t ; cas ++)	{
	cin >> s >> k;
	cnt = 0;
	for(i=0;i<s.size();)	{
		while(s[i] == '+' && i < s.size())	{
			i++;
		}
		if(i+k <= s.size())	{
			for(j=i;j<i+k;j++)	{
				if(s[j] == '+')	s[j] = '-';
				else s[j] = '+';
			}
			cnt++;
		}
		else {
			break;
		}
	}

	if(s.find('-') != std::string::npos) {
		cout << "Case #" << cas << ":" << " " << "IMPOSSIBLE" << endl; 
	}
	else	{
		cout << "Case #" << cas << ":" << " " << cnt << endl; 	
	}
}

return 0;
}

