#pragma comment(linker, "/STACK:108777216")
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cmath>
#include <vector>
#include <deque>
#include <set>
#include <utility>
#include <algorithm>
#include <ctime>
using namespace std;

int const MAX_N = 1024 * 1024;
int const MAX_CH = 5000010;
int const INT_INF = 1000000000;

char st[MAX_CH],ans[MAX_CH],init_ans[MAX_CH];
double our_t[MAX_N];
int rr[10];

struct pp {int cnt;
char ch;} s[1000];

bool operator < (const pp &a, const pp &b) {
	return a.cnt > b.cnt;
}

int is_Ok(char * ans, int n) {
	int Ok = 1;
		for (int i=0; i<n; i++)
			if (ans[i] == '#') return 0;
		for (int i=0; i+1<n; i++)
			if (ans[i] == ans[i+1]) return 0;
		if (ans[0] == ans[n-1]) return 0;
		return 1;
}

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int tt;
	gets(st);
	sscanf(st,"%d",&tt);
	for (int qq=0; qq<tt; qq++) {
		int r,o,y,g,b,v;
		int nnn;
		scanf("%d%d%d%d%d%d%d",&nnn,&r,&o,&y,&g,&b,&v);
				
		printf("Case #%d: ",qq+1);

		s[0].cnt = r; s[0].ch = 'R';
		s[1].cnt = y; s[1].ch = 'Y';
		s[2].cnt = b; s[2].ch = 'B';

		sort(s,s+3);
		int n = s[0].cnt + s[1].cnt + s[2].cnt;
		for (int i=0; i<n; i++) ans[i] = '#';
		char lst = '@';
		for (int i=0; i<n; i++) {
			int fnd = 0;
			int ans_j = -1;
			for (int j=0; j<3; j++)
				if (s[j].cnt > 0 && s[j].ch != lst) {
					fnd = 1;
					ans_j = j;
					break;
				}
			if (!fnd)
				break;
			ans[i] = s[ans_j].ch;
			s[ans_j].cnt--;
			lst = s[ans_j].ch;
			sort(s,s+3);
		}

		int Ok = 1;
		for (int i=0; i<n; i++)
			if (ans[i] == '#') Ok = 0;
		for (int i=0; i+1<n; i++)
			if (ans[i] == ans[i+1]) Ok = 0;
		if (ans[0] == ans[n-1]) Ok = 0;

		if (!Ok) {
			Ok = 1;
			swap(ans[n-1],ans[n-2]);
			for (int i=0; i<n; i++)
				if (ans[i] == '#') Ok = 0;
			for (int i=0; i+1<n; i++)
				if (ans[i] == ans[i+1]) Ok = 0;
			if (ans[0] == ans[n-1]) Ok = 0;
		}

		if (!Ok) {
			Ok = 1;
			for (int j=0; j<3; j++) rr[j] = j;
			for (int i=0; i<n; i++) init_ans[i] = ans[i];
			for (int j=0; j<3; j++) ans[n-1-j] = init_ans[n-1-rr[j]];
			if (!is_Ok(ans,n)) {
				Ok = 0;
				while (!Ok && next_permutation(rr,rr+3)) {
					Ok = 1;
					for (int j=0; j<3; j++) ans[n-1-j] = init_ans[n-1-rr[j]];
					if (!is_Ok(ans,n))
						Ok = 0;
				}
			}
		}

		if (!Ok) printf("IMPOSSIBLE");
		else {
			ans[n] = 0;
			printf("%s",ans);
		}
		printf("\n");
	}
	
	return 0;
}