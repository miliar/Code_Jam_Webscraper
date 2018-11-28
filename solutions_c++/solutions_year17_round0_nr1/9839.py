#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <cstdlib>
#include <map>
#include <queue>

using namespace std;

struct node {
	string str;
	int cnt;
};

map<string, int> Hash;
queue<node> Q;


int T;


bool check(string S) {
	for (int i = 0 ;i <S.length(); i++)
		if (S[i] == '-') return false;
	return true;
}

string Invert(string str, int j, int K) {
	for (int i = j; i<j+K;i++) 
		if (str[i] =='-') 
			str[i] = '+';
		else
			str[i] = '-';
	return str;
}

int work(string S, int K) {

	if (check(S)) return 0;
	while (Q.size() > 0) Q.pop();
	Hash.clear();

	node data, head;
	string str, nstr;
	int cnt;
	int L;
	L = S.length() - K + 1;
	data.str = S;
	data.cnt = 0;
	Q.push(data);



	while (Q.size() > 0) {
		head = Q.front();
		str = head.str;
		cnt = head.cnt + 1;


		for (int i = 0; i<L; i++) {

			nstr = Invert(str, i, K);
			//cout<<i<<", "<<K<<":"<<str<<"	;	"<<nstr<<endl;

			if (check(nstr)) return cnt;
			if (Hash[nstr] == 0) {
				data.str = nstr;
				data.cnt  = cnt;
				Q.push(data);
				Hash[nstr] += 1;
			}
		}
		Q.pop();
	}

	return -1;


}

int main() {
	//freopen("A-small-attempt2.in","r",stdin);
	//freopen("A-small-attempt2.out", "w", stdout);

	scanf("%d", &T);
	for (int i = 1; i<= T;i++) {
		string S;
		int K;

		cin>>S>>K;

		//cout<<S<<endl;
		//cout<<S.length()<<endl;

		int ans;
		ans = work(S,K);
		if (ans >= 0)
			printf("Case #%d: %d\n", i, ans);
		else
			printf("Case #%d: IMPOSSIBLE\n", i);

	}

	return 0;
}