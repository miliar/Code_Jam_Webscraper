#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include<string>
using namespace std;

#define ll long long
#define inf 1e18
struct arr
{
    int val;
    int ind;
}a[3];
bool comp(arr &lhs, arr &rhs)
{
    return lhs.val>rhs.val;
}
int main() 
{
      freopen("input3.in", "r", stdin);
      freopen("output.txt", "w", stdout);  
    int ar[1005],n,t,num,i,maxind,j;
    
    cin>>t;
    for(int k_=1;k_<=t;k_++)
    {
        cin>>n;
        for(int i=0;i<6;i++)
        {
            cin>>num;
            if(i%2==0)
            {
                a[i/2].val=num;
                a[i/2].ind=i/2;
            }
        }
        sort(a,a+3,comp);
      //  if(k_==2)
    //    cout<<a[0].val<<" "<<n<<endl<<endl;
        
        if(a[0].val > ceil((n-1)/2.0))
        {
            cout<<"Case #"<<k_<<": IMPOSSIBLE\n";
            continue;
        }
        i=0;
        while(a[0].val--)
        {
            ar[i]=a[0].ind;
            i+=2;
        }
        maxind=i-2;
        
        for(i=maxind+1,j=0;i<n;i++,j++)
        {
          if(j%2==0)
          {
            ar[i]=a[1].ind;
            a[1].val--;
          }
          else
          {
              ar[i]=a[2].ind;
              a[2].val--;
          }
        }
        for(i=1;i<maxind;i+=2)
        {
            if(a[1].val)
            {
                ar[i]=a[1].ind;
                a[1].val--;
            }
            else
            {
                ar[i]=a[2].ind;
                a[2].val--;
            }
        }
        cout<<"Case #"<<k_<<": ";
        for(i=0;i<n;i++)
        {
            if(ar[i]==0)
            cout<<"R";
            if(ar[i]==1)
            cout<<"Y";
            if(ar[i]==2)
            cout<<"B";
        }
        cout<<endl;
        
        /*i=1;
        int j=0;
        int flag=0;
        while(a[1].val || a[2].val)
        {
            if(j%2==0)
            {
                ar[i]=a[1].ind;
                a[1].val--;
            }
            else
            {
                if(a[1].val>a[2].val)
                ar[i]=a[1]
                ar[i]=a[2].ind;
                a[2].val--;
            }
            j++;
            if(i+1==maxind)
            {
                flag=1;
            }
            if(flag==0)
            i+=2;
            else
            i+=1;
        }*/
    }
    return 0;
}
