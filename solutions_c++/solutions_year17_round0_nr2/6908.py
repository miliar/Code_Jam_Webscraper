//All codes submitted Srivatsa Sinha
#include <bits/stdc++.h>
#include <stdlib.h>

#define ll long long
#define MAX 1000001
#define ff first
#define ss second
#define MOD 1000000007
#define vi vector<int>
#define vll vector<ll,ll>
#define pii pair<int,int>
#define pll pair<ll,ll>
#define DEBUG cout<<"I am here\n"
#define pb push_back
#define mp make_pair
#define CLEAR_LIST for(int i=1; i<=MAX; i++) adj[i].clear()

#include <stdio.h>
#include <time.h>
#include <unistd.h>





using namespace std;
string str;
int j;



int main()
{
   freopen("input.txt","r",stdin);
   freopen("output.txt","w",stdout);
   //for(int i=901; i<=1000; i++) cout<<i<<endl;
    ios_base::sync_with_stdio(false);
    ll t=1;
    cin>>t;
    for(int k=1; k<=t; k++)
    {
      cin>>str;
      //cout<<str<<' ';
      bool flag1 = true;
      while(flag1) { flag1 = false;
      for(int i=0; i<str.size()-1; i++)
      {
        if(str[i]>str[i+1]) {  flag1 = true; str[i]-=1;  j=i+1; while(j<str.size()){str[j]='9'; j++;}}
      }
      }

      bool flag = false;
      cout<<"Case #"<<k<<": ";
      for(int i=0; i<str.size(); i++)
      {
      if(flag || str[i]!='0') {cout<<str[i]; flag=true;}
      }
      cout<<endl;

    }
    return 0;
}
