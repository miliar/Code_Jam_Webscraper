#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define F first
#define S second
#define oioi printf("oioi\n")
#define eoq cout << "eoq" << '\n'
using namespace std;
typedef long long int ll;
typedef unsigned long long int llu;
typedef pair<ll, ll> ii;
typedef pair<double, double> dd;
typedef vector<ll> vi;
typedef vector<ii> vii;
const int dx[] = {0 ,1,-1,0,1,-1,-1, 1};
const int dy[] = {-1,0,0, 1,1, 1,-1,-1};
const ll MOD = 0;
const ll N = 0;

string s;
string saida;
bool ok;

void solve(int pos, bool bate, int ult, string atual){
	if(ok) return;
	if(pos==s.size()){
		ok = true;
		saida = atual;
		return;
	}
	
	
	if(bate){
		for (int i = s[pos]-'0'; i >= ult; i--)
		{
			solve(pos+1, i==s[pos]-'0' ? true : false, i, atual+char(i+'0'));
		}
		
	}else{
		for (int i = 9; i >= ult; i--)
		{
			solve(pos+1, false, i, atual+char(i+'0'));
		}
	}
}

int main () {
	int t, caso=1;
	cin >> t;
	
	while (t--)
	{
		cin >> s;
		ok = false;
		solve(0, true, 0, "");
		while (saida[0]=='0')
		{
			saida.erase(saida.begin());
		}
		
		cout << "Case #" << caso++ << ": " << saida << "\n";
	}
	
	
	
	return 0;
}
