#include <bits/stdc++.h>
using namespace std;
#define ll long long

int a[1005];
int main(){
    freopen("A-large.in", "r", stdin);
    freopen("out2017.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for(int K=1; K<=t; K++){
        string s;
        cin>>s;
        int k;
        cin>>k;
        for(int i=0; i<s.size(); i++){
            if(s[i]=='-')
                a[i]=0;
            else
                a[i]=1;
        }
        int ans=0;
        for(int i=0; i<s.size()-k+1; i++){
            if(a[i]==0){
                ans++;
                for(int j=0; j<k; j++){
                    a[i+j] = !a[i+j];
                }
            }
        }
        int flag=1;
        for(int i=0; i<s.size(); i++){
            if(a[i]==0)
                flag=0;
        }
        if(flag)
            printf("Case #%d: %d\n", K, ans);
        else
            printf("Case #%d: IMPOSSIBLE\n", K);
    }
    return 0;
}
