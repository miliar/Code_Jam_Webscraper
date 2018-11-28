#include <cstdio>
#include <iostream>
#include <cstring>

using namespace std;

string testfile = "B-large";

string S;
char ans[32];


bool flag = false;
int L;

void dfs(int dep,int last_digi,bool smaller) {
	if (dep==L) {
		flag = true;
		return;
	}

	//cout<<dep<<' '<<ans<<endl;

	if (smaller) {
		ans[dep] = '9';
		dfs(dep+1,'9',smaller);
	}

	if (flag) return;

	if (S[dep]>=last_digi) {
		ans[dep] = S[dep];
		dfs(dep+1,S[dep],smaller);
	}

	if (flag) return;

	if (S[dep]>'0' && S[dep]-1>=last_digi) {
		ans[dep] = S[dep]-1;
		dfs(dep+1,S[dep]-1,1);
	}
}

void run() {
	cin>>S;
	L = S.length();

	memset(ans,0,sizeof(ans));

	flag = false;
	dfs(0,0,false);

	int leading = 0;
	while (leading<L && ans[leading]=='0')
		++leading;

	for (int i = leading; i<L; ++i)
		cout<<ans[i];
	cout<<endl;
}

int main() {
	freopen((testfile+".in").c_str(),"r",stdin);
	freopen((testfile+".out").c_str(),"w",stdout);
	int testn;
	cin>>testn;
	for (int loop = 1; loop<=testn; ++loop) {
		cout<<"Case #"<<loop<<": ";

		run();
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
