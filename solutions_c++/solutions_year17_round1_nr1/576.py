
#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;

typedef long long i8;
int R,C;
bool ha[30];
char buf[30][30];

main() {
	int ccnt;
	scanf("%d", &ccnt);
	for (int cs=1; cs<=ccnt; cs++) {
		scanf("%d%d",&R,&C);
		for (int r=0; r<R; r++)
			scanf("%s", buf+r);
		
		for (int r=0; r<R; r++) {
			ha[r]=false;
			for (int c=0; c<C; c++)
				if (buf[r][c]!='?') ha[r]=true;
			if (ha[r]) {
				for (int c=0; c<C; c++)
					if (buf[r][c]!='?') {
						for (int x=c-1; x>=0 && buf[r][x]=='?'; x--)
							buf[r][x]=buf[r][c];
						for (int x=c+1; x<C && buf[r][x]=='?'; x++)
							buf[r][x]=buf[r][c];
					}
			}
		}
		bool all;
		do {
			all = true;
			for (int r=0; r<R; r++) if (!ha[r]) {
				all=false;
				int nr=-1;
				if (r>0 && ha[r-1]) nr=r-1;
				else if (r+1<R && ha[r+1]) nr=r+1;
				if (nr>=0) {
					ha[r]=true;
					for (int c=0; c<C; c++)
						buf[r][c]=buf[nr][c];
				}
			}
		} while (!all);
		printf("Case #%d:\n", cs);
		for (int r=0; r<R; r++)
			printf("%s\n", buf[r]);
	}
}
