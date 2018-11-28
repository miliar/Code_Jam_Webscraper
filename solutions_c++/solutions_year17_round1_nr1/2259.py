#include <bits/stdc++.h>
using namespace std;
int main()
{
	freopen("/Users/rishabh-pc/Downloads/A-large (3).in","r",stdin);
    freopen("/Users/rishabh-pc/Desktop/cjA1.txt","w",stdout);
    int t;
    cin>>t;
    int tcc=1;
    while(t--){
    	  int r,c,i,j;
    	  cin>>r>>c;
    	  char mat[r][c];
    	  for(i=0;i<r;i++){
    	  	for(j=0;j<c;j++)
    	  	{
    	  		cin>>mat[i][j];
             }
		  }
    	  for(i=0;i<r;i++){
    	  	for(j=0;j<c;j++){
    	  		if(j>0 && mat[i][j-1]!='?'&& mat[i][j]=='?')
    	  		mat[i][j]=mat[i][j-1];
			  }
		  }
		  for(i=0;i<r;i++){
    	  	for(j=c-1;j>=0;j--){
    	  		if(j<c-1 && mat[i][j+1]!='?'&& mat[i][j]=='?')
    	  		mat[i][j]=mat[i][j+1];
			  }
		  }
		  int k,l;
		  for(i=1;i<r;i++){
    	  	for(j=0;j<c;j++){
    	  		if(mat[i][j]!='?')
    	  		break;
			  }
			  if(j==c){
			  	for(j=0;j<c;j++)
			  	mat[i][j]=mat[i-1][j];
			  }
		  }
		  for(i=r-2;i>=0;i--){
    	  	for(j=0;j<c;j++){
    	  		if(mat[i][j]!='?')
    	  		break;
			  }
			  if(j==c){
			  	for(j=0;j<c;j++)
			  	mat[i][j]=mat[i+1][j];
			  }
		  }
		  cout<<"Case #"<<tcc++<<": "<<endl;
		  for(i=0;i<r;i++){
		  	for(j=0;j<c;j++)
		  	cout<<mat[i][j];
		  	cout<<endl;
		  }
    	}
    return 0;
}
