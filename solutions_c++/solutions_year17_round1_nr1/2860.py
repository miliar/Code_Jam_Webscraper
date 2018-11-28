#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main(){
    int t,count=1;
    cin>>t;
    while(t--){
        int r,c;
        cin>>r>>c;
        char s[r][c];
        for(int i=0;i<r;i++)
            cin>>s[i];
        for(int i=0;i<r;i++){
            for(int j=0;j<c;j++){
                if(s[i][j]!='?'){
                    char x=s[i][j];
                    char y=x;
                    for(int k=i+1;k<r;k++){
                        if(s[k][j]=='?')
                            s[k][j]=y;
                        else
                            y=s[k][j];
                    }
                    y=x;
                    for(int k=i-1;k>=0;k--){
                        if(s[k][j]=='?')
                            s[k][j]=y;
                        else
                            y=s[k][j];
                    }
                }
            }
        }
        for(int i=0;i<r;i++){
            for(int j=0;j<c;j++){
                if(s[i][j]!='?'){
                    char x=s[i][j];
                    char y=x;
                    for(int k=j+1;k<c;k++){
                        if(s[i][k]=='?')
                            s[i][k]=y;
                        else
                            y=s[i][k];
                    }
                    y=x;
                    for(int k=j-1;k>=0;k--){
                        if(s[i][k]=='?')
                            s[i][k]=y;
                        else
                            y=s[i][k];
                    }
                }
            }
        }
        cout<<"Case #"<<count++<<":"<<endl;
        for(int i=0;i<r;i++)
           { for(int j=0;j<c;j++)
                cout<<s[i][j];
            cout<<endl;
           }
    }
}