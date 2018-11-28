#include<bits/stdc++.h>
using namespace std;
int main()
{
    ifstream cin("input.in");
    ofstream cout("output.out");
    ios::sync_with_stdio(0);cin.tie(0);
    long T,t=1;
    cin>>T;
    while(t<=T)
    {
        long long N,K,B,E;
        cin>>N>>K;
        set<long long> S;
        S.insert(0);
        S.insert(N+1);
        while(K--)
        {
            set<long long>::iterator it;
            set<long long>::iterator jt;
            long long M=0;
            for(it=S.begin();it!=S.end();it++)
            {
                jt=it;
                jt++;
                if(((*jt) - (*it)) >M && jt!=S.end())
                {
                    B=*it;
                    E=*jt;
                    M=(E-B);
                }
            }
            S.insert((E+B)/2);
        }
        //for(set<long long>::iterator it=S.begin();it!=S.end();it++)
          //  cout<<*it<<" ";
        //cout<<B<<" "<<E<<"\n";
        long long M=(B+E)/2;
        cout<<"Case #"<<t<<": "<<max(M-B,E-M)-1<<" "<<min(M-B,E-M)-1<<"\n";
        t++;
    }
    return 0;
}