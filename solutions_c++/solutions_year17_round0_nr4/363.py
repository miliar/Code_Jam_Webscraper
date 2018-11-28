#include <cstdio>
#include <cstring>
#include <queue>
#include <vector>
using namespace std;

bool fillxy[100];
bool filld[200];
char grid[100][100], mov[100][100];;

int main(){
	int cases;
	scanf("%d", &cases);
	
	int n, m;
	for(int z=1; z<=cases; z++){
		scanf("%d %d", &n, &m);
		memset(fillxy, false, sizeof(fillxy));
		memset(filld, false, sizeof(filld));
		memset(grid, '.', sizeof(grid));
		memset(mov, '.', sizeof(mov));
		
		int sc = 0;
		char ch[2];
		int r, c;
		for(int i=0; i<m; i++){
			scanf("%s %d %d", ch, &r, &c);
			grid[r-1][c-1] = ch[0];
			switch(ch[0]){
				case 'x':
					fillxy[c-1] = true;
					sc++;
					break;
				case '+':
					filld[r-1 + c-1] = true;
					sc++;
					break;
				case 'o':
					fillxy[c-1] = true;
					filld[r-1 + c-1] = true;
					sc += 2;
					break;
			}
		}
		
		//add x
		for(int i=0; i<n; i++){
			bool add = true;
			for(int j=0; j<n; j++){
				if(grid[i][j] == 'x' || grid[i][j] == 'o'){
					add = false;
					continue;
				}
			}
			if(!add) continue;
			for(int j=0; j<n; j++){
				if(fillxy[j]) continue;
				fillxy[j] = true;
				if(grid[i][j] == '+'){
					mov[i][j] = 'o';
				}else{
					mov[i][j] = 'x';
				}
				sc++;
				break;
			}
		}
		
		//add +
		int br = 0;
		int bc = n;
		int er = -1;
		int ec = n-1;
		for(int i=0; i<2*n-1; i++){
			if(bc > 0){ bc--; er++; }
			else{ br++; ec--; }
			bool add = true;
			for(int j=0; ; j++){
				if(br+j >= n || bc+j >= n) break;
				if(grid[br+j][bc+j] == '+' || grid[br+j][bc+j] == 'o'){
					add = false;
					continue;
				}
			}
			if(!add) continue;
			for(int j=0; ; j++){
				if(br+j > er-j || bc+j > ec-j) break;
				if(!filld[br+bc+2*j]){
					filld[br+bc+2*j] = true;
					if(grid[br+j][bc+j] == 'x'){
						mov[br+j][bc+j] = 'o';
					}else{
						if(mov[br+j][bc+j] == '.'){
							mov[br+j][bc+j] = '+';
						}else{
							mov[br+j][bc+j] = 'o';
						}
					}
					sc++;
					break;
				}else if(!filld[er+ec-2*j]){
					filld[er+ec-2*j] = true;
					if(grid[er-j][ec-j] == 'x'){
						mov[er-j][ec-j] = 'o';
					}else{
						if(mov[er-j][ec-j] == '.'){
							mov[er-j][ec-j] = '+';
						}else{
							mov[er-j][ec-j] = 'o';
						}
					}
					sc++;
					break;
				}
			}
		}
		vector<char> mch;
		vector<int> mr, mc;
		for(int i=0; i<n; i++){
			for(int j=0; j<n; j++){
				if(mov[i][j] != '.'){
					mch.push_back(mov[i][j]);
					mr.push_back(i);
					mc.push_back(j);
				}
			}
		}
		// for(int i=0; i<n; i++){
			// for(int j=0; j<n; j++){
				// printf("(%c%c)", grid[i][j], mov[i][j]);
			// }
			// printf("\n");
		// }
		
		printf("Case #%d: %d %d\n", z, sc, mch.size());
		for(int i=0; i<mch.size(); i++){
			printf("%c %d %d\n", mch[i], mr[i]+1, mc[i]+1);
		}
	}
	
	return 0;
}