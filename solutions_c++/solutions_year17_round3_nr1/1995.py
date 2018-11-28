#include <bits/stdc++.h>
#define ll long long int

using namespace std;

double pi=2*acos(0.0);

int n,k;

pair<int,int> arr[1005];

struct cake{
    ll r,h;

    cake(){
    }
    cake(ll a, ll b){
        r=a;
        h=b;
    }

    bool operator<(const cake& a)const{
        if (r*h>=a.r*a.h)
            return true;
        else return false;
    }

};

bool cmp(cake a, cake b){
    if (a.r>=b.r)
        return true;
    else return false;
}

vector<cake> v;

double solve(int which){
    v.clear();

    v.push_back(cake(arr[which].first,arr[which].second));

    for(int i=0;i<n;i++){
        if (i==which)
            continue;
        if (arr[i].first<=arr[which].first){
            v.push_back(cake(arr[i].first,arr[i].second));
        }
    }

    if ((int)v.size()<k)
        return 0;


    sort(v.begin()+1,v.end());

    ll area=0;
    //cout<<"k = "<<k<<endl;
    for(int i=0;i<k;i++){
        area+=2*v[i].r*v[i].h;
    }

    double x=area*pi;

    x+=(double)arr[which].first*(double)arr[which].first*pi;


    //cout<<"base = "<<arr[which].first<<" at "<<v[0].r<<" , "<<v[1].r<<" x = "<<x<<endl;

    return x;


}

int main(){
    freopen("A-small-attempt0.in","r",stdin); freopen("A-small-1.txt","w",stdout);
    int t;
    scanf("%d",&t);

    for(int tc=1;tc<=t;tc++){
        scanf("%d %d",&n,&k);

        for(int i=0;i<n;i++){
            scanf("%d %d",&arr[i].first,&arr[i].second);
        }

        double maxVal=0;

        for(int i=0;i<n;i++){
            maxVal=max(maxVal,solve(i));
        }

        printf("Case #%d: %.7f\n",tc,maxVal);


    }
}
