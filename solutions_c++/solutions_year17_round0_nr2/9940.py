#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <string>
using namespace std;
int main(){
    int l,t,p;
    string a;
        scanf("%d",&t);
        for( int i = 1 ; i <= t ; i++ ){
            cin>>a;
            p = -1;
            for( int j = 1, b = 0 ; j < a.length() ; j++ ){
                if( b == 1 )
                    a[j] = '9';
                else
                    if( a[j] < a[j-1] ){
                        if( b == 0 )
                            p = j;
                        b = 1;
                    }
            }
            for( int j = p ; j > 0 ; j-- ){
                if( a[j] < a[j-1] ){
                    a[j] = '9';
                    if( a[j-1] == '0' )
                        a[j-1] = '9';
                    else
                        a[j-1]--;
                }
            }

            printf("Case #%d: ",i);
            for( int j=0,b=0;j<a.length();j++ ){
                if( b == 1 ){
                    printf("%c",a[j]);
                }
                else{
                    if( a[j] != '0' ){
                        printf("%c",a[j]);
                        b=1;
                    }
                }
            }
            printf("\n");
        }
    return 0;
}
