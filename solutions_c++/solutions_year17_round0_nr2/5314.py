#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
using namespace std;
int T;
string N;
char rez[20];
int main()
{
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);
    cin>>T;
    for(int t=1;t<=T;t++)
    {
        cin>>N;
        cout<<"Case #"<<t<<": ";
        int poz=0;
        memset(rez,'\0',sizeof(rez));
        while(poz<N.size()-1&&N[poz]<=N[poz+1]){rez[poz]=N[poz];poz++;}
        rez[poz]=N[poz];
        if(poz==N.size()-1) {cout<<rez<<"\n";continue;}
        while(poz&&rez[poz-1]>rez[poz]-1)
            poz--;
        rez[poz]=N[poz]-1;poz++;
        while(poz<N.size()) rez[poz++]='9';
        int i=0;
        while(rez[i]=='0'&&i<poz-1)i++;
        cout<<rez+i<<'\n';
    }
    return 0;
}
