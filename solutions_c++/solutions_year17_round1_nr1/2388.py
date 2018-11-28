#include <iostream>
#include <cstdio>
using namespace std;

int r,c;
char board[30][30];

typedef struct {
	int lr,lc;
	int rr,rc;
}List;

int max(int x, int y){
	return x>y?x:y;
}
int min(int x, int y){
	return x>y?y:x;
}

int main(){
	int t;	cin >> t;
	for(int i=0;i<t;i++){
		cin >> r >> c;
		for(int x=0;x<30;x++){
			for(int y=0;y<30;y++){
				board[x][y]='?';
			}
		}
		List num[26] = {0};
		for(int x=0;x<26;x++){
			num[x].lr=0;
			num[x].lc=0;
			num[x].rr=0;
			num[x].rc=0;
		}

		int flag = 0;
		for(int x=0;x<r;x++){
			for(int y=0;y<c;y++){
				cin >> board[x][y];
				int tmp = board[x][y]-'A';
				num[tmp].lr = x;
				num[tmp].lc = y;
				num[tmp].rr = x;
				num[tmp].rc = y;			
			}
		}
		
		for(int x=0;x<r;x++){
			for(int y=0;y<c;y++){
				// printf("x %d y %d\n",x,y);
				// for(int a=0;a<r;a++){
				// 	for(int b=0;b<c;b++){
				// 		printf("%c",board[a][b] );
				// 	}
				// 	printf("\n");
				// }
				// printf("#######\n");

				if(board[x][y]=='?'){
					// printf("in left\n");
					for(int m=0;m<y;m++) // left
						if(board[x][m]!='?')	
							board[x][y] = board[x][m];

					int tmp = board[x][y]-'A';
					int RECT = 0;
					for(int m=min(num[tmp].lr,x);m<=max(num[tmp].rr,x);m++){
						if(RECT)	break;
						for(int n=min(num[tmp].lc,y);n<=max(num[tmp].rc,y);n++){
							if(board[m][n]!='?' && board[m][n]!=board[x][y])	RECT = 1;
							if(RECT)	break;
						}
					}
					if(RECT==0 && board[x][y]!='?'){
						num[tmp].lr = min(num[tmp].lr,x);
						num[tmp].lc = min(num[tmp].lc,y);
						num[tmp].rr = max(num[tmp].rr,x);
						num[tmp].rc = max(num[tmp].rc,y);
						for(int m=num[tmp].lr;m<=num[tmp].rr;m++){
							for(int n=num[tmp].lc;n<=num[tmp].rc;n++){
								board[m][n]=board[x][y];
							}
						}
					}
					else{
						// printf("in up\n");
						board[x][y]='?';
						for(int n=0;n<x;n++) // up
							if(board[n][y]!='?')	board[x][y] = board[n][y];

						int tmp1 = board[x][y]-'A';
						int RECT1 = 0;
						for(int m=min(num[tmp1].lr,x);m<=max(num[tmp1].rr,x);m++){
							if(RECT1)	break;
							for(int n=min(num[tmp1].lc,y);n<=max(num[tmp1].rc,y);n++){
								if(board[m][n]!='?' && board[m][n]!=board[x][y])	RECT1 = 1;
								if(RECT1)	break;
							}
						}
						if(RECT1==0 && board[x][y]!='?'){
							num[tmp1].lr = min(num[tmp1].lr,x);
							num[tmp1].lc = min(num[tmp1].lc,y);
							num[tmp1].rr = max(num[tmp1].rr,x);
							num[tmp1].rc = max(num[tmp1].rc,y);
							for(int m=num[tmp1].lr;m<=num[tmp1].rr;m++){
								for(int n=num[tmp1].lc;n<=num[tmp1].rc;n++){
									board[m][n]=board[x][y];
								}
							}
						}
						else{
							// printf("in right\n");
							board[x][y]='?';
							for(int m=c-1;m>y;m--) // right
								if(board[x][m]!='?')	board[x][y] = board[x][m];

							int tmp2 = board[x][y]-'A';
							int RECT2 = 0;
							for(int m=min(num[tmp2].lr,x);m<=max(num[tmp2].rr,x);m++){
								if(RECT2==1)	break;
								for(int n=min(num[tmp2].lc,y);n<=max(num[tmp2].rc,y);n++){
									if(board[m][n]!='?' && board[m][n]!=board[x][y])	RECT2 = 1;
									if(RECT2==1)	break;
								}
							}
							if(RECT2==0 && board[x][y]!='?'){
								num[tmp2].lr = min(num[tmp2].lr,x);
								num[tmp2].lc = min(num[tmp2].lc,y);
								num[tmp2].rr = max(num[tmp2].rr,x);
								num[tmp2].rc = max(num[tmp2].rc,y);
								for(int m=num[tmp2].lr;m<=num[tmp2].rr;m++){
									for(int n=num[tmp2].lc;n<=num[tmp2].rc;n++){
										board[m][n]=board[x][y];
									}
								}
							}
							else{
								// printf("in down\n");
								board[x][y]='?';
								for(int n=r-1;n>x;n--) // down
									if(board[n][y]!='?')	board[x][y] = board[n][y];

								int tmp3 = board[x][y]-'A';
								int RECT3 = 0;
								for(int m=min(num[tmp3].lr,x);m<=max(num[tmp3].rr,x);m++){
									if(RECT3)	break;
									for(int n=min(num[tmp3].lc,y);n<=max(num[tmp3].rc,y);n++){
										if(board[m][n]!='?' && board[m][n]!=board[x][y])	RECT3 = 1;
										if(RECT3)	break;
									}
								}
								if(RECT3==0 && board[x][y]!='?'){
									num[tmp3].lr = min(num[tmp3].lr,x);
									num[tmp3].lc = min(num[tmp3].lc,y);
									num[tmp3].rr = max(num[tmp3].rr,x);
									num[tmp3].rc = max(num[tmp3].rc,y);
									for(int m=num[tmp3].lr;m<=num[tmp3].rr;m++){
										for(int n=num[tmp3].lc;n<=num[tmp3].rc;n++){
											board[m][n]=board[x][y];
										}
									}
								}
								else{
									board[x][y]='?';
								}
							}
						}
					}
				}
			}
		}
		printf("Case #%d:\n",i+1);
		for(int x=0;x<r;x++){
			for(int y=0;y<c;y++){
				printf("%c",board[x][y]);
			}
			printf("\n");;
		}
	}
	return 0;
}