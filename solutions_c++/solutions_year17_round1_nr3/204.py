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
 int ad,bhd,ak,hk,bf,dbf;
int compute(int a,int b){
	int aad,abhd,aak,ahk;
	aad=ad;
	abhd=bhd;
	aak=ak;
	ahk=hk;
	int i,ans=0;
	rep(i,a){
		if(abhd-aak+dbf<=0 && abhd!=bhd){
			ans++;
			abhd=bhd;
			abhd-=aak;
		}
		
		aak-=dbf;
		ans++;
		abhd-=aak;
		if(abhd<=0)
			return -1;
	}
	rep(i,b){
		if(abhd-aak<=0){
			ans++;
			abhd=bhd;
			abhd-=aak;
		}
		
		aad+=bf;
		ans++;
		abhd-=aak;
		if(abhd<=0)
			return -1;
	}

	rep(i,300){
		if( ahk-aad>0 && abhd-aak<=0 ){
			ans++;
			abhd=bhd;
			abhd-=aak;
		}
		ahk-=aad;
		ans++;
		abhd-=aak;
		if(ahk<=0)
			break;
		if(abhd<=0)
			return -1;
	}
	if(ahk<=0)
		return ans;
	else
		return -1;
}

int main(){
    std::ios::sync_with_stdio(false);
    int t;
    cin>>t;
    int t1=t;
    while(t--){
	    cout<<"Case #"<<t1-t<<": ";
    	
    	cin>>bhd>>ad>>hk>>ak>>bf>>dbf;
    	int i,j;
    		
    		//continue;
    	
    	int ans=inf;
    	rep(i,200){
    		rep(j,200){
    			
    				int val=compute(i,j);
    				if(val!=-1){
    					ans=min(ans,val);
    				
    			}
    		}
    	}
    	if(ans!=inf){
    		cout<<ans<<endl;
    	}
    	else{
    		cout<<"IMPOSSIBLE"<<endl;
    	}

    }

}

