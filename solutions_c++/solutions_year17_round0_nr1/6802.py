#include<bits/stdc++.h>
using namespace std;


int main(){

    int t,i,j,l,c,k,m;
    bool pos;
    char word[10000];
    scanf("%d",&t);
    for(i=0;i<t;i++){
        pos = true;
        getchar();
        scanf("%s",word);
        scanf("%d",&k);
        l = strlen(word);
        c = 0;
        for(j=0;j<l;j++){
            if(word[j]=='-'){
                if( j+k-1 < l ){
                    for( m=j;m<=(k+j-1);m++ ){
                        if( m>=l ){
                            break;
                        }
                        if( word[m]=='-' )
                            word[m]='+';
                        else
                            word[m] = '-';

                    }
                    c++;
                }

            }
        }
        for(j=0;j<l;j++){
            if( word[j]=='-' ){
                pos = false;
                break;
            }
        }
        printf("Case #%d: ",i+1);
        if( !pos )
            printf("IMPOSSIBLE\n");
        else{
            printf("%d\n",c);
        }
    }


    return 0;
}
