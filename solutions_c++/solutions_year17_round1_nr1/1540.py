/// In The Name Of Allah
#include<bits/stdc++.h>
#define pb push_back
#define ll long long
#define F first
#define S second
#define OO 1000000000
#define mod 1000000007
using namespace std;
int t,n,k,ans,m,b;
char arr[100][100];
int main(){
    freopen("A-large (1).in","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>t;
    while(t--){
        cin>>n>>m;
        for(int i=0 ; i<n ; i++)
            for(int j=0 ; j<m ; j++)
                cin>>arr[i][j];
        for(int i=1 ; i<n ; i++)
            for(int j=0 ; j<m ; j++)
                if(arr[i][j]=='?')  arr[i][j]=arr[i-1][j];
        for(int i=n-2 ; i>=0 ; i--)
            for(int j=0 ; j<m ; j++)
                if(arr[i][j]=='?')  arr[i][j]=arr[i+1][j];
        for(int i=0 ; i<n ; i++)
            for(int j=1 ; j<m ; j++)
                if(arr[i][j]=='?')  arr[i][j]=arr[i][j-1];
        for(int i=0 ; i<n ; i++)
            for(int j=m-1 ; j>=0 ; j--)
                if(arr[i][j]=='?')  arr[i][j]=arr[i][j+1];
        cout<<"Case #"<<++b<<":"<<endl;
        for(int i=0 ; i<n ; i++)
        {
            for(int j=0 ; j<m ; j++){
                cout<<arr[i][j];
            }
            cout<<endl;
        }
    }

}
