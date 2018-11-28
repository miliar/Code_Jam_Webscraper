#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <iostream>
using namespace std;
char a[100][100];
int T,n,m;
int main(){
	//		freopen("in.txt", "r", stdin);\
//		freopen("out.txt", "w", stdout);
	scanf("%d", &T);
	for (int tt = 1; tt <= T; tt++){
  		scanf("%d %d\n", &n, &m);
		for (int i = 0; i < n; i++)
			scanf("%s\n", a[i]);
		if (tt == 50){
			//for (int i = 0; i < n; i++)
			//	fprintf(stderr, "%s\n", a[i]);
		}
		for (int i = 0; i < n; i++){
			int lchar = 0;
			for (int j = 0; j < m; j++){
				if (a[i][j] == '?'){
					a[i][j] = lchar;
				}else lchar = a[i][j];
			}
		}
		for (int i = 0; i < n; i++){
			int flag = 0, flag1 = 0;
			for (int j = m-1; j >= 0; j--){
				if (a[i][j] != '?' && a[i][j] != 0)
					flag1 = a[i][j];
				if (a[i][j] == '?' || a[i][j] == 0)
					flag = 1;
			}
			//cout << "!!" << flag << " " << flag1 << endl;
			if (flag){
				if (flag1 != 0){
					int j = 0;
					while (a[i][j] == '?' || a[i][j] == 0){
						a[i][j] = flag1, j++;
					}
				}else{
					if (i == 0) continue;
					for (int j = 0; j < m; j++)
						a[i][j] = a[i - 1][j];
				}
			}
		}
		for (int i = n - 2; i >= 0; i--){
			int flag = 0;
			for (int j = m - 1; j >= 0; j--)
				if (a[i][j] == '?' || a[i][j] == 0)
					flag = 1;
			if (flag){
				for (int j = 0; j < m; j++)
					a[i][j] = a[i + 1][j];
			}
		}
		printf("Case #%d:\n",tt);
		for (int i = 0; i < n; i++)
			printf("%s\n", a[i]);
	}
	return 0;
}
