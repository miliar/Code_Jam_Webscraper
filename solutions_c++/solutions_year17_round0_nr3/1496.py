#include <iostream>
#include<cmath>
#include<map>
#include<algorithm>
using namespace std;
map<long long int , long long int>mp,mp2;
int main()
{
    freopen("input.txt","r" , stdin);
   freopen("ans.txt","w" , stdout);
    int T; cin>>T;
    for(int w=0;w<T;w++)
    {
        long long int n,k,nums[100100]={0}; cin>>n>>k; int num=0;
        nums[num++]=n; mp[n]=1; long long int first=n, second=n;  long long int g=n;
        mp[first/2]+=mp[first]; mp[(first-1)/2]+=mp[first];
        first=n/2; second=(n-1)/2;
        nums[num++]=first; if(first!=second) nums[num++]=second; g=g/2;
        while(g)
        {
            mp[first/2]+=mp[first]; mp[(first-1)/2]+=mp[first];
            if(first!=second){
            mp[second/2]+=mp[second]; mp[(second-1)/2]+=mp[second];}
            if(first%2==0) {second=first/2; first=(first-1)/2;} else {first=second/2; second=(second-1)/2;}
            g/=2;
            nums[num++]=first; if(first!=second) nums[num++]=second;
        } long long int sum=0; long long int ans1=0,ans2=0;
        sort(nums,nums+num);
        for(int i=num-1;i>=0;i--)
        {
            sum+=mp[nums[i]];
            if(sum>=k)
            {
                ans1=(nums[i]/2); ans2=(nums[i]-1)/2;
        //       cout<<i<<"HERE"<<sum<<endl;
                break;
            }
        }
      //  for(int i=0;i<num;i++) cout<<mp[nums[i]]<<" "<<nums[i]<<endl;
                mp.clear();
      cout<<"Case #"<<w+1<<":"<<" ";
      cout<<max(ans1,ans2)<<" "<<min(ans1,ans2);
      cout<<endl;
    }
}
