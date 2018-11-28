#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <string.h>
#include <map>
using namespace std;
typedef long long ll;

char arr[30][30];

bool full(int r, int c){
    for(int i = 0 ; i < r ; i++){
        for(int j = 0 ; j < c ; j++){
            if(arr[i][j]=='?') return false;
        }
    }
    return true;
}

void p(int r,int c){
    for(int i = 0 ; i < r ; i++){
        for(int j = 0 ; j < c ; j++){
            printf("%c",arr[i][j]);
        }
        puts("");
    }
}

void process(){
    int r,c;
    scanf("%d %d",&r,&c);
    for(int i = 0 ; i < r ; i++){
        for(int j = 0 ; j < c ; j++){
            scanf(" %c",&arr[i][j]);
        }
    }
    for(int i = 0 ; i < r ; i ++){
        for(int j = 0 ; j < c ; j++){
            if(arr[i][j]!='?'){
                int up = i-1, down = i+1;
                while(up>=0&&arr[up][j]=='?'){
                    arr[up][j] = arr[i][j];
                    up--;
                }
                while(down<r&&arr[down][j]=='?'){
                    arr[down][j] = arr[i][j];
                    down++;
                }
            }
        }
    }
    //p(r,c);
    while(!full(r,c)){
        for(int i = 0 ; i < r ; i ++){
            for(int j = 0 ; j < c ; j++){
                if(arr[i][j]=='?'){
                  if(j==c-1){
                      arr[i][j] = arr[i][j-1];
                  }
                  else if(j==0){
                        arr[i][j] = arr[i][j+1];
                  }
                  else if(arr[i][j+1]!='?'){
                      arr[i][j] = arr[i][j+1];
                  }
                  else{
                      arr[i][j] = arr[i][j-1];
                  }
                }
            }

        }
    }
    p(r,c);
}

int main(){
    //freopen("Ginput.txt","rt",stdin);
    //freopen("output.txt","wt",stdout);
    int t;
    scanf("%d",&t);
    for(int i = 1 ; i <= t ; i++){
        printf("Case #%d:\n",i);
        process();
    }
}
