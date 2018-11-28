#include<bits/stdc++.h>
using namespace std;

int main()
{
    freopen("B-large.in.txt","r",stdin);
    freopen("outBL.txt","w",stdout);

    long long int T;
    string S;

    cin>>T;

    for(long long int I=1; I<=T; I++)
    {
        cin>>S;
        if(S.size()==1)
        {
            cout<<"Case #"<<I<<": "<<S<<endl;
            continue ;
        }
        int L=S.size();

        while(L--)
        {
            for(int J=0; J<S.size()-1; J++)
            {
                if(S[J]>S[J+1])
                {
                    S[J]=S[J]-1;
                    for(int K=J+1; K<S.size(); K++)
                    {
                        S[K]='9';
                    }
                    break;
                }
            }
        }
        if(S[0]=='0')
        {
            cout<<"Case #"<<I<<": ";
            for(int J=1; J<S.size(); J++)
            {
                cout<<S[J];
            }
            cout<<endl;
        }
        else
        {
            cout<<"Case #"<<I<<": "<<S<<endl;
        }
    }
    return 0;
}
