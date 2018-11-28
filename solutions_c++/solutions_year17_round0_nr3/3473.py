#include<cstdio>
#include<iostream>
#include<queue>
#include<cstdlib>
#include<cstring>
using namespace std;
long long t;
int main(){
    cin>>t;
    for(int i=1;i<=t;i++){
        priority_queue<long long> q;
        long long n,k,a,b,temp;
        cin>>n>>k;
        q.push(n);
        for(long long i=0;i<k;i++){
            temp=q.top();
            q.pop();
            if(temp%2==0){
                a=temp/2-1;
                b=temp/2;
                q.push(a);
                q.push(b);
            }else if(temp%2==1){
                a=b=(temp-1)/2;
                q.push(a);
                q.push(b);
            }
        }
        cout<<"Case #"<<i<<": "<<b<<" "<<a<<endl;
    }
    return 0;
}
