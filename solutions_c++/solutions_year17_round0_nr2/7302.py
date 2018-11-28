#include<bits/stdc++.h>
using namespace std;
string s;

void check(int i,int l)
{
    for(int j=i;j<l;j++)
        s[j]='9';
}
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t,cs=0;
    scanf("%d",&t);
    while(t--){
        string s1;
        cin>>s;
        int l=s.length();

        for(int i=l-1;i>0;i--){
            if(s[i]>=s[i-1])continue;
            int v=s[i-1]-'0';
            s[i-1]=(v-1)+'0';
            check(i,l);
        }
        for(int i=0;i<l;i++){
            if(s[i]=='0')continue;
            s1+=s[i];
        }
        printf("Case #%d: ",++cs);
        cout<<s1<<endl;
    }
}
