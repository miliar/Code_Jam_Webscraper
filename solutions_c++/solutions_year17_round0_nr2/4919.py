#include <bits/stdc++.h>

using namespace std;

#define debug(x) cerr << "  - " << #x << ": " << x << endl;
#define debugs(x, y) cerr << "  - " << #x << ": " << x << "         " << #y << ": " << y << endl;

typedef long long ll;


int main(){
	int t, tst = 1;
	cin >> t;

	while(t--){
		string ss;
		cin >> ss;
		int sz = ss.size();
		for(int i = 1; i < sz; i++){
			if(ss[i] < ss[i - 1]){
				int j = i - 1;
				while(j - 1 >= 0 && ss[j - 1] == ss[i - 1]){
					j--;
				}
				ss[j]--;
				for(int k = j + 1; k < sz; k++)
					ss[k] = '9';
			}
		}

		printf("Case #%d: ", tst++);
		for(int i = 0; i < ss.size(); i++){
			if(ss[i] == '0')
				continue;
			printf("%c", ss[i]);
		}
		printf("\n");
	}
	return 0;
}