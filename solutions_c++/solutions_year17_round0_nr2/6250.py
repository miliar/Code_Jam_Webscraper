#include<bits/stdc++.h>

#define ull unsigned long long int
using namespace std;

int main(){
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    ull T,N;
    cin>>T;
    for(int z=1;z<=T;z++){
        cin>>N;
        cout<<"Case #"<<z<<": ";
        if(N%10==0)
            N-=1;
        vector<char> V;
        while(N){
            V.push_back(N%10 + '0');
            N/=10;
        }
        reverse(V.begin(), V.end());

        if(V.size()==1){
            cout<<V[0]<<"\n";
            V.clear();
            continue;
        }
        int i=0;
        while(i+1<V.size()){
            if(V[i]<=V[i+1]){
                i+=1;
            }
            else{
                break;
            }
        }
        if(i+1==V.size()){
            for(int j=0;j<V.size();j++){
                cout<<V[j];
            }
            cout<<"\n";
        }
        else{
            while(i-1>=0 && V[i]==V[i-1])
                i-=1;
            V[i]=char(V[i]-1);
            for(int j=i+1;j<V.size();j++){
                V[j] = '9';
            }
            for(int j=0;j<V.size();j++){
                if(V[j]!='0')
                cout<<V[j];
            }
            cout<<"\n";
        }

        V.clear();
    }


    return 0;
}
