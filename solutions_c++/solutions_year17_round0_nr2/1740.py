#include <cstdio>
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <map>
#include <set>
#define fi first
#define se second
using namespace std;
typedef long long LL;
const int MOD = 1e9+7;
const int maxn = 1e3+10;

int main() {
    int T;
    cin>>T;
    int k;
    int kase =0;
    char ans[20];
    while(T--){
        string s;
        cin>>s;

        int times = 20;
        while (times--) {
            bool flag= false;
            for( int i=1 ; i<s.size() ; ++i)
                if(!flag){
                    if(s[i]<s[i-1]){
                        s[i-1]--;
                        s[i] = '9';
                        flag = true;
                    }
                }else{
                    s[i] = '9';
                }
        }
        printf("Case #%d: ",++kase);
        if(s[0]=='0'){
            for(int i=1;  i<s.size();++i)
                printf("%c",s[i] );
        }else for(int i=0 ; i<s.size() ; ++i)
            printf("%c",s[i] );
        printf("\n" );

    }

  return 0;
}
