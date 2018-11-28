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
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("outttt.in","w",stdout);
    int t,cas=1;
    scanf("%d",&t);
    while(t--){
    int sz;
    int idx=0;
    string s;
        cin>>s;
        sz=s.size();
        for(int i=0; i<sz-1; i++){
            if(s[i]-'0' > s[i+1]-'0'){
                idx=i+1;
                break;
            }
        }
    if(idx==0){
        cout<<"Case #"<<cas++<<": ";
        for(int i=0; i<sz; i++){
            if(s[i]!='0'){
                cout<<s[i];
                }
            }
        }
        else{
            for(int i=idx; i>=1; i--){
                if(s[i]-'0' < s[i-1]-'0'){
                    s[i]='9';
                    s[i-1]=s[i-1]-'0';
                    s[i-1]--;
                    s[i-1]+='0';
                }
            }
            for(int i=idx; i<sz; i++){
                s[i]='9';
            }
        cout<<"Case #"<<cas++<<": ";
        for(int i=0; i<sz; i++){
                if(s[i]!= '0'){

                    cout<<s[i];

                }
            }
        }
        /*
        else{
            for(int i=sz-1; i>=idx; i--){
                s[i]='9';
            }
            s[idx-1]=s[idx-1]-'0';
            s[idx-1]--;
            s[idx-1]=s[idx-1]+'0';
            cout<<"Case #"<<cas++<<": ";
            for(int i=0; i<sz; i++){
            if(s[i]!='0'){
                cout<<s[i];
                }
            }
        }*/
        cout<<endl;
    }
    return 0;
}
