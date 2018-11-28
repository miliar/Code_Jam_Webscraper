#include <iostream>
#include <cstdio>
#include <string>
using namespace std;

typedef long long ll;

#define ri(x) scanf("%d", &x)
#define FOR(i,S,E) for(int i=S; i<E; i++)

int ans[20];
char ANS[20];

int main () {
	string str; int T, i=1;
	cin >> T;
	FOR(t,1,T+1) {
		cin >> str;
		char k = str[0];
		if (str.size() == 1) {
			cout << "Case #" << t << ": " << k << endl;
			continue;
		}

		int id=1; char k2;

		while(id < str.size()) {
			//cout << str << endl;
			k2 = str[id];
			if (k2 >= k) {
				id++;
				k = k2;
			}
			else {
				while(k > k2) {
					FOR(i,id,str.size())
						str[i] = '9'; 
					str[id-1] = (str[id-1] - '0' - 1 + 10)%10 + '0';
					if (id - 1 == 0) break;
					k = str[id-2]; k2 = str[id-1];
					id--;
				}
			}
		}
		id=0;
		while(str[id] == '0') id++;
		FOR(i,id,str.size()) {
			ANS[i-id] = str[i];
		}
		ANS[str.size()-id] = '\0';
		cout << "Case #" << t << ": " << ANS << endl;
	}
}