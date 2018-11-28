#include<iostream>
#include<fstream>
#include<stdlib.h>
#include<string.h>
using namespace std;

int main()
{
    int t,k,i,j=1,x,l;
    ifstream ifile ("A-large.in");
    ofstream ofile ("output.txt");
    ifile>>t;
    char *s=(char *)calloc(1001,sizeof(char));
    while(t--)
    {
        int c=0;
        ifile>>s>>k;
        l=strlen(s);
        for(i=0;i<=l-k;i++)
        if(s[i]=='-')
        {
            for(x=0;x<k;x++)
            if(s[i+x]=='-')
                s[i+x]='+';
            else
                s[i+x]='-';
            c++;
        }
        for(i=l-k+1;i<l;i++)
        if(s[i]=='-')
        {ofile<<"Case #"<<j<<": IMPOSSIBLE"<<endl;c=-1;break;}
        if(c!=-1)
        ofile<<"Case #"<<j<<": "<<c<<endl;
        j++;
    }
}

