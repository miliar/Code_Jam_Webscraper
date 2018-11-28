#include<iostream>
#include<cstring>
#include<fstream>

using namespace std;

typedef long long int lli;

int main()
{
    lli t;
    cin>>t;
    ofstream a_out("a.txt");

    for(lli h=0;h<t;h++)
    {
        string s;
        lli k,cnt=0,flag=0;

        cin>>s>>k;

        for(lli i=0;i<s.length()- (k-1);i++)
        {
            if(s.at(i) == '-')
            {
                cnt++;
                for(lli j=i;j<i+k;j++)
                {
                    if(s.at(j) == '+')
                    {
                        s.at(j) = '-';
                    }

                    else
                    {
                        s.at(j) = '+';
                    }
                }
                //cout<<s<<endl;
            }
        }

        for(lli i = s.length()- (k-1);i<s.length();i++)
        {
            //cout<<i<<endl;
            if(s.at(i) == '-')
            {
                flag = 1;
                break;
            }
        }

        if(flag==1)
        {
            cout<<"Case #"<<h+1<<":"<<" "<<"IMPOSSIBLE"<<endl;
            a_out<<"Case #"<<h+1<<":"<<" "<<"IMPOSSIBLE"<<endl;
        }

        else
        {
            cout<<"Case #"<<h+1<<":"<<" "<<cnt<<endl;
            a_out<<"Case #"<<h+1<<":"<<" "<<cnt<<endl;
        }
    }

    return 0;
}
