#include <iostream>
#include <algorithm>
#include <vector>
#include <cstring>
#include <fstream>
using namespace std;

int T;
char S[105];

int main()
{
    ifstream fin("B-large.in");
    ofstream fout("Answer.out");
    cin.rdbuf(fin.rdbuf());
    cout.rdbuf(fout.rdbuf());
    cin>>T;
    for (int cases=1; cases<=T; cases++)
    {
        memset(S,0,sizeof(S));
        cin>>S;
        int len=strlen(S);
        bool flag=true;
        int mark;
        for (int i=1; i<len; i++)
            if (S[i]<S[i-1])
            {
                flag=false;
                mark=i-1;
                break;
            }
        if (flag)
        {
            cout<<"Case #"<<cases<<": "<<S<<endl;
            continue;
        }
        for (int i=mark;i>=0;i--)
            if (i==mark)
                S[i]-=1;
            else if (S[i]>S[i+1])
                S[i]-=1,S[i+1]='9';
        for (int i=mark+1;i<len;i++)
            S[i]='9';
        cout<<"Case #"<<cases<<": ";
        flag=true;
        for (int i=0;i<len;i++)
        {
            if (flag&&S[i]=='0') continue;
            flag=false;
            cout<<S[i];
        }
        cout<<endl;
    }
    return 0;
}
