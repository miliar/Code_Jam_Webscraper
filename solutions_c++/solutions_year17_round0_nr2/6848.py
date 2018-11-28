#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <iostream>

using namespace std;

//long long n;
char num[20];
/*
bool tidy()
{
    long long c=n;
    int a, b;

    b=c%10;  c/=10;
    while(c){
        a=c%10;  c/=10;
        if(a>b) return false;
        b=a;
    }
    return true;
}
*/
void solve()
{
    //scanf("%I64d", &n);
    //while(!tidy()) n--;
    //printf("%I64d\n", n);

    scanf("%s", num);
    int len=strlen(num);
    bool OK;
    for(int i=len-1;i>=0;i--){
        OK=true;
        for(int j=i-1;j>=0&&OK;j--){
            if(num[j]>num[i]){
                OK=false;
            }
        }
        if(!OK){
            num[i]='9';
            for(int j=i+1;j<len;j++){
                num[j]='9';
            }
            for(int j=i-1;j>=0;j--){
                if(num[j]=='0') num[j]='9';
                else{
                    num[j]--;
                    break;
                }
            }
        }
    }
    while(num[0]=='0'){
        for(int i=0;i<len;i++){
            num[i]=num[i+1];
        }
        len--;
    }
    printf("%s\n", num);
}

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t;  cin >> t;
    for(int i=1;i<=t;i++){
        printf("Case #%d: ", i);
        solve();
    }
    return 0;
}
