#include <bits/stdc++.h>
using namespace std;
 
#define fr(i,a,b) for(int (i)=(int) a;(i)<=(int)(b);++(i))
#define li list<int>
#define ll long long
#define mp make_pair
#define mod 1000000007
#define pb push_back
#define pi pair<int,int>
#define pr printf
#define vi vector<int>
#define vpi vector< pi > 
int d;
ll n,r;
void lss()
{
      d=0;
      int f=1;
      ll mm=n;
      while(mm)
     // cout<<mm<<" ";
      {
            if(mm%(ll)10==0) f=0;
            mm/=(ll)10;
            d++;
      }
      
}
int main() {
	// your code goes here
      //std::ios_base::sync_with_stdio(false);
      //freopen("input","r",stdin);
     // freopen("output","w",stdout);
      int t,tt,j;
      cin>>t;tt=t;
      while(t--)
      {
            cin>>n;
           cout<<"Case #"<<tt-t<<": ";
           int a[20]={0},l,b[20],c[20];
         lss();
         ll z=10,m=n,mn;
         mn=m%z;
         fr(i,0,d-1)
         {
             a[d-i]=m%10;
             m/=10;
         }
         fr(i,2,d)
           {
               if(a[i]<a[i-1])
               {
                   i=i-1;;
                   for(j=i-1;j>0;j--)
                   {
                   if(a[j]<=a[j+1]-1)
                   break;
                   }
                   j++;
                   a[j]=a[j]-1;
                   fr(k,j+1,d) a[k]=9;
                   break;
               }
           }
           j=1;
           while(j<=d&&a[j]<=0) j++;
           fr(i,j,d) cout<<a[i];
           
           
           cout<<"\n";
      }
      
	return 0;
}

