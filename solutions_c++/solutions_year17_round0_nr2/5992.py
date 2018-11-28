///apac question 2 round 1 , 2017
#include<bits/stdc++.h>
#include<vector>
#include<algorithm>
#define pi acos(-1)
#include<string.h>
#define rep(i,n) for(i=0;i<n;i++)
#define pb push_back
using  namespace std;
typedef long long int lli;
typedef pair<int,int> pii;
typedef vector<pii> vpii;
typedef vector<int> vi;
typedef  vector<vi> vvi;
typedef vector<lli> vlli;
typedef vector<double> vd;
typedef map<int,int> mpii;
typedef map<string,int> mpsi;
typedef tuple<int,int,int> tiii ;
typedef vector<tiii> vtiii ;
#define mp make_pair
#define modu 1000000007
int main()
{
    freopen("inputbbjam.in","r",stdin);
    freopen("outputb.out","w",stdout);
    lli n,i,flag,k,j,test,t;
    string s;
    cin>>test;
    for(t=0;t<test;t++)
    {
        cin>>s;
        n=s.size();
        int arr[n],sol[n];
        for(i=0;i<n;i++)
            arr[i]=s[i]-48;
        sol[0]=arr[0];
        flag=1;
        i=1;
        if(n==1){cout<<"Case #"<<t+1<<": "<<sol[0]<<endl;goto done;}
        while(flag && i<n)
        {
            if(arr[i]>=arr[i-1])
                {
                    sol[i]=arr[i];
                    i++;
                }
            else flag=0;
        }
        if(i==n){
            cout<<"Case #"<<t+1<<": ";
            for(j=0;j<n;j++)
                cout<<sol[j];
            cout<<endl;
            goto done;
        }
        k=i-1;
        flag = 1;
        while(flag && k>=0)
        {
            if(k==0){  sol[k]--; flag=0;   }
            else{
                sol[k]--;
                if(sol[k]>=sol[k-1])flag=0;
                else k--;
            }
        }
        for(j=k+1;j<n;j++)
            sol[j]=9;
        i=0;
        while(sol[i]==0)i++;
        cout<<"Case #"<<t+1<<": ";
        for(j=i;j<n;j++)
            cout<<sol[j];
        cout<<endl;
        done:;
    }
}
