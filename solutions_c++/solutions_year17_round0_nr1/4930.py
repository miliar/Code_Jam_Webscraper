#include <bits/stdc++.h>

using namespace std;

#define debug(x) cerr << "  - " << #x << ": " << x << endl;
#define debugs(x, y) cerr << "  - " << #x << ": " << x << "         " << #y << ": " << y << endl;

typedef long long ll;


int main(){
	int t;
	cin >> t;
	int tst = 1;
	while(t--){
		string ss;
		int k;
		cin >> ss;
		cin >> k;
		int cnt = 0;
		for(int i = 0; i <= ss.size() - k; i++){
			if(ss[i] == '-'){
				cnt++;
				for(int j = i; j < i + k; j++){
					if(ss[j] == '-')
						ss[j] = '+';
					else
						ss[j] = '-';
				}
			}
			//debug(ss);
		}
		bool impossible = false;
		for(int i = 0; i < ss.size(); i++)
			if(ss[i] == '-')
				impossible = true;
		
		if(impossible)
			printf("Case #%d: IMPOSSIBLE\n", tst++);
		else
			printf("Case #%d: %d\n", tst++, cnt);
	}
	return 0;
}