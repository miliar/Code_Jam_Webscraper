#include<iostream>
#include<cstring>
#include<string>
#include <fstream>

using namespace std;
int l;
string s;

void last(int pos)
{
    if (pos<0|| pos==l-1) return;
    if (s[pos]> s[pos+1] )
    {
        s[pos]--;
        for (int i=pos+1;i<l;i++)
            s[i]='9';
        last(pos-1);
    }
    else last(pos+1);
}

int main()
{
//    ofstream cout ("output.txt");
//    ifstream cin ("B-large.in");
    int tc,caseno=0;

    cin>>tc;
    while (tc--)
    {
        cin>>s;
        l=s.length();
        cout<<"Case #"<<++caseno<<": ";
        if (l==1)
        {
            cout<<s[0]<<endl;
            continue;
        }
        last(0);
        if (s[0]=='0')
        {
            for (int i=1;i<l;i++)
                cout<<"9";
            cout<<endl;
        }
        else
        {
            cout<<s<<endl;
        }

    }
    return 0;
}
