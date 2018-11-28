#include<bits/stdc++.h>
using namespace std;
int main()
{//freopen("C-small-2-attempt1.in","r",stdin);
//freopen("xxx.txt","w",stdout);
    int n;

cin>>n;
//cout<<n;
for(int xx=1;xx<=n;xx++)
{int no,k,ans1,ans2,first,last,mid;
cin>>no>>k;
//cout<<no<<" "<<k<<" ";
    priority_queue<pair< int,pair<int,int> > > q;
    q.push(make_pair(no+1,make_pair(0,no+1)));
    ans2=no/2;
    while(k--)
    {
        first=q.top().second.first;
        last=q.top().second.second;
        mid=(first+last)/2;

    //cout<<first<<" "<<mid<<" "<<last<<" ans1 "<<ans1<<"\n";

        q.push(make_pair(last-mid,make_pair(mid,last)));
        q.push(make_pair(mid-first,make_pair(first,mid)));
        ans2=min((mid-first)-1,(last-mid)-1);
        ans1=max((mid-first)-1,(last-mid)-1);;
        q.pop();



}
cout<<"Case #"<<xx<<": "<<ans1<<" "<<ans2<<endl;
}
}
