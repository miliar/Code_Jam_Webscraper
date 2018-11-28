#include <iostream>
#include <string>
#include <fstream>
using namespace std;
int main()
{
    ifstream fin("a_large.in");
    ofstream fout("a_large.out");
    int num=0;
    int k=0;
    int count=0;
    string input;
    fin>>num;
    for(int i=0;i<num;++i)
    {
        count=0;
        fin>>input;
        fin>>k;
        //cout<<input<<k<<endl;
        int j=0;
        for(j=0;j<=input.size()-k;++j)
        {
            if(input[j]=='-')
            {
                ++count;
                for(int l=j;l<j+k;++l)
                {
                    if(input[l]=='-') input[l]='+';
                    else input[l]='-';
                }
            }
            //cout<<input<<endl;
        }
        int flag=0;
        for(--j;j<=input.size();++j)
        {
            if(input[j]=='-')
            {
                flag=1;
                break;
            }
        }
        fout<<"Case #"<<i+1<<": ";
        if(flag==1) fout<<"IMPOSSIBLE"<<endl;
        else if(flag==0) fout<<count<<endl;
    }
}