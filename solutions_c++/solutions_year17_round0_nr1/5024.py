    #include <math.h>
    #include <iostream>
    #include <map>
    #include <vector>
    #include <set>
    #include <cstring>
    #include <algorithm>
    #include <stack>
    #include <queue>
    #include <cstring>
    #include <sstream>
    #include <stdlib.h>
    #include <stdio.h>
    #include <cctype>
    #define inf 2000000000
    #define MOD 1000000007
    #define MAX 100005
    #define M   10000007
    typedef long long ll;
    using namespace std;
    string s;
    int k;
    int ans1=0;
    int ans2=0;
    int main(){
    int TC,tc=0;
    freopen("A-large.in","r",stdin);
    freopen("output.in","w",stdout);
    scanf("%d",&TC);
    while(TC--){
    tc++;ans1=0; ans2=0;
    cin>>s;
    scanf("%d",&k);
    int n=s.size();
    string ss="";
    for(int i=0; i<n; i++){
        ss+=s[i];
    }
    for(int i=0; i<n; i++){
    if(s[i]=='-'&&(n-i)>=k){
     int j=0; ans1++;
    while(j<k&&j<n){
    if(s[i+j]=='-')s[i+j]='+';
    else s[i+j]='-';
    j++;
     }
     }
    }
    reverse(ss.begin(),ss.end());
    for(int i=0; i<n; i++){
    if(ss[i]=='-'&&(n-i)>=k){
     int j=0;ans2++;
    while(j<k&&j<n){
    if(ss[i+j]=='-')ss[i+j]='+';
    else ss[i+j]='-';
    j++;
     }
     }
    }bool b=1;
    for(int i=0; i<n; i++){
    if(s[i]!='+'){
    b=0; break ;
    }
      }
    if(!b){b=1;
    for(int i=0; i<n; i++){
    if(ss[i]!='+'){
    b=0; break;
    }}}
    if(!b){printf("Case #%d: IMPOSSIBLE\n",tc);continue ;}
    int ans=min(ans1,ans2);
    printf("Case #%d: %d",tc,ans);
    printf("\n");
    }
    return 0;
    }
