#include<stdio.h>
#include<iostream>

using namespace std;
/*
int verify(int nr)
{
    int prev=10;
    for(;nr>0 && nr%10<=prev; nr/=10) prev = nr%10;
    return nr==0;
}

int main()
{
    freopen("in.txt", "w", stdout);
    int i, j;
    printf("1000000\n");
    for(i=1;i<=100000;i++)
        printf("%d\n", i);
    freopen("ok.txt", "w", stdout);
    for(i=1;i<=100000;i++)
    {
        for(j=i;verify(j)==0;j--);
        printf("%d\n", j);
    }
    return 0;
}

*/

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int n,i,j;
    cin>>n;
    string s;
    for(int I=1;I<=n;I++)
    {
        cin>>s;
        cout<<"Case #"<<I<<": ";
        for(i=s.size()-1;s[i]>=s[i-1] && i>0;i--);
        if(i==0)
            cout<<s<<"\n";
        else{
            int pos;
            for(pos=0;pos<s.size()-1 && s[pos]<=s[pos+1];pos++);
            for(i=s.size()-1;i>pos && i>0;i--) s[i]='9';
            for(;s[i]<=s[i-1] && i>0;i--)
                s[i]='9';
            s[i]-=1;
            if(s[0]!='0')
                cout<<s<<"\n";
            else  cout<<s.substr(1)<<"\n";
        }
    }


    return 0;
}
