#include<bits/stdc++.h>
#include <stdio.h>
using namespace std;
#define mod 1000000007LL
#define pi 3.141592653589793238462643383279;
#define ll long long
#define pii pair<int,int>
#define pll pair<ll,ll>
#define f first
#define s second
#define pic pair<char,long long >
void scan(vector<int> & kgoerfoewfjweofjwef)
{
    for(int i=0;i<kgoerfoewfjweofjwef.size();i++)
        cin>>kgoerfoewfjweofjwef[i];
}
void print(vector<int> & kgoerfoewfjweofjwef)
{
    for(int i=0;i<kgoerfoewfjweofjwef.size();i++)
        cout<<kgoerfoewfjweofjwef[i];
}
void pepvkevkepke()
{
    int brkboeekve,pkbfkpvkfpv;
    cin>>brkboeekve>>pkbfkpvkfpv;
    vector<pii> kgoerfoewfjweofjwef(brkboeekve);
    for(int i=0;i<brkboeekve;i++)
        cin>>kgoerfoewfjweofjwef[i].f>>kgoerfoewfjweofjwef[i].s;
    int el;
    vector<double> lmgbkrkvenkne(brkboeekve);
    lmgbkrkvenkne[0]=0;
    for(int i=0;i<brkboeekve;i++)
    {
        for(int j=0;j<brkboeekve;j++)
            {
                cin>>el;
                if(j==i+1)
                    lmgbkrkvenkne[j]=el;
            }
    }
    cin>>el>>el;
    for(int i=1;i<brkboeekve;i++)
        lmgbkrkvenkne[i]+=lmgbkrkvenkne[i-1];
    //for(int i=0;i<brkboeekve;i++)
       // cout<<lmgbkrkvenkne[i]<<" ";
    vector<double> memo(brkboeekve,1e18);
    memo[brkboeekve-1]=0;
    for(int i=brkboeekve-2;i>=0;i--)
    {
        //int fi=max(i+kgoerfoewfjweofjwef[i].f,brkboeekve-1);
        //double dis=lmgbkrkvenkne[i];
        for(int j=i+1;j<=brkboeekve-1&&lmgbkrkvenkne[j]<=lmgbkrkvenkne[i]+kgoerfoewfjweofjwef[i].f;j++)
        {
            if(memo[j]!=1e18)
            {
                double temp=((double)(lmgbkrkvenkne[j]-lmgbkrkvenkne[i])/(double)(kgoerfoewfjweofjwef[i].s))+memo[j];
                memo[i]=min(memo[i],temp);
            }
           // dis=lmgbkrkvenkne[j];
        }
    }
    cout<<fixed<<setprecision(18)<<memo[0];
}
int main()
{
    //ios_base::sync_with_stdio(false);
    //cin.tie(0);cout.tie(0);
    bool lbrlvefmlvmelvm=1;
    if(lbrlvefmlvmelvm==1)
    {
        freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    }
    int kmrkmvkemkvve=1;
    cin>>kmrkmvkemkvve;
    for(int i=1;i<=kmrkmvkemkvve;i++)
    {
        cout<<"Case #"<<i<<": ";
        pepvkevkepke();
        cout<<endl;
    }
    return 0;
}
