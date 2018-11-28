
#include <iostream>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <list>
#include <cstring>
#include <math.h>

using namespace std;

typedef long long int lli;
typedef unsigned long long int ulli;
typedef long double ld;

int main() {

    int t;
    cin >> t;

    for(int num=0;num<t;num++)
    {
        string s,out="";
        cin >> s;

        int flag=0,index=0;
        int len = s.size();
        for(int i=1;i<len;i++)
        {
            if(s[i]<s[i-1])
            {
                index=i;
                flag=1;
                break;
            }
        }

        if(flag==0) out=s;
        else
        {
            for(int i=index;i<len;i++)
                s[i]='9';

            if(s[index-1]!='1')
            {
                index--;
                int myflag=0;
                while(index>0)
                {
                    if(s[index-1]==s[index]) s[index]='9';
                    else
                    {
                         int m=s[index]-48;
                         s[index]=m+47;
                         myflag=1;
                         break;
                    }
                    index--;
                }
                if(myflag==0)
                {
                    int m=s[index]-48;
                    s[index]=m+47;
                }
                out=s;
            }
            else
            {
                index--;
                while(index)
                {
                    s[index]='9';
                    index--;
                }
                s[index]='0';

                for(int i=1;i<len;i++)
                    out+=s[i];

            }
        }

        cout << "Case #" << num+1 << ": " <<  out << endl;

    }

    return 0;
}


