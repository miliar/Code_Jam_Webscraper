//
//  main.cpp
//  google_jam_qa
//
//  Created by Ken-Hao Liu on 08/04/2017.
//  Copyright © 2017 Ken-Hao Liu. All rights reserved.
//

#include <iostream>
using namespace std;

class Solution{
public:
    int K;
    int solve(string &s, int k){
        K=k;
        return cal(s,0,0);
    }
    
    int cal(string &s, int start,int cnt){
//        printf("cal %d\n",start);
        while(start<s.size()&&s[start]=='+')start++;
        if(start==s.size())return cnt;
        if(start>s.size()-K)return -1;
        int next=-1;
        for(int j=start;j<start+K;j++){
            if(s[j]=='-')s[j]='+';
            else{
                if(next<0)next=j;
                s[j]='-';
            }
        }
        if(next>=0)return cal(s,next,cnt+1);
        start+=K;
        while(start<s.size()&&s[start]=='+')start++;
        return cal(s,start,cnt+1);
    }
};

int main(int argc, const char * argv[]) {
    int t,k;
    string s;
    scanf("%d\n",&t);
    for(int i=0;i<t;i++){
        Solution sol;
        cin>>s>>k;
        int ans=sol.solve(s,k);
        if(ans>=0)printf("Case #%d: %d\n",i+1,ans);
        else printf("Case #%d: IMPOSSIBLE\n",i+1);
    }
    return 0;
}
