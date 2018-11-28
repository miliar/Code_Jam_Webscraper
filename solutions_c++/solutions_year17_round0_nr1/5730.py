#include <iostream>
#include <fstream>
#include <string>

using namespace std;

bool finalCheck(string str,int k)
{
    int l = str.length();
    for(int j=l-1; j>= l-k;j--)
        if(str[j]=='-')
            return false;
    return true;
}

string change(string str,int i, int k)
{
    for(int j= i;j < (i + k);j++)
    {
        if(str[j]=='-')
            str[j] = '+';
        else
            str[j] = '-';
    }
                //cout<<str<<endl;
    return str;
}

int minMove(string str, int k)
{
    int move = 0;
    int maxIndx = str.length() - k;

   // cout<<str<<endl;

    for(int i=0;i<=maxIndx;i++)
    {
        if(str[i] == '-')
        {
            str = change(str,i,k);
           // cout<<str<<endl;
            move++;
        }
    }
    if(!finalCheck(str, k))
        return -1;

    return move;
}

int main()
{
    ifstream in("A-large.in");
    ofstream out("A-large.out");

    int T;
    in>>T;

    for(int i=0;i<T;i++)
    {
        string input;
        in>>input;
        //cout<<input;
        int k;
        in>>k;
        //cout<<k<<endl;
       // cout<<v;
       int m = minMove(input,k);

        out<<"Case #"<<i+1<<": ";

        if( m == -1)
            out<<"IMPOSSIBLE";
        else
            out<<m;

        //cout<<"m = "<<m<<endl<<endl;

        if(i != T-1)
            out<<endl;
    }

    out.close();
    return 0;
}
