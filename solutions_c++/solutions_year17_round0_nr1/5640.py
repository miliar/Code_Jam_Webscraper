#include <iostream>
#include<bits/stdc++.h>
using namespace std;

int main()
{
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("oneA.txt", "w", stdout);
    int t;
    scanf("%d",&t);
    for(int a=1;a<=t;a++){
        string s;
        cin>>s;
        int k;
        scanf("%d",&k);
        int counter=0;
        bool flag = false;
        for(int i=0;i<s.size();){
            if(s[i] == '-' && i+k-1<s.size()){
                s[i] = '+';
                for(int j=1;j< k ; j++){
                    if(s[i+j] == '-')s[i+j]='+';
                    else s[i+j]='-';
                }
                counter++;
                i++;
            }else if(s[i] == '-'){
                flag = true;
                printf("Case #%d: IMPOSSIBLE\n",a);
                break;
            }else{
                i++;
            }

        }
        if(!flag)
            printf("Case #%d: %d\n",a,counter);
    }

    return 0;
}
