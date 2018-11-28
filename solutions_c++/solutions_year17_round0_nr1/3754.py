#include<cstring>
#include<cstdio>
#include<string>
#include<iostream>
using namespace std;

string s;
int ans,k,len;

void print() {
    for(int i=len-k+1;i<len;++i) {
        if(s[i]=='-') {
            puts("IMPOSSIBLE");
            return ;
        }
    }
    printf("%d\n",ans);
}

int main() {
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T;scanf("%d",&T);
    int ca=0;
    while(T--) {
        printf("Case #%d: ",++ca);
        cin>>s;
        scanf("%d",&k);
        len=s.length();
        ans=0;

        for(int i=0;i<len-k+1;++i) {
            if(s[i]=='-') {
                for(int j=0;j<k;++j) {
                    s[i+j]=(s[i+j]=='+')?'-':'+';
                }
                ++ans;
            }
        }

        print();

    }
    return 0;
}
