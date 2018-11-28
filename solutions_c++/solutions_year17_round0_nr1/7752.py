#include <bits/stdc++.h>
#include <iostream>

using namespace std;

int main()
{
    int t;
    ofstream file;
    ifstream input;
    file.open("A-output1.txt");
    input.open("A-large.in");
    input >>t;
    int n=1;
    while(n<=t)
    {
        string s;
        int k,counter=0,c=0;
        input >>s;
        input >>k;
        for(int i=0;i<s.length();i++)
        {
            if(s[i]=='-'&&(s.length()-i)>=k)
            {
                c++;
                for(int j=0;j<k;j++)
                {
                    if(s[i+j]=='-')
                        s[i+j]='+';
                    else
                        s[i+j]='-';
                }
            }
        }
        for(int i=0;i<s.length();i++)
        {
            if(s[i]=='+')
                counter++;
        }
        file<<"Case #"<<n<<": ";
        if(counter==s.length())
            file<<c<<endl;
        else
            file<<"IMPOSSIBLE"<<endl;
        n++;
    }
    return 0;
}
