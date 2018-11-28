#include <cstdio>
#include <cstdlib>
#include <cstring>

void print_result(char map[][30], int r, int c, int caseNum)
{
	int i, j;
	printf("Case #%d:\n", caseNum);
	for(i = 0;i < r;i++){
		for(j = 0;j < c;j++)
			printf("%c", map[i][j]);
		printf("\n");
	}
}

int main()
{
	int t, caseNum = 1, i, j, k, r, c, ans, nnz;
	char map[30][30];
	scanf("%d", &t);
	while(t--){
		scanf("%d%d", &r, &c);
		for(i = 0;i < r;i++)
			scanf("%s", map[i]);
		
		for(i = 0;i < r;i++){
			nnz = -1;
			for(j = 0;j < c;j++){
				if(map[i][j] == '?' && nnz >= 0){
					map[i][j] = map[i][j - 1];
				}
				if(map[i][j] != '?' && nnz == -1){
					nnz = j;
					for(k = 0;k < j;k++)
						map[i][k] = map[i][j];
				}
			}
		}
		for(i = 0;i < c;i++){
			nnz = -1;
			for(j = 0;j < r;j++){
				if(map[j][i] == '?' && nnz >= 0){
					map[j][i] = map[j - 1][i];
				}
				if(map[j][i] != '?' && nnz == -1){
					nnz = i;
					for(k = 0;k < j;k++)
						map[k][i] = map[j][i];
				}
			}
		}
		
		print_result(map, r, c, caseNum);
		caseNum++;
	}
	return 0;
}
