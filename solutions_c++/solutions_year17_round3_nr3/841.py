#include<bits/stdc++.h>

using namespace std;

typedef long long ll;

void _main()
{
    int N,K;
    cin>>N>>K;
    double U;
    cin>>U;
    double prob[N];
    for(int i=0;i<N;i++)
        cin>>prob[i];
    sort(prob,prob+N);
    int same=0;
    while(U>0){
        while(same<N-1&&prob[same]==prob[same+1])same++;
        if(same==N-1){
            for(int i=0;i<N;i++)
                prob[i]+=U/N;
            U=0;
        }
        else{
            double need=prob[same+1]-prob[same];
            double give=0;
            if(U>need*(same+1)){
                give=need;
                U-=need*(same+1);
            }else{
                give=U/(same+1);
                U=0;
            }
            for(int i=0;i<=same;i++)
                prob[i]+=give;
        }
    }
    double ans=1;
    for(int i=0;i<N;i++)
        ans*=prob[i];
    cout<<ans;
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

