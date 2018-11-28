#include <iostream>
#include <fstream>
#include <string>
using namespace std;
string s;
void flip (int i2,int k2)
{
    int j;
    for(j=i2;j<=i2+k2-1;++j)
    {
        if(s[j]=='+')
            s[j]='-';
        else
            s[j]='+';
    }
}
int main()
{
    ifstream fin;
    fin.open("smallin.txt");
    ofstream fout;
    fout.open("smallout.txt");
    int t,x=1;
    fin>>t;
    while(x<=t)
    {
        int k;
        fin>>s;
        fin>>k;
        int i,len=s.length();
        int c=0,flag=0;
        for(i=0;i<len;i++)
        {
            if(s[i]=='-')
            {
                if(i<=(len-k))
                    {flip(i,k);++c;}
                else
                {flag=1;break;}
            }
        }
        //cout<<s;
        fout<<"Case #"<<x<<": ";
        if(flag==0)
            fout<<c;
        else
            fout<<"IMPOSSIBLE";

        fout<<endl;
        ++x;//s.clear();
    }
    return 0;
}
