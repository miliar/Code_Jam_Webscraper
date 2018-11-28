
// In the name of God
#include <bits/stdc++.h>

using namespace std;
#define Size(x) ((int)(x).size())
#define pb push_back
typedef long long ll;
typedef long double ld;
typedef pair<int,int>pii;
const int INF = 1e9 + 10;

bool is[33];

int main()
{
	ios_base :: sync_with_stdio(false) ,cin.tie(0) , cout.tie(0);
	int T;cin>>T;
	int cnt = 0;
	while(T--){
		++cnt;
		string s;cin>>s;
		cout << "Case #" << cnt << ": ";
		bool fl = false;
		for(int i=0;i<Size(s)-1;++i)
			if(s[i] > s[i+1]) fl = true;
		if(!fl){
			cout << s << '\n';
			continue;
		}
		fl = false;
		is[0] = true;
		for(int i=1;i<Size(s);++i)
			is[i] = is[i-1] && (s[i-1] < s[i]);
		for(int i=Size(s)-1;~i && !fl;--i){
			if(is[i] && ((i == 0 && s[i]-'1') || (i != 0 && s[i] - s[i-1] > 0))){
				fl = true;
				s[i]--;
				for(int j=i+1;j<Size(s);++j) s[j] = '9';
			}
		}
		if(fl){
			cout << s << '\n';
			continue;
		}
		for(int i=0;i<Size(s)-1;++i) cout << 9;cout << '\n';
	}
	return 0;
}

