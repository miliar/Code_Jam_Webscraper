#include<bits/stdc++.h>
using namespace std;
bool F(long i)
{
    return (i%10)>(i/10) || i==0;
}
string check(char A,char B)
{
    long N=(A-48);
    N*=10;
    N+=(B-48);
    while(F(N)==0)
        N--;
    string P="  ";
    P[0]=char(N/10+48);
    P[1]=char(N%10+48);
    return P;
}
int main()
{
    ifstream cin("input.in");
    ofstream cout("output.out");
    ios::sync_with_stdio(0);cin.tie(0);
    long T,t=1;
    cin>>T;
    while(t<=T)
    {
        string S;
        cin>>S;
        long L=S.size();
        long i=L-2;
        while(i>=0)
        {
            if(S[i+1]<S[i])
            {
                string P=check(S[i],S[i+1]);
                S[i]=P[0];
                S[i+1]=P[1];
                for(long j=i+2;j<L;j++)
                    S[j]='9';
                //cout<<S<<"\n";
            }
            i--;
        }
        if(S[0]=='0')
            S=S.substr(1,S.size());
        cout<<"Case #"<<t<<": "<<S<<"\n";
        t++;
    }
    return 0;
}