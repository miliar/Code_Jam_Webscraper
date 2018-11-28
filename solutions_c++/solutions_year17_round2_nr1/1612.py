#include<bits/stdc++.h>
using namespace std;
int main()
{
    ifstream cin("input.in");
    ofstream cout("output.out");
    ios::sync_with_stdio(0);cin.tie(0);
    long T,t=1;
    cin>>T;
    while(t<=T){
        long K;
        double N,A,B,Z,Q,L;
        cin>>N>>K>>Z>>Q;
        L=(N-Z)/Q;
        K--;
        while(K--){
            cin>>A>>B;
            if((N-A)/B>L)
            {
                Z=A;
                Q=B;
                L=((N-A)/B);
            }
        }   
        cout<<fixed;
        cout<<setprecision(6);
        //cout<<Z<<" "<<Q<<"\n";
        cout<<"Case #"<<t<<": "<<double(N/L)<<"\n";
        t++;
    }
}