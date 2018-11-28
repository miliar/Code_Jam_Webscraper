#include<bits/stdc++.h>

using namespace std;

int main()
{
    ofstream cout;   ifstream cin;
    cout.open("out_big.txt");
    cin.open("large.in");

    int t,T,i,k;
    char s[25];
    cin>>T;
    for(t=1;t<=T;t++)
    {
        cin>>s; k=100;
        for(i=strlen(s)-1;i>=1;i--)
        {
            if(s[i]<s[i-1])
            {
                s[i-1]--; k=i;
            }
        }
        for(i=k;i<strlen(s);i++){s[i]='9';}
        if(s[0]=='0')
        {
            for(i=0;i<strlen(s)-1;i++){s[i]=s[i+1];}
            s[strlen(s)-1]='\0';
        }
        cout<<"Case #"<<t<<": "<<s<<"\n";
    }
    return 0;
}
