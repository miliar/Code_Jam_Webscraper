#include<iostream>
#include<fstream>
#include<string>
using namespace std;
int main()
{
     ifstream my;
    my.open("d.txt");
    ofstream myf;
    myf.open("small_output.txt");
    int T,k,l;
    string S;
    my>>T;
    for(int i=1;i<=T;i++)
    {
        my>>S>>k;
        int count=0;
        l=S.length();
        for(int j=0;j<l;j++)
        {
            if(S[j]=='-')
            {
                if(j+k>l)
                {
                    myf<<"Case #"<<i<<": IMPOSSIBLE"<<endl;
                    goto O;
                }
                else
                {
                count ++;
                for(int p=j;p<j+k;p++)
                {
                    if(S[p]=='-')
                    {
                        S.replace(p,1,"+");
                    }
                    else
                    {
                        S.replace(p,1,"-");
                    }
                }
                }
            }
        }
        myf<<"Case #"<<i<<": "<<count<<endl;
        O:  ;
    }
    my.close();
    myf.close();
    return 0;
}
