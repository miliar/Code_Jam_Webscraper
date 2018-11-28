#include <bits/stdc++.h>
using namespace std;

char grid[50][50];
int r,c;
map<char,bool> used;

bool canplace(int i,int j,char letter){
    return grid[i][j]=='?'||grid[i][j]==letter;
}

void ssolve(int row,int col,char letter){
    int i,j,k,p;
    for (i=col-1;i>=0;i--){
        if (canplace(row,i,letter))grid[row][i]=letter;
        else break;
    }for (j=col+1;j<c;j++){
        if (canplace(row,j,letter))grid[row][j]=letter;
        else break;
    }
    i++,j--;
    for (k=row+1;k<r;k++){

        for (p=i;p<=j;p++){
            if (!canplace(k,p,letter))break;
        }
        if (p!=j+1)break;
        for (p=i;p<=j;p++){
            grid[k][p]=letter;
        }
    }
    for (k=row-1;k>=0;k--){

        for (p=i;p<=j;p++){
            if (!canplace(k,p,letter))break;
        }
        if (p!=j+1)break;
        for (p=i;p<=j;p++){
            grid[k][p]=letter;
        }
    }
}

int main(){
    int t;

    cin>>t;
    for (int n=1;n<=t;n++){
        cin>>r>>c;
        used.clear();
        for (int i=0;i<r;i++)cin>>grid[i];
        for (int i=0;i<r;i++){
            for (int j=0;j<c;j++){
                if (grid[i][j]!='?'&&!used[grid[i][j]])ssolve(i,j,grid[i][j]);
                used[grid[i][j]]=true;
            }
        }
        cout<<"Case #"<<n<<":\n";
        for (int i=0;i<r;i++){
            for (int j=0;j<c;j++)cout<<grid[i][j];
            cout<<endl;
        }
    }
}
