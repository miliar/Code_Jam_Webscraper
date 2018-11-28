//
//  main.cpp
//  Problem
//
//  Created by Loc Ngo on 4/14/17.
//  Copyright © 2017 Loc Ngo. All rights reserved.
//

#include <iostream>
#include <fstream>
using namespace std;
ifstream fin("/Users/locngo/Desktop/A-small-attempt1.in");
int R,C;
char A[25][25];
char B[25][25];

bool check(char B[25][25],int c,int r1,int c1,int r2,int c2){
    for(int i=r1;i<=r2;i++)
        for(int j=c1;j<=c2;j++)
            if(B[i][j]!='?'&&B[i][j]!=c)
                return false;
    return true;
}

void fillArea(char B[25][25],int rc,int cc, char c,int i,int j){
    int rr1,rr2,cc1,cc2;
    int area = 0;
    for(int r1=0;r1<=rc;r1++)
        for(int c1=0;c1<=cc;c1++)
            for(int r2=rc;r2<R;r2++)
                for(int c2=cc;c2<C;c2++)
                    if(check(B,c,r1,c1,r2,c2)&&area<(r2-r1+1)*(c2-c1+1)){
                        area = (r2-r1+1)*(c2-c1+1);
                        rr1 = r1;
                        cc1 = c1;
                        rr2 = r2;
                        cc2 = c2;
                    }
    
    for(int i=rr1;i<=rr2;i++)
        for(int j=cc1;j<=cc2;j++)
            B[i][j] = c;
}

void process(int t){
    fin>>R>>C;
    
    for(int i=0;i<R;i++)
        for(int j=0;j<C;j++){
            fin>>A[i][j];
            B[i][j] = A[i][j];
        }
    for(int i=0;i<R;i++)
        for(int j=0;j<C;j++)
            if(A[i][j]!='?')
                fillArea(B,i,j,A[i][j],i,j);
    cout<<"Case #"<<t<<": \n";
    for(int i=0;i<R;i++){
        for(int j=0;j<C;j++)
            cout<<B[i][j];
        cout<<endl;
    }
}

int main(int argc, const char * argv[]) {
    // insert code here...
    int T;
    fin>>T;
    for(int i=1;i<=T;i++)
        process(i);
    return 0;
}
