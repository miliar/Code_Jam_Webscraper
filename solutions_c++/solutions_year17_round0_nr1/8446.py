/**************************************************************************************************************
   *  Md. Abdulla Al Mamun (Nayon)
   *  ID: 1306001
   *  Session: 2013-2014
   *  Department of Computer Science and Engineering
   *  Begum Rokeya University, Rangpur (BRUR)
***************************************************************************************************************/
#include <bits/stdc++.h>

using namespace std;

#define PI acos(-1.0)
#define EPS 1e-9
#define INF 1 << 28
#define sq(a) ((a) * (a))
#define toRad(a) ((a)*(PI)/180)
#define toDeg(a) ((a)*180/(PI))
#define all(x) (x).begin(), (x).end()
#define pb(x) push_back(x)
#define ppb pop_back
#define mp(a, b) make_pair(a, b)
#define endl '\n'
#define MAX 100000
#define MOD 1000000007
#define what_is(x) cerr << #x << " is " << x << endl;

inline bool isEq(double a, double b){ return (abs(a - b) < EPS); }

typedef pair<int, int> pii;
typedef long long ll;

//#define isValid(a, b) ((a >= 0 && a < b) ? 1 : 0)
//int dr[]  =  {0, -1, -1, -1,  0,  1, 1, 1};
//int dc[]  =  {1,  1,  0, -1, -1, -1, 0, 1};

void flip(string &s, int i, int k)
{
	for(int j = i; j < i+k; j++){
		if(s[j] == '-')
			s[j] = '+';
		else
			s[j] = '-';
	}
}

map<string, bool>vis;
int bfs(string s, int k)
{
	queue<pair<string, int > >q;
	q.push(pair<string, int>(s, 0));
	vis[s] = true;
	int len = s.length(), lev;
	string u, v, dest = "";
	for(int i = 0; i < len; i++){
		dest.push_back('+');
	}
	len -= k;
	while(!q.empty()){
		u = q.front().first;
		lev = q.front().second;
		q.pop();
		if(u == dest)
			return lev;
		for(int i = 0; i <= len; i++){
			v = u;
			flip(v, i, k);
			if(!vis[v]){
				vis[v] = true;
				q.push(pair<string, int>(v, lev+1));
			}
		}
	}
	return -1;
}

int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
	//ios_base::sync_with_stdio(false); cin.tie(NULL);
	int t;
	string s;
	int k;
	cin >> t;
	for(int i = 1; i <= t; i++){
		cin >> s >> k;
		int a = bfs(s, k);
		if(a >= 0)
			cout << "Case #" << i << ": " << a << endl;
		else
			cout << "Case #" << i << ": IMPOSSIBLE" << endl;
		vis.clear();
	}
	return 0;
}
