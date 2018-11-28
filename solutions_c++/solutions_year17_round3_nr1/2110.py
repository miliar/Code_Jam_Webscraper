#include<bits/stdc++.h>
using namespace std;

vector<pair<long long ,long long > > v;
long long int a[100001];
#define PI 3.14159265359
double pos[10001],sp[10001];
long long N,K;
map<pair<pair<int,int>,int>, long long > mp;
long long rec( int ind ,int curr, int prev){

if(ind>=N)
    return 0;
    if(curr==K)
    return 0;
int rem=N-ind;
if(rem <(K-curr)){
//cout<<"Yaha aaya"<<endl;
//cout<<N<<" "<<ind<<" "<<K<<" "<<curr<<endl;
    return LONG_LONG_MIN;

}

if(mp.find(make_pair(make_pair(ind,curr),prev))!=mp.end()){
    return mp[make_pair(make_pair(ind,curr),prev)];
}
long long val=0;
if(prev!=-1)
val =((v[ind].first*v[ind].first)-(v[prev].first*v[prev].first))+2*v[ind].first*v[ind].second;
else
    val =(v[ind].first)*v[ind].first+2*v[ind].first*v[ind].second;
long long ans=0;
long long cal =rec(ind+1,curr+1,ind);
if(cal!=LONG_LONG_MIN){
    ans = cal+val;
}
long long cal1= rec(ind+1 ,curr ,prev);
if(cal1!=LONG_LONG_MIN){

    ans=max(ans,cal1);
}
return mp[make_pair(make_pair(ind,curr),prev)]=ans;
}
int main(){
freopen("C:\\Users\\Chandan\\Desktop\\input.txt", "r", stdin);
freopen("C:\\Users\\Chandan\\Desktop\\gcj.txt", "w", stdout);

double D,x,y;
int t;
cin>>t;
int lc=1;
while(t--){
        int i;
        cout<<"Case #"<<lc<<": ";
        lc++;
cin>>N>>K;

for(i=0;i<N;i++){

    cin>>x>>y;
    v.push_back(make_pair(x,y));

}

sort(v.begin(),v.end());
mp.clear();
double ans =((double)(rec(0,0,-1)))*PI;;
v.clear();
mp.clear();
printf("%.7lf\n",ans);
}
return 0;
}
