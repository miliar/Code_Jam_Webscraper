#include <iostream>
#include <cstdio>
#include <queue>
#include <cstring>
#include <algorithm>
#define maxn 1000100
#define maxm 10010
#define inf 0x3f3f3f3f

using namespace std;

int main() {
    int T,Cas = 1;
    scanf("%d",&T);
    while(T--){
        int length,m,f,i,j;
        string s,str,str1,str2;
        cin>>s;
        length=s.length();
        m = -1;
        for(j = 0;j < length-1;++ j){
            if(s[j] > s[j+1]){
                m = j;
                break;
            }
        }
        printf("Case #%d: ",Cas);
        Cas++;
        if(m == -1){
            cout<<s<<endl;
            continue;
        }
        f = m;
        while(f){
            s[f] = s[f]-1;
            if(s[f-1] <= s[f])
                break;
            else{
                f--;
            }
        }
        if(s[0] > s[1])
            s[0] = s[0]-1;
        str="";
        for(i = 0;i <= f;++ i)
            str += s[i];
        str1 = "";
        str1 = str;
        for(i = f + 1;i < length;++ i)
            str1 += '9';
        int w = str1.length();
        str2 = "";
        int v = 0;
        for(i = 0;i < str1.length();++ i)
            if(str1[i] > '0'){
                v = i;
                break;
            }
        for(j = v;j < str1.length();++ j)
            str2 += str1[j];
        cout<<str2<<endl;
    }
}

