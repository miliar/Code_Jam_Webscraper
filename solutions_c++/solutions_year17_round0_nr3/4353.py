#include <iostream>
#include<vector>
#include<sstream>
#include<algorithm>
#include<queue>
using namespace std;

int main(){
    int t;
    cin>>t;
    long long int n,k;
    int c=1,h=1;
    while (t--){
        cin>>n>>k;
        priority_queue<long long int>v;
        long long int max=0,min=0;
        v.push(n);
        for (long long int i=0; i<k; i++){
            int s=v.top();
            v.pop();
            if(s%2==1){
                s=s/2;
                max=min=s;
                v.push(max);
                v.push(min);
            }
            else{
                s=s/2;
                max=s;
                min=s-1;
                v.push(max);
                v.push(min);
            }
            //sort(v.begin(),v.end(),greater<long long int>());
        }
        cout<<"Case #"<<c<<": "<<max<<" "<<min<<endl;
        c++;

    }
    
}
