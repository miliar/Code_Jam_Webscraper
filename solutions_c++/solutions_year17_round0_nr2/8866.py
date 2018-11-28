#include<iostream>
#include<fstream>
#define llu unsigned long long int
#define fin cin
#define fout cout
using namespace std;
int main()
{
    ifstream fin;
    fin.open("B-small-attempt1.in");
    ofstream fout;
    fout.open("B.out");
    ios_base::sync_with_stdio(false);
    int t;
    fin>>t;
    for(int i=1;i<=t;i++)
    {
        string num;
        fin>>num;
        if(num.size()==1)
        {
            fout<<"Case #"<<i<<": "<<num<<endl;
            continue;
        }
        int count(0);
        int dekh(0);
        for(int i=0;i<num.size()-1;i++)
        {
            if(num[i]==num[i+1]) count++;
            if(num[i]>num[i+1]) dekh = 1;
        }
        if(count == num.size()-1)
            fout<<"Case #"<<i<<": "<<num<<endl;
        else if(dekh == 0)
            fout<<"Case #"<<i<<": "<<num<<endl;
        else
        {
            int cnt(0);
            for(int i=0;i<num.size()-1;i++)
            {
                if(num[i] >= num[i+1])
                {
                    if(cnt==0)
                    {
                        num[i]=num[i]-1;
                        num[i+1]='9';
                    }
                    else
                        num[i+1]='9';
                    cnt++;
                }
            }
            fout<<"Case #"<<i<<": ";
            int f(0);
            for(int i=0;i<num.size();i++)
            {
                if(num[i]=='0' && f==0)
                    continue;
                else if(num[i]=='1')
                {
                    f=1;
                    fout<<num[i];
                }
                else
                    fout<<num[i];
            }
            fout<<endl;
        }
    }
    fin.close();
    fout.close();
    return 0;
}
