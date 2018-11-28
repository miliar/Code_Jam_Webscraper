#include <stdio.h>
#include <iostream>
#include <string>
#include <algorithm>
#include <stdlib.h>
#include <map>
#include <assert.h>
#include <vector>
#include <complex>
#include <string.h>
//#include <tr1/unordered_map>
using namespace std;

int s[10];
int a[10] , fi[10];
char id[20] = {'R', 'O', 'Y', 'G', 'B', 'V'};
vector<int>ans,tmp;

int main(){
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int T,CASE=0;
    scanf("%d",&T);
    while(T--){
        int n;
        scanf("%d",&n);
        for(int i=0;i<6;i++){
            scanf("%d",&s[i]);
//            cout<<s[i]<<endl;
            if( i % 2 == 0 )
                a[i>>1] = s[i];
        }
        bool flag = true;
        for(int i=0;i<3;i++){
            a[i] -= s[(i*2+3)%6];
            if( s[(i*2+3)%6] && a[i] <= 0 )
                flag = 0;
            if(s[(i*2+3)%6]) fi[i] = 1;
            else fi[i] = 0;
//            cout<<"*"<<a[i]<<" "<<s[(i+3)%6]<<endl;
        }
        if( flag ){
            ans.clear();
            tmp.clear();
            int t = 0;
            for(int i=0;i<3;i++)
                if( a[t] < a[i] )
                    t = i;
            int x = (t+1)%3 , y = (t+2)%3;
            if( a[t] <= a[x] + a[y] ){
                int k = a[x] + a[y] - a[t];
                for(int i=0;i<a[t];i++){
                    tmp.push_back(t*2);
                    if(a[x]){
                        tmp.push_back(x*2);
                        a[x]--;
                        if( i < k )
                            tmp.push_back(y*2);
                    }else
                        tmp.push_back(y*2);
                }
//                printf("sa\n");
                for(int i=0;i<tmp.size();i++){
                    ans.push_back(tmp[i]);
                    int t = tmp[i];
                    if( fi[t/2] ){
                        for(int i=0;i<s[(t+3)%6];i++){
                            ans.push_back((t+3)%6);
                            ans.push_back(t);
                        }
                        fi[t/2] = 0;
                    }
                }
            }else
                flag = 0;
        }
        if( ans.size() && ans.back() == ans[0] )
            flag = 0;
        printf("Case #%d: ",++CASE);
        if(flag){
            assert(ans.size() == n);
            for(int i=0;i<ans.size();i++)
                putchar(id[ans[i]]);
            for(int i=0;i<ans.size();i++)
                assert( ans[i] != ans[(i+1)%ans.size()] );
            puts("");
        }else{
            int t = -1 , c = 0;
            for(int i=0;i<6;i++)
                if( s[i] )
                    c++ , t = i;
            if( c == 2 && s[t] == s[(t+3)%6] ){
                for(int i=0;i<s[t];i++)
                    printf("%c%c",id[t],id[(t+3)%6]);
                puts("");
            }else{
                puts("IMPOSSIBLE");
//                for(int i=0;i<6;i++)
//                    printf("%d ",s[i]);puts("");
//                assert( s[0] > s[2] +s[4] || s[2] > s[0] +s[4] || s[4] > s[2] +s[0] );
            }
        }
    }
    return 0;
}
