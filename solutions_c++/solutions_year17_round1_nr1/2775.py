#include<bits/stdc++.h>
using namespace std;

int main(){

    int t,r,c,i,j,I,J;
    scanf("%d",&t);
    int cases=1;
    while(cases<=t){
        scanf("%d",&r);
        scanf("%d",&c);
        string cake[r];
        int count=0;
        for(i=0;i<r;i++){
            cin>>cake[i];
            for(j=0;j<cake[i].size();j++){
                if(cake[i][j]=='?')
                    count++;
            }
        }
        if(count==0){

        }
        else{
            for(i=0;i<r;i++){
                for(j=0;j<c;j++){

                   if(cake[i][j]!='?'){

                        I=i;
                        J=j-1;

                        while(J>=0 && cake[I][J]=='?'){
                            cake[I][J]=cake[i][j];
                            J--;
                        }
                        I=i;
                        J=j+1;
                        while(J<c && cake[I][J]=='?'){
                            cake[I][J]=cake[i][j];
                            J++;
                        }

                    }
                }
            }

        for(i=0;i<r;i++){
            for(j=0;j<c;j++){

                if(cake[i][j]!='?'){
                    I=i;J=j;
                    while( I+1<r && cake[I+1][J]=='?'){
                        cake[I+1]=cake[I];
                        I++;
                    }
                    I=i;J=j;
                    while( I-1>=0 && cake[I-1][J]=='?'){
                        cake[I-1]=cake[I];
                        I--;
                    }


                }
            }
        }



    }
    cout<<"Case #"<<cases<<":"<<"\n";
            for(i=0;i<r;i++){
                cout<<cake[i]<<"\n";
            }
    cases++;

    }
}
