#include<bits/stdc++.h>
using namespace std;

struct compare{
    bool operator()(const long long int &l, const long long int &r){
        return l<r;
    }
};

int main(){
    int t,T;
    long long int i,j;
    long long int x,y,z,n,k,count;

    cin>>T;
    t=1;
    while(t<=T){
        cin>>n>>k; 
        count=0; 

        //max priority queue
        priority_queue<long long int,vector<long long int>, compare> pq;
        unordered_map<long long int, long long int> mp;
        pq.push(n);
        mp[n]=1;
        
        while(count<k){
            x=pq.top();
            pq.pop();
            y=mp[x];
            count+=y;
            //mp[x]=0;
            
            i=(x-1)/2;
            j=(x)/2;

            if(i>0){
                if(mp.find(i)==mp.end()){
                    //add i
                    pq.push(i);
                    mp[i]=y;
                } else {
                    mp[i]+=y;
                }
            }

            if(j>0){
                if(mp.find(j)==mp.end()){
                    //add j
                    pq.push(j);
                    mp[j]=y;
                } else {
                    mp[j]+=y;
                }
            }
        }
         
        cout<<"Case #"<<t<<": ";
        //output here
        cout<<j<<" "<<i; 
        cout<<endl;

        t++;
    }

    return 0;
}
