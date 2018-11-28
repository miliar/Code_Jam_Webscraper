#include <iostream>
#include <stdio.h>
#include <fstream>

using namespace std;

char cake[30][30];
ofstream ifile("large.txt");

void solve(int r,int c,int tt){

char fchar[r];
int i,j;
for(i=0;i<r;i++){
    for(j=0;j<c&&cake[i][j]=='?';j++){}
    if(j==c) fchar[i]='1';
    else {fchar[i]=cake[i][j];

    for(j=0;j<c&&cake[i][j]=='?';j++){cake[i][j]=fchar[i];}

    }

}
i=0;
while(fchar[i]=='1'){i++;}
int temp=i-1;
for(;i<r;i++){
    if(fchar[i]=='1'){
        for(j=0;j<c;j++){

            cake[i][j]=cake[i-1][j];

        }
        continue;
    }

    for(j=0;j<c;j++){
        if(cake[i][j]=='?')
            cake[i][j]=cake[i][j-1];

    }



}
if(temp>=0){
    for(;temp>=0;temp--){
        for(j=0;j<c;j++){

            cake[temp][j]=cake[temp+1][j];

        }


    }



}

ifile << "Case #" << tt << ":" <<endl;

for(i=0;i<r;i++){

    ifile<<cake[i] << endl;


}



return ;

}

int main(){
int t,tt;
ifstream myfile("sample.txt");

myfile >> t;

for(tt=1;tt<=t;tt++){
    int r,c;
    myfile >> r >>c;
    for(int i=0;i<r;i++){
            myfile >>cake[i];
    }
    solve(r,c,tt);



}




}
