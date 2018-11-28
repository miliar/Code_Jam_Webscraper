#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t,i,j,k,flg=0;
    string str="";
    ifstream fin ("C:\\Users\\ADMIN\\Desktop\\CodeJam17\\input.txt");
    ofstream fout ("C:\\Users\\ADMIN\\Desktop\\CodeJam17\\sol.txt");

    fin>>t;

    for(j=1;j<=t;j++)
    {
        flg=0;
        fin>>str;

        for(i=1;str[i]!='\0';)
        {
            if(str[i]>=str[i-1])
            {
                i++;
            }
            else
            {
                i--;
                str[i]=(char)(str[i]-1);
                break;
            }
        }
        if(str[i]=='\0'){
                fout<<"Case #"<<j<<": "<<str<<"\n";
            continue;
        }
        for(;i>=1;)
        {
            if(str[i]>=str[i-1])
            {
                break;
            }
            else
            {
                i--;
                str[i]=(char)(str[i]-1);
            }
        }
        fout<<"Case #"<<j<<": ";
        for(k=0;k<=i;k++)
        {
            if(!flg&&str[k]=='0')
                continue;
            flg=1;
            fout<<str[k];
        }
        for(k=i+1;str[k]!='\0';k++)
        {
            fout<<"9";
        }
        fout<<"\n";


    }

    return 0;
}
