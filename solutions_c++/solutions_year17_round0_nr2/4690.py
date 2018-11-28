#include <bits/stdc++.h>
#include<stdio.h>
using namespace std;
#define pii pair<long long,long long>
#define F(i,a,b) for(ll i = (ll)(a); i <= (ll)(b); i++)
#define RF(i,a,b) for(ll i = (ll)(a); i >= (ll)(b); i--)
#define PI 3.14159265
#define ll long long
#define ff first
#define ss second
#define pb(x) push_back(x)
#define mp(x,y) make_pair(x,y)
#define debug(x) cout << #x << " = " << x << endl
#define INF 1000000009
#define mod 1000000007

int main()
{
     ios::sync_with_stdio(0);
     ll int n,k;
     cin>>n;
    
     ll int caser=0;
     ll int count;
     ll int flag=0;
     for(int i=0;i<n;i++)
     {
         count=0;
         caser++;
         flag=0;
         cin>>k;
         ll int p = k;
         
         while(p>0)
         {
             count++;
             p = p/10;
         }
        ll int arr[count];
    
        ll int r = count-1;
        ll int e=r;
        p=k;
        while(p>0)
        {
            arr[e]=p%10;
            p = p/10;
            e--;
        }
        if(arr[0]==1)
        {
         cout<<"Case #"<<caser<<": ";   
            for(int j=1;j<=r;j++)
            {
                if(arr[j]==1)
                {
                    continue;
                    
                }
                else if(arr[j]==0)
                {
                    flag=1;
                    break;
                }
                else
                break;
            }
            if(flag==1)
            {
                
                for(int j=0;j<r;j++)
                cout<<9;
                cout<<"\n";
            }
            else
            {
                flag=0;
                for(int j=0;j<=r;j++)
            {
                if(flag==1)
                arr[j]=9;
                else if(j==r)
                arr[j]=arr[j];
                else if(arr[j+1]>=arr[j])
                {
                    arr[j] = arr[j];
                }
                else
                {
                    flag=1;
                   ll int m = j;
                   
                   ll int p = arr[m];
                   while(m-1>=0 && arr[m]==arr[m-1])
                   {
                       arr[m]=9;
                       m--;
                   }
                   arr[m] = p-1;
                }
            }
            
            for(int j=0;j<=r;j++)
            cout<<arr[j];
        
            cout<<"\n";
            }
        }
        else
        {
            cout<<"Case #"<<caser<<": ";  
            for(int j=0;j<=r;j++)
            {
                if(flag==1)
                arr[j]=9;
                else if(j==r)
                arr[j]=arr[j];
                else if(arr[j+1]>=arr[j])
                {
                    arr[j] = arr[j];
                }
                else
                {
                    flag=1;
                   ll int m = j;
                   
                   ll int p = arr[m];
                   while(m-1>=0 && arr[m]==arr[m-1])
                   {
                       arr[m]=9;
                       m--;
                   }
                   arr[m] = p-1;
                }
            }
            for(int j=0;j<=r;j++)
            cout<<arr[j];
            cout<<"\n";
            
        }
        
         
     }

    return 0;
}