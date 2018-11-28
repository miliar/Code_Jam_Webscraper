//in the name of allah
#include<bits/stdc++.h>
using namespace std;
const int N=1e3+10;
int a[N];
char s[N];
void solve(){
        int n , k;        
        scanf("%s%d" , s , &k);
        n = strlen(s);
        memset(a , 0 , sizeof a);
        int ret=0;
        bool sum = false;
        for(int i=0 ; i<n ; i++){
                for(int j=0 ; j<a[i] ; j++)
                        sum ^= 1;
                bool cur = (s[i] == '+');
                cur ^= sum;
                if(!cur){
                        if(i+k>n){
                                puts("IMPOSSIBLE");                       
                                return;
                        }
                        a[i+k] ++;
                        sum ^= 1;
                        ret ++;
                }
        }
        printf("%d\n" , ret);
}

int main(){
        int t , it=0;
        scanf("%d" , &t);
        while(++it <= t){
                printf("Case #%d: " , it);
                solve();
        }
        return 0;
}
