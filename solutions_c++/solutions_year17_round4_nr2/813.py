//teja349
#include <bits/stdc++.h>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <climits>
#include <utility>
#include <algorithm>
#include <cmath>
#include <queue>
#include <stack>
#include <iomanip> 
//setbase - cout << setbase (16); cout << 100 << endl; Prints 64
//setfill -   cout << setfill ('x') << setw (5); cout << 77 << endl; prints xxx77
//setprecision - cout << setprecision (14) << f << endl; Prints x.xxxx


using namespace std;
#define f(i,a,b) for(i=a;i<b;i++)
#define rep(i,n) f(i,0,n)
#define fd(i,a,b) for(i=a;i>=b;i--)
#define pb push_back
#define mp make_pair
#define vi vector< int >
#define vl vector< ll >
#define ss second
#define ff first
#define ll long long
#define pii pair< int,int >
#define pll pair< ll,ll >
#define sz(a) a.size()
#define inf (1000*1000*1000+5)
#define all(a) a.begin(),a.end()
#define tri pair<int,pii>
#define vii vector<pii>
#define vll vector<pll>
#define viii vector<tri>
#define mod (1000*1000*1000+7)
#define pqueue priority_queue< int >
#define pdqueue priority_queue< int,vi ,greater< int > >

//std::ios::sync_with_stdio(false);   

int main(){
    std::ios::sync_with_stdio(false);
    int t;
    cin>>t;
    int t1=t;
    while(t--){
    	cout<<"Case #"<<t1-t<<": ";
    	int arr[13][1234]={0};
		int haha[13]={0};
    	int n,c,m,i,val1,val2,l1,l2,x,y,ans=0;
    	cin>>n>>c>>m;
    	rep(i,m){
    		cin>>val1>>val2;
    		arr[val2][val1]++;
    		haha[val2]++;

    	}
    	ans=arr[1][1]+arr[2][1];
    	x=arr[2][1];
    	y=arr[1][1];
    	l1=haha[1]-arr[1][1];
    	l2=haha[2]-arr[2][1];
    	if(l1-x<=0 || l2-y<=0){
    		cout<<ans+max(0,max(l1-x,l2-y))<<" "<<0<<endl;
    		continue;
    	}
    	else{
    		ans+=max(l1-x,l2-y);
    		if(l1-x>=l2-y){
    			x+=(l1-x-l2+y);
    		}
    		else{
    			y+=(l2-y-l1+x);
    		}
    		int total=x+y;
    		//cout<<total<<endl;
    		int mama=min(l1-x,l2-y);
    		//cout<<mama<<endl;
    		int jjj=0;
    		f(i,2,n+1){
    			if(arr[1][i]+arr[2][i]>mama){
    				if(total>arr[1][i]+arr[2][i]-mama){
    					total-=arr[1][i]+arr[2][i]-mama;
    				}
    				else{
    					jjj=max(arr[1][i]+arr[2][i]-total-mama,jjj);
    				}
    			}
    		}
    		cout<<ans<<" "<<jjj<<endl;
    	}


  }

}

