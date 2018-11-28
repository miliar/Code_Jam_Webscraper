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
//setprecision - cout << setprecision (4) << f << endl; Prints x.xxxx


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
int n,p;
double arr[100][100];
double rec[100];
vector<vii> vec(100);

int haha[100];
int compute(int i,int j){
	double val=arr[i][j]/1.1;
	val/=rec[i];
	int val1=ceil(val);
	double vale=arr[i][j]/0.9;
	vale/=rec[i];
	//cout<<vale<<endl;
	int vale1=floor(vale);
	//cout<<val1<<" "<<vale1<<endl; 
	if(vale1<val1){
		return 0;
	}
	vec[i].pb(mp(val1,vale1));
	return 0;
}
int main(){
    std::ios::sync_with_stdio(false);
    int t;
    cin>>t;
    int t1=t;
    while(t--){
    	cout<<"Case #"<<t1-t<<": ";
    	int i,j;
    	cin>>n>>p;
    	rep(i,n){
    		cin>>rec[i];
    		vec[i].clear();
    		haha[i]=0;
    		//pq[i].clear();
    	}
    	rep(i,n){
    		rep(j,p){
    			cin>>arr[i][j];
    		}
    	}
    	rep(i,n){
    		rep(j,p){
    			compute(i,j);
    		}
    	}
    	rep(i,n){
    		sort(vec[i].begin(),vec[i].end());
    	}
    	//return 0;
    	vector< pdqueue > pq(100);
    	int pac=1,flag,remem,ans=0;
    	while(1){
    		flag=0;
    		rep(i,n){
    			if(vec[i].size()==haha[i] && pq[i].empty()){
    				flag=1;
    				break;
    			}
    		}
    		
    		if(flag){
    			break;
    		}
    		rep(i,n){
    			f(j,haha[i],vec[i].size()){
    				if(vec[i][j].ff<=pac){

    					pq[i].push(vec[i][j].ss);
    				}
    				else{
    					//haha[i]=j;
    					break;
    				}
    			}
    			haha[i]=j;

    		}

    		rep(i,n){
    			//cout<<"yoo"<<endl;
    			while(!pq[i].empty()){
    				if(pq[i].top()<pac){
    					pq[i].pop();
    				}
    				else{
    					break;
    				}
    			}

    		}
    		//cout<<"yoo"<<endl;
    		flag=0;
    		while(1){

    			rep(i,n){
    				if(pq[i].empty()){
    					flag=1;
    					remem=i;
    					break;
    				}
    			}
    			if(flag){
    				break;
    			}
    			ans++;
    			rep(i,n){
    				pq[i].pop();
    			}
    		}
    		if(haha[i]!=vec[i].size()){
    			pac=vec[i][haha[i]].ff;
    		}
    		else{
    			pac=inf;
    		}



    	}
    	cout<<ans<<endl;
    }

}

