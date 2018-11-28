#include <iostream>

using namespace std;

int main()
{
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("oneA.txt", "w", stdout);
    int t;
    scanf("%d",&t);
    for(int a = 1 ; a<=t;a++){
        string s;
        cin>>s;
        for(int i = 1 ; i < s.size();i++){
            if(s[i] < s[i-1]){
                s[i-1]--;
                for(int j = i ; j <s.size();j++)
                    s[j]='9';
                if(i>=1)
                    i=i-2;
            }
        }
        int index=0;
        while(s[index] == '0')
            index++;
        printf("Case #%d: ",a);
        for(int i = index;i<s.size();i++)
            printf("%c",s[i]);
        printf("\n");
    }
    return 0;
}
