#include<iostream>
#include<vector>
using namespace std;
int main(){
    int t;
    cin>>t;
    int cas=0;
    while(t--){
        long long n;
        cin>>n;
        vector<int> dig;
        while(n){
            dig.push_back(n%10);
            n/=10;
        }

        if(dig.empty()){
            dig.push_back(0);
        }

        long long ans=0;
        for(int i=0;i<dig.size()-1;i++){
            if(dig[i]<dig[i+1]){
                dig[i+1]--;
                for(int j=i;j>=0;j--){
                    dig[j]=9;
                }
            }
        }
        for(int i=dig.size()-1;i>=0;i--){
            ans*=10;
            ans+=dig[i];
        }

        cout<<"Case #"<<++cas<<": "<<ans<<endl;
    }
}
