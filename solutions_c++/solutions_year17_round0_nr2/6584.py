#include<iostream>
#include<fstream>
#include<stdlib.h>
#include<string.h>
using namespace std;

int main()
{
    int t,i,j,k,l,c=0;
    ifstream ifile ("B-large.in");
    ofstream ofile ("B-largeoutput.txt");
    char *s=(char *)calloc(25,sizeof(char));
    ifile>>t;
    for(j=1;j<=t;j++)
    {
        ifile>>s;
        c=0;
        l=strlen(s);
        for(i=0;i<l;i++)
        if(s[i]=='0')
        {
            s[i-1]--;
            for(;i<l;i++)
                s[i]='9';
            break;c=1;
        }
        if(c==0)
        for(i=l-1;i>0;i--)
        if(s[i]<s[i-1])
        {
            s[i-1]--;
            for(k=i;k<l;k++)
                s[k]='9';
        }
        ofile<<"Case #"<<j<<": ";
        if(s[0]!='0')
            ofile<<s[i];
        ofile<<s+1<<endl;
    }
}
