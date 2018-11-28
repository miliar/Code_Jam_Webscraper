#include<cstdio>
#include<string>
#include<iostream>
#include<algorithm>
#include<cstring>
#include<queue>
#include<vector>
#include<deque>
using namespace std;

int T;
int main(){
    freopen("B-large.in","r",stdin);
    freopen("outputB.txt","w",stdout);
    scanf("%d",&T);
    for(int i=1;i<=T;i++){
        string s;
        cin >> s;
        int cnt=0;
        while(1){
            bool flag = false;
            for(int j=s.size()-1;j>0;j--){
                if(s[j-1]>s[j]){
                    flag=true;
                    s[j]='9';
                    if(s[j-1]=='9'&&cnt==0){
                        int temp = (s[j-1]-'0')-1;
                        s[j-1]=temp+'0';
                    }
                    else if(s[j-1]!='9' && s[j-1]>0){
                        int temp = (s[j-1]-'0')-1;
                        s[j-1]=temp+'0';
                    }
                }
            }
            if(!flag)
                break;
            cnt++;
        }
        long long a = atoll(s.c_str());
        printf("Case #%d: %lld\n",i,a);

    }
    return 0;
}

