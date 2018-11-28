//Mitesh Agrawal
#include <bits/stdc++.h>
using namespace std;

string s[30];
int r,c;

int valid(int a, int b){
    return (0<=a && a<r && 0<=b && b<c);
}

bool space(){
    int i,j;
    for(i=0;i<r;i++)
        for(j=0;j<c;j++)
            if(s[i][j]=='?')
                return true;
    return false;
}

void fill(){
    int i,j;
    for(i=0;i<r;i++)
        for(j=0;j<c;j++)
            if(s[i][j]=='?'){
                if(valid(i+1,j) && s[i+1][j]!='?')
                    s[i][j] = s[i+1][j];
                else if(valid(i-1,j) && s[i-1][j]!='?')
                    s[i][j] = s[i-1][j];
            }

}

void fill1(){
    int i,j;
    for(i=0;i<r;i++)
        for(j=0;j<c;j++)
            if(s[i][j]=='?'){
                if(valid(i,j+1) && s[i][j+1]!='?')
                    s[i][j] = s[i][j+1];
                else if(valid(i,j-1) && s[i][j-1]!='?')
                    s[i][j] = s[i][j-1];
            }

}

int main(){
    freopen ("A-large.in","r",stdin); 
    freopen ("A-large.out","w",stdout); 
    int i,j,t,test;
    scanf("%d",&t);
    for(test=1;test<=t;test++){
        scanf("%d %d",&r,&c);
        for(i=0;i<r;i++){
            cin>>s[i];
        }
        for(i=0;i<1000;i++){
            fill();
        }
        for(i=0;i<1000;i++){
            fill1();
        }
        printf("Case #%d:\n",test);
        for(i=0;i<r;i++)
            cout<<s[i]<<endl;
    }


    return 0;
}