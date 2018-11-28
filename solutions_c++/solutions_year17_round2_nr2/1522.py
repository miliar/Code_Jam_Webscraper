#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>

using namespace std;

int con[6][6] = {{0,0,1,1,1,0}, {0,0,0,1,1,1}, {1,0,0,0,1,1}, 
				 {1,1,0,0,0,1}, {1,1,1,0,0,0}, {0,1,1,1,0,0}};
				 
int rec[1024], ccc;
char ss[8] = "ROYGBV";

int main(){
	int T;
	cin >> T;
	int index = 0;

	while (index++ < T){
		int n, a[6];
		scanf("%d", &n);
		for(int i = 0; i < 6; i ++)scanf("%d", &a[i]);
		
		bool noAns = false;
		for(int i = 0; i < 6; i ++)
		{
			int sum = 0;
			for(int j = 0; j < 6; j ++)
			{
				if(con[i][j] == 1)
				{
					sum += a[j];
				}
			}
			if(sum < a[i])noAns = true;
		}
		
		int v = -1;
		ccc = 0;
		while(ccc < n)
		{
			int mx = 0;
			int cur = -1;
			for(int i = 0; i < 6; i ++)
			{
				if (v == -1 || con[v][i] == 1)
				{
					if(a[i] > mx || (a[i] == mx && i == rec[0])) 
					{
						cur = i;
						mx = a[i];
					}
				}
			}
			if(cur == -1)break;
			a[cur] --;
			rec[ccc++] = cur;
			v = cur;
		}
		
		if(con[rec[ccc-1]][rec[0]] == 0)noAns = true;
		
		if(ccc < n || noAns)
		{
			cout << "Case #" << index << ": IMPOSSIBLE" << endl;
		}
		else {
			cout << "Case #" << index << ": ";
			for(int i = 0; i < ccc; i ++)
			{
				putchar(ss[rec[i]]);
			}
			putchar('\n');
		}
		
	}
	return 0;
}
