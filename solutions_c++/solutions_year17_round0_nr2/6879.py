#include <iostream>
#include <cstring>
#include <cstdio>
#include <climits>
#define lli long long int
using namespace std;

int valueOf(char);
int decrement(char);
void check(int);
string s;
int main()
{
    lli t,j;
    freopen("in_new.in","r",stdin);
    freopen("ans4.txt","w",stdout);
    cin>>t;
    for(lli i = 1 ; i <= t; ++i)
    {
        cin>>s;
        for( j = 0 ; j < s.length()-1; ++j)
        {
            if(valueOf(s.at(j)) > valueOf(s.at(j+1)))
            {
                s.at(j) = decrement(s.at(j));
                s.at(j+1) = '9';
                check(j);
                break;
            }
        }
        for(lli p = j+1 ; p <s.length() ; ++p)
        {
            s.at(p) = '9';
        }
        cout<<"Case #"<<i<<": ";
        if(s.at(0) == '0')
        {
            for(int p = 1; p < s.length(); ++p)
            {
                cout<<s.at(p);
            }
            cout<<endl;
        }else{
        cout<<s<<endl;}
    }


    return 0;
}

int valueOf(char ch)
{
    return ch-'0';
}

int decrement(char ch)
{

    switch(ch)
    {
    case '1':
        return '0';
    case '2':
        return '1';
    case '3':
        return '2';
    case '4':
        return '3';
    case '5':
        return '4';
    case '6':
        return '5';
    case '7':
        return '6';
    case '8':
        return '7';
    case '9':
        return '8';
    }
    return 0;
}

void check(int k)
{
    if(k == 0){return;}

        if(s.at(k) < s.at(k-1))
        {
            s.at(k) = '9';
            s.at(k-1) = decrement(s.at(k-1));
            check(k-1);
        }

}
