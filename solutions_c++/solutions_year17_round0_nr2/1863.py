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
bool change(vector<int> &v){
   int i;
  for(i=0;i<v.size()-1;i++){
    if(v[i]>v[i+1]){
        v[i]--;
        v[i+1]=9;
        break;
     }
   }i++;
    for(;i<v.size();i++){
        v[i]=9;
    }
}
bool check(vector<int> v){
    for(int i=0;i<v.size()-1;i++){
    if(v[i]>v[i+1]){
        return false;
    }
    }
    return true;
}
int main()
{
  //  boost1;boost2;
    freopen("B-large.in", "r", stdin);
    freopen("blarge.out", "w", stdout);
    lli t,n;
    cin>>t;
    for(int k=1;k<=t;k++){
        cin>>n;
       lli val=n;
       vector<int> arr;
       while(val>0){
             arr.push_back(val%10);
             val/=10;
           }
           for(int i=0,j=arr.size()-1;i<(arr.size()/2);i++,j--){
              swap(arr[i],arr[j]);
           }
       for(int i=0;i<19;i++)
       {
          /* cout<<"\nNum : ";
           for(int i=0;i<arr.size();i++){
            cout<<arr[i]<<" ";
           }*/
           if(check(arr)){
             break;
           }
           else{
            change(arr);
           }
       }
       lli ans=arr[0],val1=0,j=1;
       cout<<"Case #"<<k<<": ";
       for(int i=1;i<arr.size();i++){
            if(arr[i]==0){
              break;
          }
          ans=ans*10+arr[i];
       }
       cout<<ans<<endl;
    }
	return 0;
}





