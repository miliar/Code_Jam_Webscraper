#include<bits/stdc++.h>
using namespace std;
string s;
int k,t,i,cnt;

void flip(int i){
    int j;
    for(int j=i;j<i+k;j++){
        if(s[j] == '-')
            s[j] = '+';
        else
            s[j] = '-';
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cin>>t;
    for(int tt=1;tt<=t;tt++){
        cin>>s;
        cin>>k;
        cnt = 0;
        int len = s.length();
        for(i=0;i<=len-k;i++){
            if(s[i] == '-'){
                flip(i);
                cnt++;
                //for(int x=0;x<len;x++)
                    //cout<<s[x]<<" ";
                //cout<<endl;
                }
            }
            int flag=0;
            for(i=0;i<len;i++)
                if(s[i]=='-'){
                    flag = 1;
                break;
            }
        if(flag)
            printf("Case #%d: IMPOSSIBLE\n",tt);
        else
            printf("Case #%d: %d\n",tt,cnt);
    }

}
