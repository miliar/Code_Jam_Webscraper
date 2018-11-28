#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <math.h>
#include <fstream>
#include <string.h>
#include <cstring>
using namespace std;
string s;
int k;
int main(){
    int tc,cas=1;
freopen("A-large.in","r",stdin);
freopen("output.in","w",stdout);
    scanf("%d",&tc);
    while(tc--){
    int ans1=0,ans2=0;
    cin>>s;
    cin>>k;
    int sz=s.size();
    string s2="";
    for(int i=0; i<sz; i++){
        s2+=s[i];
    }
    for(int i=0; i<sz; i++){
    if(s2[i]=='-'&&(sz-i)>=k){
    int j=0; ans1++;
    while(j<k&&j<sz){
    if(s2[i+j]=='-')s2[i+j]='+';
    else s2[i+j]='-';
    j++;
        }
    }
}
    reverse(s.begin(),s.end());
    for(int i=0; i<sz; i++){
    if(s[i]=='-'&&(sz-i)>=k){
     int j=0;ans2++;
    while(j<k&&j<sz){
    if(s[i+j]=='-')s[i+j]='+';
    else s[i+j]='-';
    j++;
        }
    }
}
    bool b1=1;
    for(int i=0; i<sz; i++){
    if(s2[i]=='-'){
        b1=0; break;
        }
      }
    bool b2=1;
    for(int i=0; i<sz; i++){
        if(s[i]!='-'){
        b2=0; break;
        }
    }
    if(!b1 && !b2){printf("Case #%d: IMPOSSIBLE\n",cas++);continue ;}
        printf("Case #%d: %d",cas++,min(ans1,ans2));
        cout<<endl;
        }
    return 0;
}
