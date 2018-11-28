/*input
3
3 3
G??
?C?
??J
3 4
CODE
????
?JAM
2 2
CA
KE
*/
#include <bits/stdc++.h>

using namespace std;

#define gcd                         __gcd

#define fr(i, a, b) for(int (i) = (a); (i) < (b); ++(i))
#define fu(i,n) fr(i,0,n)

#define sc(a) scanf("%d", &a) //next three are handy ways to get ints, it's also force you to use '&' sign
#define sc2(a,b) scanf("%d%d", &a, &b)
#define sc3(a,b,c) scanf("%d%d%d", &a, &b, &c)

#define pr(a) printf("%d\n", a)
#define pr2(a, b) printf("%d %d\n", a, b)
#define pr3(a, b, c) printf("%d %d %d\n", a, b, c)

#define clr(a,x) memset(a,x,sizeof(a)) //set elements of array to some value
#define char2Int(c) (c-'0')
#define sz(x) ((int)((x).size()))

#define remax(a,b) (a)=max((a),(b)) // set a to the maximum of a and b
#define remin(a,b) (a)=min((a),(b));

#define snuke(i,t) for (typeof(t.begin()) i=t.begin(); i!=t.end(); i++) // traverse an STL data structure

#define all(c) (c).begin(),(c).end() //handy for function like "sort()"
#define rall(c) (c).rbegin(), (c).rend()

#define IOS ios_base::sync_with_stdio(0) //to synchronize the input of cin and scanf
#define INF 1001001001

#define mt make_tuple
#define mp make_pair
#define fi first
#define se second
#define pb push_back

//for vectors
typedef vector<int> vi; 
typedef pair<int,int> ii; 
typedef long long ll;
typedef unsigned long long ull;

constexpr int maxn = 26;

char grid[maxn][maxn];

bool isValid(int x, int y, int lin, int col){
	return (x>= 0 && x < lin && y >= 0 && y < col);
}

void solve(int lin, int col, int cas)
{
	set<char> visited;
	bool ok;
	fu(l, lin)
	{
		fu(c, col)
		{
			//try to expand linearly
			if(grid[l][c] == '?')continue;
			int begC = c, endC = c;
			char mrk = grid[l][c];
			if(visited.find(mrk) != visited.end())
				continue;
			for(int tempC = c-1; tempC >= 0; --tempC)
			{
				if(grid[l][tempC] != '?')
					break;
				else{
					begC = tempC;
					grid[l][tempC] = mrk;
				}
			}
			for(int tempC = c+1; tempC < col; ++tempC)
			{
				if(grid[l][tempC] != '?')
					break;
				else{
					endC = tempC;
					grid[l][tempC] = mrk;
				}
			}
			int begL = l, endL = l;
			for(int tempL = l-1; tempL >= 0; --tempL)
			{
				ok = true;
				for(int tC = begC; tC <= endC; ++tC)
				{
					if(grid[tempL][tC] != '?' && grid[tempL][tC] != mrk)
					{
						ok = false;
						break;
					}
				}
				if(ok)
				{
					for(int tC = begC; tC <= endC; ++tC)
					{
						grid[tempL][tC] = mrk;
					}
				}
				else break;
			}
			for(int tempL = l+1; tempL < lin; ++tempL)
			{
				ok = true;
				for(int tC = begC; tC <= endC; ++tC)
				{
					if(grid[tempL][tC] != '?' && grid[tempL][tC] != mrk)
					{
						ok = false;
						break;
					}
				}
				if(ok)
				{
					for(int tC = begC; tC <= endC; ++tC)
					{
						grid[tempL][tC] = mrk;
					}
				}
				else break;
			}
			visited.insert(mrk);
		}
	}
}
int main()
{
	ifstream in; in.open("in.txt");
	ofstream out; out.open("out.txt");
	int t;
	in >> t;
	fu(i, t)
	{
		int x, y;
		in >> x >> y;
		string s;
		fu(l, x)
		{
			in >> s;
			fu(c, y)
				grid[l][c] = s[c];
		}
		solve(x, y, i);
		out << "Case #" << i+1 << ":" << endl;
		fu(lin, x)
		{
			fu(col, y)
			{
				out << grid[lin][col];
			}
			out<<endl;
		}

	}
	return 0;
}
