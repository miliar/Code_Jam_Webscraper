//
//  GCJB.cpp
//  
//
//  Created by Kesarwani, Prateek on 4/8/17.
//
//

#include <iostream>
using namespace std;
int main(){
    int T;
    scanf("%d",&T);
    for(int t=1;t<=T;++t){
        string s;
        cin>>s;
        int L=s.size();
        char p='9';
        for(int i=L-1;i>=0;--i){
            if(s[i]<=p){
                p=s[i];
                continue;
            }
            s[i]--;
            p=s[i];
            for(int x=i+1;x<L;++x){
                s[x]='9';
            }
        }
        printf("Case #%d: ",t);
        int fl=0;
        for(int i=0;i<L;++i){
            if(s[i]=='0' && !fl)
                continue;
            fl=1;
            printf("%c",s[i]);
        }
        printf("\n");
    }
    return 0;
}
