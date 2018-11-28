#include<iostream>
#include<fstream>
using namespace std;

int main()
{
    int i,j,T,K,k;
    ifstream in("input.txt");
    ofstream out("output.txt");
    in>>T;
    for(i=0;i<T;i++)
    {
        int total=0,loc;
        string S;
        in>>S>>K;
        for(k=0;k<S.size();k++)
        {
            loc=-1;
        for(j=0;j<S.size();j++)
            if(S[j]=='-')
            {
                loc=j;
                break;
            }
        if(loc!=-1&&loc+K<=S.size())
        {
        for(j=loc;j<loc+K;j++)
            if(S[j]=='-')
                S[j]='+';
            else
                S[j]='-';
        total++;
        }
        }
        for(j=0;j<S.size();j++)
            if(S[j]=='-')
            {
            total=-1;
            break;
            }
        if(total==-1)
            out<<"Case #"<<i+1<<": "<<"IMPOSSIBLE"<<endl;
        else
            out<<"Case #"<<i+1<<": "<<total<<endl;
    }
}