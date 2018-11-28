#include<iostream>
#include<fstream>
using namespace std;
void write(char ar[],char x,char y,char z,int X,int Y,int Z);
int main(){
    ifstream in("B-small-attempt0.in");
    ofstream out("out.txt");
    int t,n;
    int R,O,Y,G,B,V;
    in>>t;
    for(int it=0;it<t;it++){
        in>>n>>R>>O>>Y>>G>>B>>V;
        if((R<G) || (Y<V) || (B<O)){
            out<<"Case #"<<it+1<<": "<<"IMPOSSIBLE"<<endl;
            continue;
        }
        if((R==G && G && (Y || V || B || O)) || (Y==V && V && (R || G || B || O)) || (B==O && O && (Y || V || R || G))){
            out<<"Case #"<<it+1<<": "<<"IMPOSSIBLE"<<endl;
            continue;
        }
        R-=G;
        Y-=V;
        B-=O;
        if(R+Y<B || R+B<Y || B+Y<R){
            out<<"Case #"<<it+1<<": "<<"IMPOSSIBLE"<<endl;
            continue;
        }
        char ar[R+B+Y];
        if(Y>=B && Y>=R){
            write(ar,'Y','B','R',Y,B,R);
        }
        if(B>Y && B>=R){
            write(ar,'B','R','Y',B,R,Y);
        }
        if(R>Y && R>B){
            write(ar,'R','Y','B',R,Y,B);
        }
        out<<"Case #"<<it+1<<": ";
        bool startR=false,startB=false,startY=false;
        for(int I=0;I<R+B+Y;I++){
            if(ar[I]=='R' && !startR){
                for(int i=0;i<G;i++){
                    out<<"RG";
                }
                startR=true;
            }
            if(ar[I]=='Y' && !startY){
                for(int i=0;i<V;i++){
                    out<<"YV";
                }
                startY=true;
            }
            if(ar[I]=='B' && !startB){
                for(int i=0;i<O;i++){
                    out<<"BO";
                }
                startB=true;
            }
            out<<ar[I];
        }
        if(R+G+Y==0){
            for(int i=0;i<G;i++){
                out<<"RG";
            }
            for(int i=0;i<V;i++){
                out<<"YV";
            }
            for(int i=0;i<O;i++){
                out<<"BO";
            }
        }
        out<<endl;
    }
}
void write(char ar[],char x,char y,char z,int X,int Y,int Z){
    int len=Y+Z-X;
    int id=0;
    for(int i=0;i<len;i++){
        ar[id++]=x;
        ar[id++]=y;
        ar[id++]=z;
    }
    for(int i=0;i<Y-len;i++){
        ar[id++]=x;
        ar[id++]=y;
    }
    for(int i=0;i<Z-len;i++){
        ar[id++]=x;
        ar[id++]=z;
    }
}
