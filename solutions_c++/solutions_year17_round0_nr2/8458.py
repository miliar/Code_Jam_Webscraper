#include<bits/stdc++.h>
using namespace std;

vector<string> A();


int main(){

    FILE *in = freopen("B-small-attempt0.in", "r", stdin);
    FILE *out = freopen("A-large.out", "w", stdout);

    int T;
    cin>>T;
    for(int i=1; i<=T; i++){

        int N;
        cin>>N;
        string S;

        while(N){
            stringstream ss;
            ss<<N;
            S = ss.str();
            string R = S;
            sort(S.begin(),S.end());
            if(R == S){
                cout<<"Case #"<<i<<": "<<S<<endl;
                break;
            }
            N--;
        }
    }

    return 0;
}
