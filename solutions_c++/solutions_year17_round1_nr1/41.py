#include <iostream>
#include <cstdio>
#include <cstdlib>

using namespace std;

int n,m;
char s[30][30];
int tt;

int main() {
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);

	scanf("%d\n",&tt);
	for (int ii=1;ii<=tt;++ii) {
		scanf("%d%d\n",&n,&m);
		for (int i=0;i<n;++i)
			scanf("%s\n",s[i]);

		for (int i=0;i<n;++i) {
			bool flag=false;
			for (int j=0;j<m;++j)
				if (s[i][j]!='?') flag=true;

			if (!flag) {
				for (int j=0;j<m;++j)
					if (i>0) s[i][j]=s[i-1][j];
				continue;
			}
			for (int j=1;j<m;++j)
				if (s[i][j]=='?') s[i][j]=s[i][j-1];
			for (int j=m-2;j>=0;--j) 
				if (s[i][j]=='?') s[i][j]=s[i][j+1];
		}

		for (int i=n-2;i>=0;--i) {
			bool flag=false;
			for (int j=0;j<m;++j)
				if (s[i][j]!='?') flag=true;

			if (!flag)
				for (int j=0;j<m;++j)
					s[i][j]=s[i+1][j];
		}

		printf("Case #%d:\n",ii);
		for (int i=0;i<n;++i)
			printf("%s\n",s[i]);
	}
}