#include<iostream>
#include<cstring>
using namespace std;
#define ll long long
#define ld long double
#define key pair<ll,ll>
#define pb push_back
#define mp make_pair
#define ff first
#define ss second
#define fastio ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0)
int main()
{
    fastio;
    ll t;
    cin>>t;
    for(ll L=1;L<=t;L++)
    {
        ll l,r;
        cin>>l>>r;
        string mat[100];
        int ans=0;
        for(ll i=0;i<l;i++)
        {
            cin>>mat[i];
            for(ll j=0;j<mat[i].size();j++)
            {
                if(mat[i][j]=='?')
                mat[i][j]='#';
            }
        }
        for(ll i=0;i<l;i++)
        {
            int prev=-1;
            for(ll j=0;j<r;j++)
            {
                    if(mat[i][j]>='A'&&mat[i][j]<='Z')
                    {
                        for(ll J=j-1;J>=0;J--)
                        {
                            if(!(mat[i][J]>='A'&&mat[i][J]<='Z'))
                            {
                                mat[i][J]=mat[i][j];
                            }
                            else
                            break;
                        }
                        prev=j;
                        ans=1;
                    }
            }
            for(ll J=prev+1;J<r;J++)
            {
                 if(!(mat[i][J]>='A'&&mat[i][J]<='Z'))
                 {
                     mat[i][J]=mat[i][prev];
                 }
            }
        }
            if(ans==0)
            {
                for(ll i=0;i<l;i++)
                {
                    for(ll j=0;j<r;j++)
                    {
                        mat[i][j]='A';
                    }
                }
            }
            else
            {
                ll previous=-1;
                for(ll i=0;i<l;i++)
                {
                    if(mat[i][0]>='A'&&mat[i][0]<='Z')
                    {
                        for(ll I=i-1;I>previous;I--)
                        {
                            mat[I]=mat[i];
                        }
                        previous=i;
                    }
                }
                for(ll i=l-1;i>=0;i--)
                {
                    if(mat[i][0]>='A'&&mat[i][0]<='Z')
                    {
                        for(ll I=i+1;I<l;I++)
                        {
                            mat[I]=mat[i];
                        }
                        break;
                    }
                }
            }
            cout<<"Case #"<<L<<": "<<endl;
            for(ll i=0;i<l;i++)
            cout<<mat[i]<<endl;  
        }  
    }