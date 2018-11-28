#include<iostream>
#include<fstream>
#include<vector>
#include<bits/stdc++.h>
#define ll long long int
using namespace std;
/*void row(char c[][30],int r,int c,int row,int col,char e){
    int i=0,j;
    while(i<c && (c[r][i] == '?' || c[r][i] == e)){
        c[r][i] = e;
        i++;
    }
    i=c+1;
    while(i<col && (c[r][i] == '?' || c[r][i] == e)){
        c[r][i] = e;
        i++;
    }
}*/
int safe(int r,int c,int row,int col){
    if(r>=0 && r<row && c>=0 && c<col)
    return 1;
    return 0;
}
/*void col(char c[][30],int r,int c,int row,int col,char e){
    int i=0,j;
    while(i<c && (c[r][i] == '?' || c[r][i] == e)){
        c[r][i] = e;
        i++;
    }
    i=c+1;
    while(i<col && (c[r][i] == '?' || c[r][i] == e)){
        c[r][i] = e;
        i++;
    }
}*/
void get(char c[][30],int vis[],int row,int col,ofstream &op){
    int i,j,k;
        int f=0;
        while(1)
        {
            int flag=0;
            for(i=0;i<row;i++){
            f=0;
            for(j=0;j<col;j++){
                if(c[i][j] == '?')
                flag = 1;
                if(c[i][j] != '?'){
                    f=1;
                    for(k=j-1;k>=0;k--){
                        if(c[i][k] != '?')
                        break;
                        c[i][k]=c[i][j];
                    }
                    for(k=j+1;k<col;k++){
                        if(c[i][k] != '?')
                        break;
                        c[i][k]=c[i][j];
                    }
                }
            }
            if(f == 0){
                int s=0;
                if(i!=row-1){
                    for(j=0;j<col;j++){
                        if(c[i+1][j] != '?')
                        s=1;
                        c[i][j] = c[i+1][j];
                    }
                    if(s == 0){
                        if(i != 0){
                            for(j=0;j<col;j++){
                                c[i][j] = c[i-1][j];
                            }
                        }
                    }
                }
                else if(i == row-1){
                    for(j=0;j<col;j++){
                        if(c[i-1][j] != '?')
                        s=1;
                        c[i][j] = c[i-1][j];
                    }
                }
            }
        }
            if(flag == 0)
            break;
        }
        for(i=0;i<row;i++){
            for(j=0;j<col;j++){
                op<<c[i][j];
            }
            op<<endl;
        }
}
int main(){
    int t,i,n,j,row,col,k;
    char c[30][30];
    ifstream ip;
    ofstream op;
    ip.open("A-large.in");
    op.open("op.txt");
    ip>>t;
    for(i=1;i<=t;i++){
        int vis[27]={0};
        ip>>row>>col;
        for(j=0;j<row;j++){
            for(k=0;k<col;k++){
                ip>>c[j][k];
            }
        }
        //cout<<i<<endl;
        op<<"Case #"<<i<<": "<<endl;
        get(c,vis,row,col,op);
    }
    return 0;
}
