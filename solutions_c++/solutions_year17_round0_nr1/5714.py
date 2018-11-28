#include<cstdio>
#include<string>
#include<iostream>
#include<algorithm>
#include<cstring>
#include<queue>
#include<vector>
#include<deque>
using namespace std;

int T;
int main(){
    freopen("A-large.in","r",stdin);
    freopen("outputA.txt","w",stdout);
    scanf("%d",&T);
    for(int j=1;j<=T;j++){
        string s;
        bool flag=false;
        int cnt=0;
        int A;
        cin >> s;
        scanf("%d",&A);
        for(int i=0;i<=s.size()-A;i++){
            if(s[i]=='-'){
                cnt++;
                for(int k=i;k<i+A;k++){
                    if(s[k]=='-')
                        s[k]='+';
                    else
                        s[k]='-';
                }
            }
        }
        for(int i=0;i<s.size();i++){
            if(s[i]=='-'){
                flag=true;
                break;
            }
        }
        printf("Case #%d: ",j);
        if(flag)
            puts("IMPOSSIBLE");
        else
            printf("%d\n",cnt);
    }
    return 0;
}

