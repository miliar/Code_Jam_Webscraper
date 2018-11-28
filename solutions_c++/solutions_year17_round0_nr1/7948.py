#include <bits/stdc++.h>
using namespace std;
int main()
{
    ifstream in("A-large.in");
    ofstream out("out.out");
    int T;
    in>>T;
    for(int t=1;t<=T;t++)
    {
        string s;
        in>>s;
        int K;
        in>>K;
        int counter =0;
        int N = s.size();
        for(int i=0;i<=N-K;i++)
            if(s[i]=='-'){
                 for(int j=0;j<K;j++)
                    if(s[i+j]=='-') s[i+j]='+';
                        else s[i+j]='-';
                counter++;
            }

       out<<"Case #"<<t<<": ";
       bool impossible = false;
       for(int i=0;i<N;i++)
        if(s[i]=='-') {
                out<<"IMPOSSIBLE\n";
                impossible = true;
                break;
        }
        if(!impossible) out<<counter<<"\n";


    }
}
