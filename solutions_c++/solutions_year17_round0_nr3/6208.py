#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    int t;
    int l,r;
    int val=0;
    string str;
    int case_no=0;
    cin>>t;
    while(t--){
        ++case_no;
        int n,k,temp,left,right,ctr;
        cin>>n>>k;
        priority_queue < int > pq;
        pq.push(n);
        for(int i=1;i<=k;i++){
            temp=pq.top();
            if(i==k){
                break;
            }
            pq.pop();
            ctr=(temp+1)/2;
            right=temp-ctr;
            left=ctr-1;
            pq.push(left);
            pq.push(right);
        }
        ctr=(temp+1)/2;
        int max_=max(temp-ctr,ctr-1);
        int min_=min(temp-ctr,ctr-1);
        cout<<"Case #"<<case_no<<": "<<max_<<" "<<min_;
        // cout<<str<<":";
        
        cout<<"\n";
        
    }
    return 0;
}

