#include<bits/stdc++.h>
using namespace std;
vector<string> mat(30),auxv;
int h,w,tc;
bitset<500> bs;
bool posibleI(int a,int b,int y){
    if(y==0) return false;
    for(int i=a; i<=b; i++)
        if(mat[i][y-1]!='?') return false;
    return true;
}
bool posibleD(int a,int b,int y){
    if(y==w-1) return false;
    for(int i=a; i<=b; i++){
        if(mat[i][y+1]!='?') return false;
    }
    return true;
}
bool hasQ(){
    for(int i=0; i<h; i++){
        for(int j=0; j<w; j++){
            if(mat[i][j]=='?') return true;
        }
    }
    return false;
}
void expI(int a,int b,int y,char c){
    for(int i=a; i<=b; i++)
        mat[i][y-1]=c;
}
void expD(int a,int b,int y,char c){
    for(int i=a; i<=b; i++)
        mat[i][y+1]=c;
}
int main(){
    char aux;
    int chg;
    cin>>tc;
    for(int t=1; t<=tc; t++){
        chg=0;
        bs.reset();
        cin>>h>>w;
        for(int i=0; i<h; i++)
            cin>>mat[i];
        auxv=mat;
        for(int y=0; y<h; y++){
            for (int x=0; x<w; x++){
                if(mat[y][x]!='?'&&!bs[mat[y][x]]){
                    aux=mat[y][x];
                    bs[mat[y][x]]=1;
                    int i=y-1,top,bot;
                    while(i>=0&&mat[i][x]=='?'){mat[i--][x]=aux; chg++;}
                    top=i+1;
                    i=y+1;
                    while(i<h&&mat[i][x]=='?'){mat[i++][x]=aux; chg++;}
                    bot=i-1;
                    i=x;
                    while(posibleI(top,bot,i)){
                        expI(top,bot,i,aux);
                        chg+=bot-top+1;
                        i--;
                    }
                    i=x;
                    while(posibleD(top,bot,i)){
                        chg+=bot-top+1;
                        expD(top,bot,i,aux);
                        i++;
                    }
                }
            }
        }
        if(hasQ()){
        bs.reset();
        mat=auxv;
        for(int y=h-1; y>=0; y--){
            for (int x=w-1; x>=0; x--){
                if(mat[y][x]!='?'&&!bs[mat[y][x]]){
                    aux=mat[y][x];
                    bs[mat[y][x]]=1;
                    int i=y-1,top,bot;
                    while(i>=0&&mat[i][x]=='?'){mat[i--][x]=aux; chg++;}
                    top=i+1;
                    i=y+1;
                    while(i<h&&mat[i][x]=='?'){mat[i++][x]=aux; chg++;}
                    bot=i-1;
                    i=x;
                    while(posibleI(top,bot,i)){
                        expI(top,bot,i,aux);
                        chg+=bot-top+1;
                        i--;
                    }
                    i=x;
                    while(posibleD(top,bot,i)){
                        chg+=bot-top+1;
                        expD(top,bot,i,aux);
                        i++;
                    }
                }
            }
        }}
        cout<<"Case #"<<t<<":"<<endl;
        for(int i=0; i<h; i++)
            cout<<mat[i]<<endl;
    }
}
