

#include<iostream>
#include<algorithm>
#include<memory.h>
#include<stdio.h>
#include<string>
#include<vector>
#include<bitset>
#include<climits>
#include<fstream>


using namespace std;

typedef long long int lli;
typedef unsigned long long int ulli;

int main()
{
    int t,index,tc;

    string s;

    ofstream a_out("b.txt");

    cin>>t;



    for(int tc=1;tc<=t;tc++)
    {
        index=0;

        cin>>s;

        for(int i=1;i<s.length();i++)
        {
            if(s[i]<s[i-1])
            {
                s[i-1]-=1;
                index=i-1;
                for(;i<s.length();i++)
                {
                    s[i]='9';
                }
            }
        }


        for(int i=index;i>=0;i--)
        {
            if(s[i]<s[i-1] && i>0)
            {
                s[i]='9';
                s[i-1]-=1;
            }
        }



        cout<<"Case #"<<tc<<": ";
        a_out<<"Case #"<<tc<<": ";

        if(s[0]=='0')
        {
            for(int i=1;i<s.length();i++)
            {
                cout<<s[i];
                a_out<<s[i];
            }
        }
        else
        {
            for(int i=0;i<s.length();i++)
            {
                cout<<s[i];
                a_out<<s[i];
            }

        }

        cout<<endl;
        a_out<<endl;

    }
    return 0;
}

/*11
132
1000
7
111111111111111110
88812
68812
966612
7681
7781
6681
6688812*/
