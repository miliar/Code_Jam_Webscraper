#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
    int t;
    scanf("%d", &t);

    string s,s1;
    int siz;
    int index;

    for(int l=0;l<t;l++)
    {
        cin>>s;

        siz = s.size();

        index = -1;

        for(int i=1;i<siz;i++)
        {
            if(s[i]<s[i-1])
            {
                index = i;
                break;
            }
        }
        //


        if(index>=0)
        {
            //
            for(int i=index;i<siz;i++)
            {
                s[i] = '9';
            }
            //
            index--;
            s[index]--;
            for(int i=index-1;i>=0;i--)
            {
                if(s[i]>s[i+1])
                {
                    s[i+1] = '9';
                    s[i]--;
                }

            }
            //
        }

        if(s[0]=='0')
        {
            cout<<"Case #"<<l+1<<": "<<s.substr(1, siz-1)<<endl;
        }
        else
        {
            cout<<"Case #"<<l+1<<": "<<s<<endl;
        }
    }
}
