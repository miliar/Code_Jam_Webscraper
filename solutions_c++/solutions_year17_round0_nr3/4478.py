#include<bits/stdc++.h>
using namespace std;
// v[2000010];
bool comp(int a , int b){
    return b<a;
}
int main()
{
    freopen("C-small-2-attempt2.out","w",stdout);
    freopen("C-small-2-attempt2.in","r",stdin);
    int tc,t=0;
    cin>>tc;
    while(t<tc){
        t++;
        int n,k;
        cin>>n>>k;

        priority_queue<int>v;
        //for(int i=0;i<100010;i++)v[i]=0;
        v.push(n);
        int j=0;
        int l=0,r,p,q;
        for(int i=1;i<=k;i++){
            //sort(v,v+j+1,comp);
            p=(v.top()-1)/2;
            q=(v.top()-1)/2;
            if((v.top()-1)%2!=0)
                p++;
            //cout<<v.top()<<endl;
            v.pop();
            v.push(p);
            v.push(q);

        }
        //for(int x=0;x<j;x++)cout<<v[x]<<" ";

        printf("Case #%d: ",t);
        cout<<max(p,q)<<" "<<min(p,q)<<endl;
    }

    return 0;
}

