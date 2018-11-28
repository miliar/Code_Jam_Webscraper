#include<bits/stdc++.h>
using namespace std;
bool check(string str)
{
    for(int i=0;i<str.length();i++){
        if(str[i]=='-')
            return false;
    }
    return true;
}
int main()
{
    freopen("A-large.out","w",stdout);
    freopen("A-large.in","r",stdin);
    int tc,t=0;
    cin>>tc;
    getchar();
    while(t<tc){
        t++;
        string str;
        int f;
        cin>>str>>f;
        int len;
        len=str.length();
        int cnt=0;
        for(int i=0;i<=len-f;i++){
            if(str[i]=='+')
                continue;
            for(int j=i;j<i+f;j++){
                if(str[j] == '-')
                    str[j] = '+';
                else
                    str[j] = '-';
            }
            cnt++;
        }
        if(check(str))
            printf("Case #%d: %d\n",t,cnt);
        else
            printf("Case #%d: IMPOSSIBLE\n",t);
    }

    return 0;
}

