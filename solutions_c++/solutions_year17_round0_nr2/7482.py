#include <bits/stdc++.h>

using namespace std;

int main()
{
    //freopen("B-large.in","r",stdin);
    //freopen("B-large.out","w",stdout);
    int t;
    cin>>t;
    for(int ca=1;ca<=t;ca++){
        string num;
        cin>>num;
        printf("Case #%d: ",ca);
        if(num.size()==1){
            printf("%s\n",num.c_str());
            continue;
        }
        int i;
        for(i=0;i+1<num.size();i++)if(num[i]>num[i+1])break;
        if(i+1==num.size()){
            printf("%s\n",num.c_str());
            continue;
        }
        while(i-1>=0 && num[i-1]==num[i])i--;
        num[i]--;i++;
        while(i<num.size())num[i++]='9';
        if(num[0]=='0')num=num.substr(1);
        printf("%s\n",num.c_str());
    }
    return 0;
}
