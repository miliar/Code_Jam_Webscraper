#include <bits/stdc++.h>
using namespace std;
int main()
{
    int T,i,j,k,K;
    string s;
    cin >>T;
    ofstream fout;
    fout.open("Code.txt");
    int c=1;
    while(T--)
    {
        cin >>s;
        int len=s.length();

        int pos=-1;
        for(i=0;i<len-1;i++)
        {
            if(s[i]>s[i+1])
                {   pos=i;
                    for(j=pos-1;j>=0;)
                        if(s[j]==s[i])
                        j--;
                        else
                        break;
                    pos=j+1;
                    break;
                }
        }
        if(pos!=-1)
        {
            s[pos]=s[pos]-1;
            for(i=pos+1;i<len;i++)
                s[i]='9';
            for(i=0;i<len;i++)
                if(s[i]!='0')
            {
                pos=i;
                break;
            }
        }
        else
        pos=0;
        fout <<"Case #"<<c<<": ";
        for(i=pos;i<len;i++)
            fout<<s[i];
        fout<<endl;
        c++;

    }

    return 0;

}
