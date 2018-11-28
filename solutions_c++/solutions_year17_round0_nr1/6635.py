
#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;

int tc; int k;
char str[1111];

char change(char c){
    if ( c== '-') return '+';
    else return '-';
}

int main(){
    freopen("output.txt","w",stdout);
    cin >>tc;
    for (int tcc =1; tcc<= tc ;tcc++){
        cin >> str;
        scanf("%d",&k);
        int cnt = 0 ;
        for (int i =0 ; i<=strlen(str)-k; i++ ){
            if ( str[i] == '-'){
                cnt ++ ;
                for (int j= 0; j<=k-1; j++){
                    str[i+j]= change(str[i+j]);
                }
            }
        }
        bool flag = false;
        for (int i = (int)strlen(str)-1 ; strlen(str)-k < i ;i-- ){
            if ( str[i] =='-'){
                flag= true;
            }
        }
        
        printf("Case #%d: ",tcc);
        if ( flag ) cout<<"IMPOSSIBLE"<<endl;
        else  cout<<cnt<<endl;
    }
    
}