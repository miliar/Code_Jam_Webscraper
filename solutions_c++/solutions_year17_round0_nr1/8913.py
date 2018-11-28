#include<iostream>
#include<fstream>
#include<cstring>
using namespace std;
ifstream in("pk.in");
ofstream out ("pk.out");

int main()
{
    char *s = new char[1005];
    int n,k, a[1005], len, i, cnt, bec, j, l;
    in>>n;
    for(l = 1; l<= n; l++)
    {
        bec=1;
        cnt=0;
        in>>s;
        in>>k;
        len = strlen(s);
        for(i=0;i<len;i++)
            if(s[i]=='+')
                a[i]=1;
            else if(s[i]=='-')
                a[i]=0;
        for(i=0;i<=len-k;i++)
        {
            if(a[i]==0)
            {
                cnt++;
                for(j=0;j<k;j++)
                    a[i+j]=!a[i+j];
            }
        }
        for(i=0;i<len;i++)
        {
            if(a[i]==0)
            {
                bec=0;
                break;
            }
        }
        if(bec==1)
            out<<"Case #"<<l<<": "<<cnt<<endl;
        else
            out<<"Case #"<<l<<": IMPOSSIBLE"<<endl;
    }


}
