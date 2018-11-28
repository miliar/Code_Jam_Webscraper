#include <iostream>
#include <math.h>
#include <vector>
#include <algorithm>
#include <functional>
using namespace std;

int main(){
    int t;cin>>t;int caseno=1;
    while(t--){
        int n,k;cin>>n>>k;
        vector<int> sizes;
        sizes.push_back(n);//cout<<sizes.size()<<endl;
        int curr=0;
        int ss=sizes.size();
        while(curr<ss){
            if(sizes[curr]!=1){
            if(sizes[curr]==2){
                sizes.push_back(1);
            }
            else if(sizes[curr]%2==0){
                sizes.push_back(sizes[curr]/2);
                sizes.push_back(sizes[curr]/2-1);
            }
            else{
                sizes.push_back(sizes[curr]/2);
                sizes.push_back(sizes[curr]/2);
            }
            }
            ss=sizes.size();
            curr++;//cout<<sizes.size()<<endl;
        }
        
        sort(sizes.begin(),sizes.end(),greater<int>());
        
        int maxlargest=sizes[k-1];
        int ans=maxlargest/2;
        int ans1=0;if(ans!=0)ans1=ans-1;
        if(maxlargest%2==0){
            cout<<"Case #"<<caseno<<": "<<ans<<" "<<ans1<<endl;
        }
        else{
            cout<<"Case #"<<caseno<<": "<<ans<<" "<<ans<<endl;
        }
        
        caseno++;
    }
}
