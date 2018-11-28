#include<iostream>

using namespace std;

int main(){
	freopen("A-large.in","r",stdin);
	freopen("C.txt","w",stdout);
	int t;
	cin>>t;

	int p=1;
	while(p<=t){
		int r,c;
		cin>>r>>c;
		char mat[r][c];
		bool flag[r][c];
		for(int i=0;i<r;i++){
			for(int j=0;j<c;j++)
				flag[i][j] = 0;
		}
		for(int i=0;i<r;i++){
			for(int j=0;j<c;j++)
				{
					cin>>mat[i][j];
				 if(mat[i][j]!='?')
				 	flag[i][j] = 1;
				}
		}

		char row[r];
		char col[r];

		for(int i=0;i<r;i++)
			row[i] = 'a';

		for(int i=0;i<c;i++)
			col[i] = 'a';	

        for(int i=0;i<r;i++){
			for(int j=0;j<c;j++)
				if(mat[i][j]>='A' && mat[i][j]<='Z' && flag[i][j]==1){
					int a,b;
					a=i;
					b=j+1;
					while(b<c && flag[a][b]==0){
							mat[a][b] = mat[i][j];
								b++;
							}
				
					a=i;
					b=j-1;
					while(b>=0 && flag[a][b]==0){
							mat[a][b] = mat[i][j];
								b--;
			}				}
				
		} 
        for(int i=0;i<r;i++){
			for(int j=0;j<c;j++)
				if(mat[i][j]=='?'){
									if(i>0)
									mat[i][j] = mat[i-1][j];
								else
									mat[i][j] = mat[i+1][j];}
		}

		  for(int i=r;i>=0;i--){
			for(int j=c;j>=0;j--)
				if(mat[i][j]=='?'){
									
									mat[i][j] = mat[i+1][j];}
		}

		cout<<"Case #"<<p<<":"<<endl;
		for(int i=0;i<r;i++){
			for(int j=0;j<c;j++)
				cout<<mat[i][j];
			cout<<endl;
		}

		p++;
	}
}