#include <iostream>
using namespace std;
string s;
int k;
int t;
int kase;
void flip(int start, int end)
{
	for(int i=start; i<=end; i++){
		if(s[i] == '+')
			s[i] = '-';
		else if(s[i] == '-')
			s[i] = '+';
	}

}

int main()
{
	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);
	cin >> t;
	while(t--){
		int cnt=0,cntplus=0;
		cin >> s;
		cin >> k;
		for(int i=0; i < s.length()-k+1; i++){
			if(s[i] == '+') continue;
			if(s[i] == '-') {
				flip(i, i+k-1);
				cnt++;
			}
		}
		for(int i=0; i < s.length(); i++){
			if(s[i] == '+'){
				cntplus++;
			}
		}
		if(cntplus == s.length())
			cout << "Case #" << ++kase << ": " << cnt << "\n";
		else
			cout << "Case #" << ++kase << ": " << "IMPOSSIBLE\n";
	}
	return 0;
}