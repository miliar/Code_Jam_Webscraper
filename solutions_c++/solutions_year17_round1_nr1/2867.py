// devsks 
//codeJam
//	08.04.2017
#include "bits/stdc++.h"

using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int tt=1;tt<=t;tt++){
		
		int r,c;
		cin>>r>>c;
		char str[r][c+1];
		for(int i=0;i<r;i++)
			scanf("%s",str[i]);
		map<pair<int,int>, bool> mat;
		for(int i=0;i<r;i++){
			for(int j=0;j<c;j++){
				if(str[i][j]!='?' && mat[make_pair(i,j)]==false){
					int x = j+1;
					while(x < c && str[i][x]=='?'){
						mat[make_pair(i,x)]=true;
						str[i][x] = str[i][j];
						x++;
					}
					if(x!=j+1)
						mat[make_pair(i,j)] = true;
					x = j-1;
					while(x >=0 && str[i][x]=='?'){
						mat[make_pair(i,x)]  =true;
						str[i][x] = str[i][j];
						x--;
					}
					if(x!=j-1)
						mat[make_pair(i,j)] = true;

				}
				if(str[i][j]!='?' && mat[make_pair(i,j)]==false){
					int x = i-1;	
					while(x >=0 && str[x][j]=='?'){
						str[x][j] = str[i][j];
						mat[make_pair(x,j)] = true;
						x--;
					}
					if(x!=i-1)
						mat[make_pair(i,j)]=true;
					x = i+1;
					while(x < r && str[x][j]=='?'){
						str[x][j] =str[i][j];
						mat[make_pair(x,j)] = true;
						x++;
					}
					if(x!=i+1)
						mat[make_pair(i,j)] = true;
				}
			}
		
		}
		for(int i=0;i<r;i++){
			int flag=0,s,e;
			for(int j=0;j<c;j++)
				if(str[i][j]=='?'){
					if(flag==0)
						s = j;
					flag++;
				}
			if(flag){
				int skip=0;
				if(i){
					if(s==0){
						strncpy(str[i],str[i-1],flag);
					}
					else if(s && str[i-1][s]!=str[i-1][s-1])
						strncpy(str[i]+s,str[i-1]+s,flag);
					else
						skip=1;
				
				}
				else
					skip=1;
				if(skip && i+1 < r)
					strncpy(str[i]+s,str[i+1]+s,flag);
			
			}
		
		}	
		cout<<"Case #"<<tt<<":\n";
		for(int i=0;i<r;i++)
			puts(str[i]);
	}


	return 0;
}
