#include<iostream>
#include<string>

using namespace std;

char let;

int main(){
    int t,r,c,q=1;
    cin>>t;
    while(t--){
        cin>>r>>c;
        
        int flag=1;
        char board[r][c];
        
		for(int i=0;i<r;i++){
            for(int j=0;j<c;j++){
                cin>>board[i][j];
            }
        }
        
		for(int i=0;i<r;i++){
            for(int k=0;k<c;k++){
                if(board[i][k]!='?'){
                    for(int m=0;m<k;m++){
                        board[i][m]=board[i][k];
                    }
                    flag=1;
                    break;
                }
                flag=0;
            }
        
		    for(int j=0;j<c;j++){
                if(flag!=0){
                    if(board[i][j]=='?'){
                            if(j-1>=0)
                                board[i][j]=board[i][j-1];
                    }
                }else{
                    if(board[i][j]=='?' && i-1>=0){
                        board[i][j]=board[i-1][j];
                    }
                }
            }
        }
        
		for(int i=r-1;i>=0;i--){
            for(int j=c-1;j>=0;j--){
                if(board[i][j]=='?' && i+1<r){
                    board[i][j]=board[i+1][j];
                }
            }
        }
        
		cout<<"Case #"<<q<<":"<<endl;
        
		for(int i=0;i<r;i++)
        {
            for(int j=0;j<c;j++){
                cout<<board[i][j];
            }
            cout<<endl;
        }
    q++;
    }
    return 0;
}

