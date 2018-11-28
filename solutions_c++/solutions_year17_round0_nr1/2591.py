#include<iostream>
#include<fstream>
#include<iomanip>
#include<string>
#define cin ifile
#define cout ofile

using namespace std;



int main()
{
    ifstream ifile("A-large.in");
    ofstream ofile("out1.txt");
    int t;
    cin>>t;

    for(int fff=1;fff<=t;fff++)
    {
        string str;
        int k;
        cin>>str>>k;
        int cnt=0;
        int flag=1;

        for(int i=0;i<str.size();i++)
        {
            if(str[i]=='+')
                continue;
            else
            {
                cnt++;
                if(i+k-1<str.size())
                {
                   for(int j=0;j<k;j++)
                   {
                       if(str[i+j]=='+')
                            str[i+j]='-';
                       else
                            str[i+j]='+';
                   }
                }else
                    {
                        flag=0;
                        break;
                    }
            }
        }
        if(flag==0)
             cout<<"Case #"<<fff<<": "<<"IMPOSSIBLE"<<"\n";
        else
            cout<<"Case #"<<fff<<": "<<cnt<<"\n";
    }
    return 0;
}
