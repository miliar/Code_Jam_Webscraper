#include <bits/stdc++.h>
using namespace std;
char ar[30][30];
void fillSides(char ch,int r,int c,int row,int col){
    int i=c-1,j=c+1;
    while(j<col){
        if(ar[r][j]=='?'){
            ar[r][j]=ch;
        }
        else{
            break;
        }
        j++;
    }
    while(i>=0){
        if(ar[r][i]=='?'){
            ar[r][i]=ch;
        }
        else{
            break;
        }
        i--;
    }
}
void fillUp(char ch,int r,int c,int row,int col){
    int i=r-1,j=r+1;
    while(i>=0){
        if(ar[i][c]=='?'){
            ar[i][c]=ch;
        }
        else{
            break;
        }
        i--;
    }
    while(j<row){
        if(ar[j][c]=='?'){
            ar[j][c]=ch;
        }
        else{
            break;
        }
        j++;
    }
}
int main(){
    freopen("A-large.in","r",stdin);
    freopen("problem_ALarge.out","w",stdout);
    int t,tc,r,c,i,j;
    cin>>t;
    for(tc=1;tc<=t;tc++){
        cin>>r>>c;
        for(i=0;i<r;i++){
            for(j=0;j<c;j++){
                cin>>ar[i][j];
            }
        }
        for(i=0;i<r;i++){
            for(j=0;j<c;j++){
                if(ar[i][j]!='?'){
                    fillUp(ar[i][j],i,j,r,c);
                }
            }
        }
        for(i=0;i<r;i++){
            for(j=0;j<c;j++){
                if(ar[i][j]!='?'){
                    fillSides(ar[i][j],i,j,r,c);
                }
            }
        }
        cout<<"Case #"<<tc<<":\n";
        for(i=0;i<r;i++){
            for(j=0;j<c;j++){
                cout<<ar[i][j];
            }
            cout<<"\n";
        }
    }
return 0;
}
