#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<stack>
#include<queue>
#include<vector>
#include<set>
#include<map>

const int mod=1000000007;

using namespace std;

int t;
int r, c;

char grid[30][30];

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d", &t);
	for(int cases=1;cases<=t;cases++){
        scanf("%d %d", &r, &c);
        for(int i=0;i<r;i++) scanf("%s", grid[i]);
        for(int i=0;i<r;i++){
            for(int j=0;j<c;j++){
                if(grid[i][j]!='?'){
                    for(int k=j+1;k<c;k++){
                        if(grid[i][k]!='?') break;
                        grid[i][k]=grid[i][j];
                    }
                }
            }
            for(int j=c-1;j>=0;j--){
                if(grid[i][j]!='?'){
                    for(int k=j-1;k>=0;k--){
                        if(grid[i][k]!='?') break;
                        grid[i][k]=grid[i][j];
                    }
                }
            }
        }
        for(int j=0;j<c;j++){
            for(int i=0;i<r;i++){
                if(grid[i][j]!='?'){
                    for(int k=i+1;k<r;k++){
                        if(grid[k][j]!='?') break;
                        grid[k][j]=grid[i][j];
                    }
                }
            }
            for(int i=r-1;i>=0;i--){
                if(grid[i][j]!='?'){
                    for(int k=i-1;k>=0;k--){
                        if(grid[k][j]!='?') break;
                        grid[k][j]=grid[i][j];
                    }
                }
            }
        }
        printf("Case #%d:\n", cases);
        for(int i=0;i<r;i++) printf("%s\n", grid[i]);
	}
}
