#include<bits/stdc++.h>
using namespace std;

#define l long long
#define ld long double
#define pb push_back
#define mod 10000007
#define ii pair<int,int>
#define jj pair<ii,ii>

int main(){

    freopen("input.txt","r",stdin);
    freopen("output1.txt","w",stdout);
    int t;cin>>t;

    for(int ix=1;ix<=t;ix++){

        printf("Case #%d: ",ix);
        l n,k;cin>>n>>k;

        priority_queue<l>pq;
        map<l,l>mark;

        mark[n]=1;
        pq.push(n);

        while(true){
            l u=pq.top();
            pq.pop();
            l v=mark[u];
            mark[u]=0;
            //cout<<u<<" "<<v<<endl;
            l val1,val2;
            if(u%2==0){
                val1=u/2;
                val2=u/2;
                val2--;
            }
            else{
                val1=u/2;
                val2=u/2;
            }

            if(k<=v){
                cout<<max(val1,val2)<<" "<<min(val1,val2)<<endl;
                break;
            }
            else{
                k-=v;
                if(u%2==0){
                    if(val1){
                        if(mark[val1]==0)
                            pq.push(val1);
                        mark[val1]+=v;
                    }
                    if(val2){
                        if(mark[val2]==0)
                            pq.push(val2);
                        mark[val2]+=v;
                    }

                }
                else{
                    if(val1){
                        if(mark[val1]==0)
                            pq.push(val1);
                        mark[val1]+=2*v;
                    }
                }
            }
        }
    }
}
