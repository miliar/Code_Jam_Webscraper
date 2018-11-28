#include<iostream>
#include<stdlib.h>
#include<string>
#include<stdio.h>

using namespace std;

int chek(string s,int i)
{
    while(s[i]!='-'&&i<s.length())
    {
        i++;
    }
    return i;
}

int check(string s,int n)
{
    string s1(s);
    for(int i=0;i<s.length();i++)
        s1.at(i)='+';
    int i,count=0;
    i=chek(s,0);
    if(i==s.length())
        return 0;
    else if(i>s.length()-n)
        {
            return -1;
        }
    else
    {
        int x;
        while(i<=s.length()-n)
        {
            int k = i;
            for(int j=0;j<n;j++)
            {
                if(s.at(k)=='+')
                    s.at(k)='-';
                else if(s.at(k)=='-')
                    s.at(k)='+';
                k++;
            }
            count++;
            x=s1.compare(s);
            if(x==0)
                break;
            else if(x==0&&i>s.length()-n)
            {
                return -1;
            }
            i=chek(s,i+1);
        }
        x=s1.compare(s);
        if(x==0&&i<=(s.length()-n))
            return count;
        else
            return -1;
    }
}

int main()
{
    int no_tcase;
    freopen( "A-large.in", "r", stdin );
	freopen( "output.txt", "w", stdout );

    cin>>no_tcase;

    for(unsigned int i=1;i<=no_tcase;i++)
    {
        string in_case;
        int npancakes;
        cin>>in_case>>npancakes;
        int a=check(in_case,npancakes);
        if(a!=-1)
        {
            cout<<"Case #"<<i<<": "<<a<<endl;
        }
        else
            cout<<"Case #"<<i<<": IMPOSSIBLE"<<endl;

    }

return 0;

}
