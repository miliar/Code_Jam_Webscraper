#include <iostream>
#include <map>
#include <stack>
#include <set>
#include <bits/stdc++.h>
#include <stdio.h>

using namespace std;

int T;
int R,Y,B,O,G,V,N;
char ans[1024];

char last_char='F';
typedef struct {
                int cnt; char c;
            } str_t;
            str_t arr[3];

int cmpfunc (const void * a, const void * b)
{
    int r= ( ((str_t*)a)->cnt - ((str_t*)b)->cnt );
    //fprintf(stderr," %c#%c ",last_char,((str_t*)a)->c);
    if(last_char==((str_t*)a)->c)  return -1;
    if(last_char==((str_t*)b)->c)  return 1;
    if(r==0) {

    }
   return r;
}

void solve(){
    if(O==0 && G==0 && V==0){
        int valid = (N)/2;
        int total = R+Y+B;
        if( (R > valid || Y>valid || B > valid))
           {
            sprintf(ans,"%s","IMPOSSIBLE");
        }else{

            arr[0] = {R, 'R'};
            arr[1] = {Y, 'Y'};
            arr[2] = {B, 'B'};
            sprintf(ans,"");
            while(arr[0].cnt || arr[1].cnt || arr[2].cnt){
                    qsort(arr,3,sizeof(str_t), cmpfunc);
                    for(int i=0;i<=2;i++){
                    //    printf(" %d %c ",arr[i].cnt, arr[i].c);
                    }
                   // printf("\n");
                arr[2].cnt--;
                last_char = arr[2].c;
                    sprintf(ans,"%s%c",ans,arr[2].c);
                }
        }
    }else{
        sprintf(ans,"%s","IMPOSSIBLE");
    }
    if(ans[0]==ans[N-1]){
        char c = ans[N-1];
        ans[N-1] = ans[N-2];
        ans[N-2] = c;
    }
}



int main(){

#if 1
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
#endif

    cin>>T;
    for(int t=0; t<T; t++){
        cin>>N>>R>>O>>Y>>G>>B>>V;
        solve();

        printf("Case #%d: %s\n", t+1, ans);
    }
    return 0;
}

