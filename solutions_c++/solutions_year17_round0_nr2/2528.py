#include <cstdio>
#include <string>

using namespace std;

int t;
string number;
char cnum[20];

string solve(string number) {
	char cmp=number[number.length()-1];
	for(int i=number.length()-2; i>=0; i--) {
		if(number[i]>cmp) {
			number[i]-=1;
			for(int j=i+1; j<number.length(); j++)
				number[j]='9';
		}
		cmp=number[i];
	}

	return number;
}

int main() {

	scanf("%d", &t);
	for(int testcase=1; testcase<=t; testcase++) {
		scanf("%s", cnum);
		number=cnum;

		string ans=solve(number);
		for(int i=0; i<ans.length(); i++) {
			if(ans[i]!='0') {
				ans=ans.substr(i);
				break;
			}
		}
		printf("Case #%d: %s\n", testcase, ans.c_str());
	}

	return 0;
}
