#include<bits/stdc++.h>
#define PI 3.14159265359

using namespace std;
int n,k;
double mxsum=0;
double csum=0;
double mxrad=0;
vector<pair<int,int> > arr;

void solve(int i,int c){
    if(c==k||i==n){
        mxsum=max(mxsum,csum);
        return;
    }
    double r1 = arr[i].first,h1=arr[i].second;
    double s=(2*r1*PI*h1);
    s+=max((double)0,(PI*r1*r1)-(PI*mxrad*mxrad));
    int lcmx=mxrad;
    solve(i+1,c);
    csum+=s;
    mxrad=max(mxrad,r1);
    solve(i+1,c+1);
    mxrad=lcmx;
    csum-=s;
}

int main(){
   // freopen("A-small-attempt3.in","r",stdin);
    //freopen("ample1.txt","w",stdout);
    int T;
    cin>>T;
    for(int O=0;O<T;O++){
        mxsum=0;
        csum=0;
        mxrad=0;
        arr.clear();
        cin>>n>>k;
       for(int i=0;i<n;i++){
        int r,h;
        cin>>r>>h;
        arr.push_back(make_pair(r,h));
       }
       solve(0,0);
        cout<<fixed<<setprecision(8)<<"Case #"<<O+1<<": "<<mxsum<<endl;
    }
}
