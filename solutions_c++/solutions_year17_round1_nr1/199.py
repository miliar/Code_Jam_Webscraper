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
int n,m,haha,prev; 
string str[200];
int preprocess(int i){
	int lol=-1,j;
	rep(j,m){
		if(str[i][j]!='?'){
			lol=j;
			break;
		}
	}
	//cout<<i<<endl;
	if(lol!=-1){
		prev=1;
		rep(j,m){
			if(str[i][j]!='?'){
				lol=j;
			}
			else{
				str[i][j]=str[i][lol];
			}
		}
		return 0;
	}
	else{
		if(prev!=-1){
			if(haha){
				str[i]=str[i-1];
			}
			else{
				str[i]=str[i+1];
			}
		}
		return 0;

	}
}
int main(){
  	std::ios::sync_with_stdio(false);
    int t;
    cin>>t;
    int t1=t;
    while(t--){
   		cout<<"Case #"<<t1-t<<": "<<endl;
   		int i;
   		cin>>n>>m;
   		rep(i,n){
   			cin>>str[i];
   		}
   		prev=-1;
   		haha=1;
   		rep(i,n){
   			preprocess(i);
   		}
   		prev=-1;
   		haha=0;
   		fd(i,n-1,0){
   			preprocess(i);
   		}
   		rep(i,n){
   			cout<<str[i]<<endl;
   		}

    }

}

