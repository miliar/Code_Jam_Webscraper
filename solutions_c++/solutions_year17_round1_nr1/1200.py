#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>

using namespace std;

int main(){
	int T;
	cin >> T;
	int index = 0;

	while (index++ < T){
		int R, C;
		char mat[32][32];
		
		scanf("%d %d", &R, &C);
		
		for(int i = 0; i < R; i ++)
		{
			scanf("%s", mat[i]);
		}
		
		int splitline = -1;
		for(int i = 0; i < R; i ++)
		{
			char pre = '?';
			for(int j = 0; j < C; j ++)
			{
				if(mat[i][j] != '?')
				{
					if(pre == '?')
					{
						for(int k = 0; k < j; k ++)
						{
							mat[i][k] = mat[i][j];
						}
					}
					pre = mat[i][j];
					if(splitline == -1)
					{
						splitline = i;
					}
				}
				else{
					if(pre != '?')
					{
						mat[i][j] = pre;
					}
					else if(splitline != -1 && i > 0)
					{
						mat[i][j] = mat[i-1][j];
					}
				}
			}
		}
		
		for(int i = splitline-1; i >= 0; i --)
		{
			char pre = '?';
			for(int j = 0; j < C; j ++)
			{
				if(mat[i][j] != '?')
				{
					if(pre == '?')
					{
						for(int k = 0; k < j; k ++)
						{
							mat[i][k] = mat[i][j];
						}
					}
					pre = mat[i][j];
				}
				else{
					if(pre != '?')
					{
						mat[i][j] = pre;
					}
					else if(splitline != -1)
					{
						mat[i][j] = mat[i+1][j];
					}
				}
			}
		}
		
		cout << "Case #" << index << ":" << endl;
		for(int i = 0; i < R; i ++)
		{
			printf("%s\n", mat[i]);
		}
	}
}
