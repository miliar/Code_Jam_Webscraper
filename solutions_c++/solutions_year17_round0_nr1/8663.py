#include<bits/stdc++.h>
using namespace std;
int main(){

    freopen("A-small-attempt1.in","r",stdin);
    freopen("output0.txt","w",stdout);
    int t;
    string s;
    scanf("%d",&t);
    for(int i=0;i<t;i++){
        bool impossible = false;
        int flips=0;
        cin >> s;
        int f;
        scanf("%d",&f);
        for(int j=0;j<=s.length()-f;j++){
            if(s[j]=='-'){
                    flips++;
                for(int k=j;k<j+f;k++){
                    if(s[k]=='-'){
                        s[k]='+';
                    }
                    else {
                        s[k]='-';
                    }
                }
            }
        }
        for(int z=s.length()-f;z<s.length();z++){
            if(s[z]=='-'){
                impossible = true;
                break;
            }
        }

        if(!impossible){
                printf("Case #%d: %d\n",i+1,flips);
        }
        else {
            printf("Case #%d: IMPOSSIBLE\n",i+1);
        }

    }
    return 0;
}
