
#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;

int tc;
char str[33];

int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    cin >>tc;
    for (int tcc =1; tcc<= tc ;tcc++){
        char str2[33];
        cin >> str;
        int len = (int)strlen(str);//사이즈만큼
        strcpy(str2, str);
        bool changed= true ;
        while (changed){
            changed = false ;
            for (int i = len-1 ; i> 0 ;i--){
                if  ( str[i-1] <= str[i] ){ // 오름차순 --> 그대로
                    
                }else {
                    str[i] = '9';
                    if ( str2[i-1] >= str[i-1] )
                    str[i-1] -= 1; //한자리 낮춰주기 0이 절대 못옴..
                    changed = true ;
                }
            }
            if ( str[0] == '0') { //댕기기
                for (int i =0 ;i< strlen(str) ;i++){
                    str[i] = str[i+1];
                    
                }
                len --;
            }
        }
        printf("Case #%d: ",tcc);
        printf("%s\n",str);
    }
}