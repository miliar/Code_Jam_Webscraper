#include <bits/stdc++.h>
using namespace std;

int T,D,N;
int horse[1001][2];
float Max=0;

int main() {
    cin>>T;
    float H;
    for(int t=1;t<=T;t++){
        cin>>D>>N;
        Max=0.0f;

        for(int n=1;n<=N;n++){
            cin>>horse[n][0]>>horse[n][1];
            H = float(D-horse[n][0])/horse[n][1];
            //cout<<float(D/H)<<endl;
            //cout<<float(D/H)<<endl;
           // cout<<"n="<< n<<endl;
            //cout<<H<<endl;

            if(H!=0)
                Max = Max > H ?  Max : H;

        }
        cout<<"Case #"<<t<<": ";
       // cout<<Max<<endl;
        printf("%f\n",(float)D/Max);
    }

    return 0;
}
