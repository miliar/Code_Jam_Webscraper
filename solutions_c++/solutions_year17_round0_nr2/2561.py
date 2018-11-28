#include<iostream>
#include<fstream>
#include<iomanip>
#include<string>
#define cin ifile
#define cout ofile

using namespace std;
string ans;

void func(string num)
{
    if(num.size()==0)
        return;
    string temp;
    for(int i=0;i<num.size();i++)
    {
        temp+=num[0];
    }

    if(temp>num)
    {
        ans+=num[0]-1;
        for(int i=1;i<num.size();i++)
            ans+='9';
        return;
    }
    else
    {
        ans+=num[0];
        func(num.substr(1,num.size()-1));
    }
}

int main()
{
    ifstream ifile("B-large.in");
    ofstream ofile("out1.txt");
    int t;
    cin>>t;

    for(int fff=1;fff<=t;fff++)
    {
        string str;
        cin>>str;

        ans="";
        string temp;
        for(int i=0;i<str.size();i++)
        {
            temp+='1';
        }
        if(temp>str)
        {
            for(int i=1;i<str.size();i++)
            {
                ans+='9';
            }
        }
        else
        {
            func(str);
        }

             cout<<"Case #"<<fff<<": "<<ans<<"\n";
       }
    return 0;
}
