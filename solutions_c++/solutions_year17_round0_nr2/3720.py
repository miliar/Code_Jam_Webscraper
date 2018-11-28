//in the name of allah
#include<bits/stdc++.h>
using namespace std;
const int N=20;
char s[N] , o[N];
bool cmp(char *a , char *b , int n){
        for(int i=0 ; i<n ; i++)
                if(a[i] != b[i])
                        return (a[i] < b[i]);
        return true;                
}
void solve(){
        scanf("%s" , s);
        int n = strlen(s);
        for(int i=0 ; i<n ; i++){
                int j=0;
                for( ; j<10 ; j++){
                        for(int k=i ; k<n ; k++)
                                o[k] = char('0'+j);
                        if(!cmp(o , s , n))
                                break;
                }
                j--;
                o[i] = char('0'+j);
        }
        int st = (o[0] == '0');
        for(int i=st ; i<n ; i++)
                printf("%c" , o[i]);
        puts("");
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
