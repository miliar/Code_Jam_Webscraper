#include<bits/stdc++.h>
using namespace std;

vector<unsigned long> A;


void printA(){

    for(int i=0; i<A.size(); i++)
        cout<<A[i]<<" ";
    cout<<endl<<endl;
}


int main(){

    FILE *in = freopen("C-small-1-attempt0.in", "r", stdin);
    FILE *out = freopen("C-small-1.out", "w", stdout);

    int T;
    cin>>T;
    for(int i=1; i<=T; i++){

        unsigned long N,L,R;
        cin>>N;
        int K;
        cin>>K;
        A.clear();
        A.push_back(N);
        while(K--){
            int l = A.size() - 1;
            if(A.size() > 0)
                sort(A.begin(), A.end());
            if(A[l] == 0){
                L = R = 0;
                break;
            }
            unsigned long B = A[l]/2;
            L = R = B;
            A.pop_back();
            if((B * 2) == A[l]){
                A.push_back((B-1));
                A.push_back(B);
                R = B-1;
            }
            else{
                A.push_back(B);
                A.push_back(B);
            }
        //    printA();
        }
    sort(A.begin(), A.end());

    cout<<"Case #"<<i<<": "<<L<<" "<<R<<endl;

    }


    return 0;
}
