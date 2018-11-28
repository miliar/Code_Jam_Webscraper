#include <cstdio>
#include <cstring>

using namespace std;

bool panCake[1001];
int t;
int panNum;
int flip;
char pan[1001];

int main() {

	scanf("%d", &t);
	for(int testcase=1; testcase<=t; testcase++) {
		scanf("%s %d", pan, &flip);
		panNum=strlen(pan);
		for(int i=0; i<panNum; i++) {
			if(pan[i]=='+')
				panCake[i]=true;
			else
				panCake[i]=false;
		}

		int ans=0;
		for(int i=0; i<panNum-flip+1; i++) {
			if(!panCake[i]) {
				for(int j=0; j<flip; j++)
					panCake[i+j]=!panCake[i+j];
				ans++;
			}
		}

		bool flag=true;
		for(int i=0; i<panNum; i++) {
			if(!panCake[i]) {
				flag=false;
				break;
			}
		}

		if(flag)
			printf("Case #%d: %d\n", testcase, ans);
		else
			printf("Case #%d: IMPOSSIBLE\n", testcase);
	}

	return 0;
}