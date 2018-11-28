#include <bits/stdc++.h>
using namespace std;

#define Pi 3.141592653589793
#define eps 1e-9
#define MAX int(1e9)
#define MIN int(-1e9)
#define SQR(n) (n*n)
#define MEM(a,val) memset(a,val,sizeof(a))
#define ll long long
#define vi vector<int>
#define vll vector<ll>
#define vii vector< vector<int> >
#define pb push_back
#define F first
#define S second
#define SS stringstream
#define all(v) ((v).begin(),(v).end())
#define FOR(i,a,b) for(int i = a; i <= b; i++)
#define FORD(i,a,b) for(int i = b; i >= a; i--)
#define ul unsigned long
#define READ freopen("input.txt", "r", stdin);
#define WRITE freopen("output.txt", "w", stdout);
#define fast_io ios_base::sync_with_stdio(false)
#ifdef _WIN32
#  define LLD "%I64d"
#else
#  define LLD "%lld"
#endif

ll mod(ll a, ll b) // calculates a%b, not remainder
{
	ll ans;
	if(b == 0)
		return -1;
	else
	{
		ans = (a<0 ? mod(((a%b)+b),b) : a%b);
	}
	return ans;
}

int main()
{
	fast_io;
	ifstream in_file("A-large.in");
	ofstream out_file("file_1.out");
	int t;
	in_file>> t;
	FOR(m,0,t-1){ 
		string s;
		int k;
		in_file>> s;
		in_file>> k;
		int n = s.size();
		int count = 0;
		bool flag = false;
		out_file << "Case #" << m+1 << ": ";
		for(int i = 0; i < n; i++){
			if(s[i] == '-'){
				if(i+k-1 > n-1){
					flag = true;
					out_file<< "IMPOSSIBLE" << endl;
					break;
				}
				for(int j = i; j < i+k; j++){
					if(s[j] == '-') s[j] = '+';
					else s[j] = '-';
				}
				count++;
			}
		}
		if(!flag)
			out_file << count << endl;
	}
	return 0;
}