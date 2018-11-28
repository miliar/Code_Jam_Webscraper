#include<iostream>
#include<cmath>
#include<vector>
#include<algorithm>
using namespace std;
void push(pair<int,int> a);
pair<int,int>pop();
void sortQue();
void del();
pair<int,int> evalAns(int n,int k);


int main()
{
    int test;
    cin>>test;
    for(int t=1;t<=test;t++)
    {
        int n,k;
        cin>>n>>k;
        pair<int,int> ans=evalAns(n,k);
        cout<<"Case #"<<t<<": "<<ans.first<<" "<<ans.second<<endl;
    }
    return 0;
}

pair<int,int> evalAns(int n,int k)
{
    int cur=0;
    int l=0;
    int h=n-1;
    int mid=(l+h)/2;
    del();
    push(make_pair(l,h));
    push(make_pair(-1,-1));
    while(cur<k){
        pair<int,int> popped=pop();
        if(popped.first==-1&&popped.second==-1)
        {
            sortQue();
            push(make_pair(-1,-1));
            continue;
        }
        l=popped.first; h=popped.second;
        mid=(popped.first+popped.second)/2;

        if(popped.first<=mid-1)
            push(make_pair(popped.first,mid-1));
        if(mid+1<=popped.second)
            push(make_pair(mid+1,popped.second));
        cur+=1;
    }
    return make_pair(max(mid-l,h-mid),min(mid-l,h-mid));
}

vector<pair<int,int> >arr;
void push(pair<int,int> a) {
    arr.push_back(a);
}
pair<int,int>pop()
{
    pair<int,int> res=arr[0];
    arr.erase(arr.begin());
    //cout<<res.first<<" "<<res.second<<endl;
    return res;
}
bool func(pair<int,int>a,pair<int,int>b){
    return abs(a.first-a.second)>abs(b.first-b.second);
}
void sortQue(){
    sort(arr.begin(),arr.end(),func);
}
void del(){
    arr.clear();
}
