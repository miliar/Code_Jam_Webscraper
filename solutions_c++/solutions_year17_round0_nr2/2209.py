#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
    int T;
    cin>>T;
    for(int t=1;t<=T;t++){
        string S;
        cin>>S;
        vector<int> N;
        for(auto c:S){
            N.push_back(c-'0');
        }
        for(int i=N.size()-1;i>0;i--){
            if(N[i-1]<=N[i]) continue;
            else{
                N[i-1]--;
                for(int j=i;j<N.size();j++) N[j]=9;
                if(i-1==0&&N[i-1]==0) N.erase(N.begin());
                i=N.size();
            }
        }
        cout<<"Case #"<<t<<": ";
        int i=0;
        while(N[i]==0)i++;
        while(i<N.size())cout<<N[i++];
        cout<<endl;
    }


    return 0;
}