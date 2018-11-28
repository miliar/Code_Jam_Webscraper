#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <stdlib.h>
#include <string.h>
using namespace std;

char mat[100][100];
int math[100][100];
int R, C;
void maxim(int y, int x){
	//for all x1<=x to x2>=x && y1<=y to y2>=y
	int ty1=0, ty2=0, tx1=0, tx2=0, mx=-1;
	int s=0;
	//cout<<"** "<<mat[y][x]<<endl;
	for(int y1=0;y1<=y;y1++)
		for(int y2=y;y2<R;y2++)
			for(int x1=0;x1<=x;x1++)
				for(int x2=x;x2<C;x2++){
					s=0;
					for(int i=y1;i<=y2;i++)	
						for(int j=x1;j<=x2;j++)
							if(mat[i][j]!='?')s++;
					if(s==1){
						//cout<<"this"<<endl;
						if((y2-y1+1)*(x2-x1+1)>mx){
							mx=(y2-y1+1)*(x2-x1+1);
							ty1=y1;
							ty2=y2;
							tx1=x1;
							tx2=x2;
							//cout<<"Ok..."<< mx<<endl;
						}
					}
					//cout<<endl;
				}
				for(int i=ty1;i<=ty2;i++){
					for(int j=tx1;j<=tx2;j++){
						mat[i][j]=mat[y][x];
						//cout<<mat[i][j];
					}
					//cout<<endl;
				}
}
void _main(){
	cin>>R>>C;

	for(int i=0;i<R;i++){
		for(int j=0;j<C;j++){
			cin>>mat[i][j];
			if(mat[i][j]=='?')
				math[i][j]=0;
			else
				math[i][j]=1;
		}
	}

	//MAGIC
	for(int i=0;i<R;i++){
		for(int j=0;j<C;j++){
			if(mat[i][j]!='?' && math[i][j]==1){
				maxim(i,j);
			}
		}
	}

	for(int i=0;i<R;i++){
		for(int j=0;j<C;j++){
			cout<<mat[i][j];
		}
		cout<<endl;
	}

}
int main(){
	int tt, ans;
	cin>>tt;
	for(int t=0;t<tt;t++){
		printf("Case #%d:\n",t+1);
		_main();
	}
	return 0;
}