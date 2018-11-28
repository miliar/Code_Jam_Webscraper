#include<bits/stdc++.h>
using namespace std;
#define inc(i,x) for(int i=0;i<x;i++)
#define onc(i,x) for(int i=1;i<=x;i++)
typedef long long ll;

char s[20];
char n[20];
int len;

bool find(int d,int lb)
{
    if(d>=len) return 1;
    int me=s[d]-'0';
    if(me<lb) return 0;
    n[d]=me+'0';
    if(find(d+1,me)) return 1;
    if(me>0&&me-1>=lb){
        n[d]=me-1+'0';
        for(int i=d+1;i<len;i++) n[i]='9';
        return 1;
    }
    return 0;
}

main()
{
    int t;
    cin>>t;
    onc(kase,t){
        cin>>s;
        len=strlen(s);
        find(0,0);
        bool flag=0;
        cout<<"Case #"<<kase<<": ";
        for(int i=0;i<len;i++){
            if(n[i]=='0'&&!flag){
                continue;
            }
            flag=1;
            cout<<n[i];
        }
        cout<<'\n';
    }
}
