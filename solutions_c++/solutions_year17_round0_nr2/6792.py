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

char digits[] = {'0','1','2','3','4','5','6','7','8','9'};

string maketidy(string s);
string process(string s);
bool checktidy(string s);
string makemetidy(string s);



int main()	{

freopen("B-large.in", "r", stdin);
freopen("B-large.out", "w", stdout);

int t,cas;
LL n;
string s;
cin >> t;

for(cas = 1 ; cas <= t ; cas ++)	{
	cin >> s;
	cout << "Case #" << cas << ":" << " " << makemetidy(s) << endl; 
}

return 0;
}

string maketidy(string s)	{

	int j,i=0;
	int x,y;
	char c;

	while( i < s.size()-1 && (int)s[i] <= (int)s[i+1])	{
		i++;
	}
	
	if ( i < s.size()-1)	{
		x = (int)s[i] - (int)'0' - 1;
		s[i] = digits[x];
		for(j=i+1 ; j< s.size();j++)	{
			s[j] = '9';
		}
	}
//	cout << "maketidy : " << s << endl;
	return process(s);
}

string process(string s)	{
	string t;
	int i = 0;
	int j = 0;
	while(s[i] == '0' && i<s.size())	{
		i++;
	}
	for(j=i;j<s.size();j++)	{
		t.push_back(s[j]);
	}
	return t;
}

bool checktidy(string s)	{
	int i,x,y;
	for(i=0;i<s.size()-1;)	{
		if((int)s[i] <= (int)s[i+1])	{
			i++;
		}
		else break;
	}
	if(i == s.size()-1)	return true;
	else return false;
}

string makemetidy(string s)	{
	if(checktidy(s))	{
		return s;
	}
	else	{
		return makemetidy(maketidy(s));
	}
}