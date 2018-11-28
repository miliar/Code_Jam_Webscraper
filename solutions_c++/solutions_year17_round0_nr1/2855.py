//
//  A.cpp
//  
//
//  Created by Kesarwani, Prateek on 4/9/17.
//
//

#include<iostream>
using namespace std;
int main(){
    int T;
    scanf("%d",&T);
    for(int t=1;t<=T;++t){
        string s;
        cin>>s;
        int K,ans=0;
        scanf("%d",&K);
        int qq=0;
        for(int i=0;i<s.size();++i){
            if(s[i]=='+')
                continue;
            ++ans;
            for(int j=i,cnt=0;cnt<K;++cnt,++j){
                if(j==s.size()){
                    qq=1;
                    break;
                }
                if(s[j]=='+')
                    s[j]='-';
                else
                    s[j]='+';
            }
            if(qq)
                break;
        }
        printf("Case #%d: ",t);
        if(qq)
        printf("IMPOSSIBLE\n");
        else
        printf("%d\n",ans);
    }
    return 0;
}
