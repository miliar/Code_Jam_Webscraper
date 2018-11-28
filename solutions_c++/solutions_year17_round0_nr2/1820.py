#include<iostream>
#include<string>
#include<queue>
#include<cstring>
#include<vector>
#include<set>
#include<map>
#include<cstdio>
#include<cmath>
#include<algorithm>
using namespace std;
int data[50];
int main(){

    string str;
    int testcase,k,i,j,r,counter,flag;
    //freopen("input.txt","r",stdin);
    //freopen("output.txt","w",stdout);
    scanf("%d",&testcase);
    for( int t = 1; t <= testcase; t++ ){
        cin>>str;
        r = str.size();
        for( i = 0; i < str.size() ; i++ ){
            data[i+1] = str[i]-'0';
        }
        for( i = 2; i <= r; i++ ){
            if( data[i] < data[i-1]){
                data[i-1]--;
                for( j = i-1; j >= 1; j-- ){
                    if( data[j] >= data[j-1]){
                        for( k = j+1; k <= r; k++ ){
                            data[k] = 9;
                        }
                        if( j == 1 ){
                            if( data[j] == 0 ){
                                data[j] = 9;
                                r--;
                            }
                        }
                        break;
                    }
                    else{
                        data[j-1]--;
                    }
                }
                break;
            }
        }
        printf("Case #%d: ",t);
        for( i = 1; i <= r; i++ ){
            printf("%d",data[i]);
        }
        printf("\n");
    }


return 0;
}
