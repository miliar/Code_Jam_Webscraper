#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
#include <string>
using namespace std;
int T;
bool a[2000];
int main(){
    freopen("A-large.in","r",stdin);
    freopen("A.out","w",stdout);
    cin>>T;
    for(int t(1);t<=T;t++){
        string s;
        cin>>s;
        int n=s.length(),k,ans=0;
        for(int i(0);i<n;i++)
            a[i]=(s[i]=='+');
        cin>>k;
        bool flag=0;
        for(int i(0);i<n;i++)
            if(!a[i]){
                if(i+k-1>=n)flag=1;
                for(int j(i);j<i+k;j++)
                    a[j]=!a[j];
                ans++;
            }
        printf("Case #%d: ",t);
        if(flag)printf("IMPOSSIBLE\n");
        else printf("%d\n",ans);
    }
    return 0;
}