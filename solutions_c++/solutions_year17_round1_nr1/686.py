
// In the name of God
#include <bits/stdc++.h>

using namespace std;
#define Size(x) ((int)(x).size())
#define pb push_back
typedef long long ll;
typedef long double ld;
typedef pair<int,int>pii;
const int INF = 1e9 + 10;
const int MN = 33;

string s[MN];
int n , m;

void upd(string &str,string p)
{
	bool fl = false;
	for(int i=0;i<m;++i) if(str[i] != '?') fl = true;
	if(!fl){
		str = p;
		return;
	}
	for(int i=0;i<m;++i) if(i && str[i] == '?') str[i] = str[i-1];
	for(int i=m-1;~i;--i) if(i+1 < m && str[i] == '?') str[i] = str[i+1];
}

void output()
{
	for(int i=0;i<n;++i)
		cout << s[i] << '\n';
}

int main()
{
	ios_base :: sync_with_stdio(false) ,cin.tie(0) , cout.tie(0);
	int T;cin>>T;
	int cnt = 0;
	while(T--){
		++cnt;
		cin >> n >> m;
		for(int i=0;i<n;++i)
			cin >> s[i];
		cout << "Case #" << cnt << ":\n";

		int r = -1;
		for(int i=0;i<n;++i)
			for(int j=0;j<m;++j) if(s[i][j] != '?') r = i;

		if(r == -1){
			for(int i=0;i<n;++i)
				for(int j=0;j<m;++j) s[i][j] = 'A';
			output();
			continue;
		}
		for(int i=0;i<m;++i) if(s[r][i] == '?' && i) s[r][i] = s[r][i-1];
		for(int i=m-1;~i;--i) if(s[r][i] == '?' && i+1 < m) s[r][i] = s[r][i+1];
	
		for(int i=r-1;~i;--i) upd(s[i] , s[i+1]);
		for(int i=r+1;i<n;++i) upd(s[i] , s[i-1]);
		output();
	}
	return 0;
}

