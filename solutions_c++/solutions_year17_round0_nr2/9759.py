#include <iostream>
#include <string.h>
using namespace std;

void tidy(string );
int check(string s3)
{
    unsigned int b;
    int c = 0;
    for(b=0 ; b<(s3.length()-1) ; b++)
    {
        if(s3[b]<=s3[b+1])
        {
            continue;
        }
        if(s3[b]>s3[b+1])
        {
            tidy(s3);
            c=1;
        }
    }
    return c;
}

void tidy(string s2)
{
    unsigned int a,b,j;
    for(a=0 ; a<(s2.length()-1);a++)
    {
        if(s2[a]>s2[a+1])
        {
            s2[a]= s2[a]-1;
            break;
        }
    }
    for( j =a+1 ; j<s2.length(); j++)
    {
        s2[j]='9';
    }
    int n=check(s2);
    if(n==0)
    {
        b=0;
        if(s2[b]!='0')
        {
            cout<< s2[b];
        }
        for(b=1 ; b<=j ; b++)
        {
            cout << s2[b];
        }
    }
}

int main()
{
    string s1;
    int T, i;
    cin >> T;
    for(i=1; i<=T ; i++)
    {
        cin >> s1;
        cout<<"case #"<<i<<": ";
        tidy(s1);
        cout<<endl;
    }
    return 0;
}