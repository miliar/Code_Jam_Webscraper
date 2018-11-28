#include<bits/stdc++.h>

using namespace std;

typedef long long ll;

void _main()
{
    int Ac,Aj;
    cin>>Ac>>Aj;
    pair<int,int> ct[4],jt[4];
    for(int i=0;i<Ac;i++)
        cin>>ct[i].first>>ct[i].second;
    for(int i=0;i<Aj;i++)
        cin>>jt[i].first>>jt[i].second;
    if(Ac==1||Aj==1){
        cout<<2;
    }else
    {
        if(Ac==2){
            sort(ct,ct+2);
            if(ct[1].first-ct[0].second+ct[0].second-ct[0].first+ct[1].second-ct[1].first<=720)
                cout<<2;
            else if(ct[0].first+1440-ct[1].second+ct[0].second-ct[0].first+ct[1].second-ct[1].first<=720)
                cout<<2;
            else
                cout<<4;
        }else{
            sort(jt,jt+2);
            if(jt[1].first-jt[0].second+jt[0].second-jt[0].first+jt[1].second-jt[1].first<=720)
                cout<<2;
            else if(jt[0].first+1440-jt[1].second+jt[0].second-jt[0].first+jt[1].second-jt[1].first<=720)
                cout<<2;
            else
                cout<<4;
        }
    }

}

int main()
{
    int T;
    cin>>T;
    for(int t=1;t<=T;t++)
    {
        cout<<"Case #"<<t<<": ";
        _main();
        cout<<endl;
    }
}

