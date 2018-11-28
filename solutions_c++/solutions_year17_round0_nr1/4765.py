#include<stdio.h>
#include<math.h>
#include<vector>
#include<algorithm>
#include<map>
#include<unordered_map>
#include<iostream>
#include<string>
#define ll long long
#define fi first
#define se second
using namespace std;
int main(void){
    freopen("A-large.in","r",stdin);
    //freopen("A-large.out", "w", stdout);
    int T;
    scanf("%i", &T);
    for(int l=0;l<T;l++){
        string s;
        cin >> s;
        int K;
        scanf("%i", &K);
        int res=0;
        int N=s.size();
        int i;
        for(i=0;i<N;i++){
            while(i<N&&s[i]=='+') i++;
            if(i==N) break;
            if(i<=N-K){
                for(int j=i;j<i+K;j++){
                    s[j]='+'+'-'-s[j];
                }
                res++;
            }
            else {res=-1; break;}
        }
        printf("Case #%i: ", l+1);
        if(res==-1) printf("IMPOSSIBLE\n");
        else printf("%i\n", res);
    }
    return 0;
}

