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
        char grid[r][c];
        for(int i=0;i<r;i++){
            for(int j=0;j<c;j++){
                cin>>grid[i][j];
            }
        }
        for(int i=0;i<r;i++){
            for(int k=0;k<c;k++){
                if(grid[i][k]!='?'){
                    for(int m=0;m<k;m++){
                        grid[i][m]=grid[i][k];
                    }
                    flag=1;
                    break;
                }
                flag=0;
            }
            for(int j=0;j<c;j++){
                if(flag!=0){
                    if(grid[i][j]=='?'){
                            if(j-1>=0)
                                grid[i][j]=grid[i][j-1];
                    }
                }else{
                    if(grid[i][j]=='?' && i-1>=0){
                        grid[i][j]=grid[i-1][j];
                    }
                }
            }
        }
        for(int i=r-1;i>=0;i--){
            for(int j=c-1;j>=0;j--){
                if(grid[i][j]=='?' && i+1<r){
                    grid[i][j]=grid[i+1][j];
                }
            }
        }
        cout<<"Case #"<<q<<":"<<endl;
        for(int i=0;i<r;i++)
        {
            for(int j=0;j<c;j++){
                cout<<grid[i][j];
            }
            cout<<endl;
        }
    q++;
    }
    return 0;
}
