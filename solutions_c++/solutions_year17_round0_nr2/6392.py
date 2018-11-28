#include<bits/stdc++.h>
using namespace std;
char ch[20];
void fillnine(int n)
{
    for(int i=n;isdigit(ch[i]);i++)
        ch[i]='9';
}
int main()
{
    int t;

    fstream it;
    it.open("B-large.in",ios::in);
    ofstream io;
    io.open("out1.txt",ios::out);
    it>>t;
    int pre;
    for(int k=0;k<t;k++)
    {

        for(int i=0;i<20;i++)
        {
            ch[i]='a';
        }
        int flag=1;
        it>>ch;

        restart:

        int j=0;
        pre=ch[j];
        //j++;
        while(isdigit(ch[j+1]))
        {
            cout<<"t";
            if(pre>ch[j+1])
            {
                if(pre>'1')
                {
                    ch[j]--;;
                    fillnine(j+1);
                    cout<<"a";
                    goto restart;
                }
                else
                {
                    ch[j]='0';
                    fillnine(j+1);
                    cout<<"h"<<" "<<ch;
                    goto restart;
                }


            }

            j++;
            pre=ch[j];

        }
        //cout<<ch<<"\t"<<ch.length();
        //finish:
        io<<"Case #"<<k+1<<": ";
        flag=0;
        for(int i=0;isdigit(ch[i]);i++)
        {
            if(ch[i]!='0')
                io<<ch[i];
        }
        io<<endl;
        cout<<"Case #"<<k+1<<": "<<ch<<endl;
    }

}
