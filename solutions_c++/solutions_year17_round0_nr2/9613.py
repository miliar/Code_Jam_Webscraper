#include<bits/stdc++.h>

using namespace std;

int main()
{
    ifstream fin("B-large.in");
    ofstream fout("out.in");
    int t;
    fin>>t;
    for(int p=1;p<=t;p++)
    {
        char ch[18];
        fin>>ch;

        char prev=0;
        bool flag=true;
        for(int i=1;i<strlen(ch);i++,prev++)
        {
            if(ch[i]<ch[prev])
            {
                ch[prev]=ch[prev]-1;
                for(int j=prev+1;j<strlen(ch);j++)
                {
                    ch[j]='9';
                }
		prev-=2;i-=2;
		continue;
            }
        }
        bool zero_vanished=false;
        fout<<"Case #"<<p<<": ";
        for(int i=0;i<strlen(ch);i++)
        {
            if(ch[i]!='0')
                zero_vanished=true;
            if(zero_vanished)
                fout<<ch[i];
        }
        fout<<endl;
    }
    fout.close();
    fin.close();
    return 0;
}
