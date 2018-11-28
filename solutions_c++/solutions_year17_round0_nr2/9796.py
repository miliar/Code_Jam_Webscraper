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
	ifstream in_file("B-small-attempt3.in");
	ofstream out_file("file_2.out");
	int t;
	in_file >> t;
	FOR(i,0,t-1){
		string s;
		in_file >> s;
		int length = s.size();
		int j;
		for(j = 0; j < length-1; j++){
			if(s[j] == s[j+1] && j+2 < length && s[j+2] < s[j])
			{
				s[j] = char(s[j]-'1'+'0');
				break;
			}
			else if(s[j] > s[j+1]){
				s[j] = char(s[j]-'1'+'0');
				break;
			}
		}
		for(int k = j+1; k < length; k++){
			s[k] = '9';
		}
		out_file << "Case #" << i+1 << ": ";
		bool flag = false;
		FOR(j,0,length-1){
			if(s[j] != '0' && !flag) flag = true; 
			if(flag) out_file << s[j];
		}
		out_file << endl;
	}
	return 0;
}