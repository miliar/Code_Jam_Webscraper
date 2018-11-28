#include<bits/stdc++.h>
using namespace std;
#define inc(i,x) for(int i=0;i<x;i++)
#define onc(i,x) for(int i=1;i<=x;i++)
int r,c;
char cake[30][30];
void print()
{
    inc(i,r){
        cout<<cake[i]<<'\n';
    }
}
main()
{
    int t;
    cin>>t;
    onc(kase,t){
        cin>>r>>c;
        inc(i,r){
            cin>>cake[i];
        }

        ///label#1
        inc(i,r){
            int cut=0;
            inc(j,c){
                if(cake[i][j]!='?'){
                    for(int k=cut;k<j;k++){
                        cake[i][k]=cake[i][j];
                    }
                    cut=j+1;
                }
            }
        }

        ///label#2
        inc(i,r){
            char hold=cake[i][0];
            inc(j,c){
                if(cake[i][j]=='?'){
                    cake[i][j]=hold;
                }
                else{
                    hold=cake[i][j];
                }
            }
        }

        ///label#3 top
        inc(j,c){
            char hold='?';
            for(int i=r-1;i>=0;i--){
                if(cake[i][j]=='?'){
                    cake[i][j]=hold;
                }
                else{
                    hold=cake[i][j];
                }
            }
        }

        ///label#4 down
        inc(j,c){
            char hold='?';
            for(int i=0;i<r;i++){
                if(cake[i][j]=='?'){
                    cake[i][j]=hold;
                }
                else{
                    hold=cake[i][j];
                }
            }
        }



        cout<<"Case #"<<kase<<":\n";
        print();
    }
}
