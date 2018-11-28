#include<bits/stdc++.h>
using namespace std;
#define lli long long int
#define ll long long
#define l long
#define f first
#define se second
#define pb push_back
#define db double
#define mp make_pair
#define Mod 100000000
#define boost1 ios::sync_with_stdio(false);
#define boost2 cin.tie(0);
bool compare(std::pair<ll,vector<ll>> p1, std::pair<ll,vector<ll>> p2){
    return p1.f>p2.f; ///for descending order sort
}
db max_val(db t1,db t2){
     if(t1>=t2){
        return t1;
     }
     else{return t2;}
}
int main()
{
  //  boost1;boost2;
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    lli t,n,d;
    cin>>t;
    for(int k=1;k<=t;k++){
       cin>>d>>n;
       db pos,speed,dist;
       db time=(0.0),ans=0.0;
       while(n--){
          cin>>pos>>speed;
          dist=(d-pos);
          db temp=dist/speed;
        //  cout<<"temp for case #"<<k<<" : "<<temp<<endl;
          time=max_val(time,temp);
       }
       //cout<<"time for case #"<<k<<" : "<<time<<endl;
       ans=d/time;
       cout<<"Case #"<<k<<": ";
       std::cout << std::fixed;
       std::cout << std::setprecision(6);
       std::cout <<ans<<endl;
    }
	return 0;
}
