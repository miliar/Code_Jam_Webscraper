#include<bits/stdc++.h>
#define llt long long int
using namespace std;

int main()
{
    llt t,n,k,tt=1,p=1,tmp;
    cin>>t;
    vector <llt> a;
    for(llt i=1; i<=1e18; i+=pow(2,p++)) a.push_back(i);
    while(tt<=t)
    {
        cin>>n>>k;
        cout<<"Case #"<<tt<<": ";
        priority_queue <llt> Q;
        Q.push(n);
        for(int i=1; i<k; i++)
        { tmp=Q.top();
          Q.pop();
          if(tmp%2==0) Q.push(tmp/2),Q.push(tmp/2-1);
          else Q.push(tmp/2),Q.push(tmp/2);
        }
        if(Q.top()%2==0) cout<<Q.top()/2<<" "<<Q.top()/2-1;
        else cout<<Q.top()/2<<" "<<Q.top()/2;
        cout<<endl;
        tt++;
    }
    return 0;
}
