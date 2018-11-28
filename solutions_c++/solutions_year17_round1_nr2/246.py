#include <bits/stdc++.h>

using namespace std;
#define pb push_back
typedef long long LL;

int n,p;
LL r[100],x;

priority_queue< pair<int,int> > q[100];


bool f(LL sup, LL req, pair<int,int> &res){
	LL sm = sup/req;
	LL tmp = sm;
	int mx= 0;
	int mn = INT_MAX;
	if ( sup*100 > sm*110*req || sup*100 < sm*90*req ){
		if ( sup*100 > (sm+1)*110*req || sup*100 < (sm+1)*90*req ){
			return false;
		}
	}
	
	if ( sup*100 > tmp*110*req || sup*100 < tmp*90*req ) tmp++;
	while( sup*100 <= tmp*110*req && sup*100 >= (tmp)*90*req  ) tmp--;	
	mn = tmp+1;
	tmp = sm;
	if ( sup*100 > tmp*110*req || sup*100 < tmp*90*req ) tmp++;
	while( sup*100 <= tmp*110*req && sup*100 >= (tmp)*90*req  ) tmp++;
	mx = tmp-1;
	res = {mn,mx};
	return true;
}

void solve(int test){
	cout << "Case #" << test + 1 << ": ";
	cin >> n >> p;
	for(int i=0; i<n; i++){
		cin >> r[i];
		while( !q[i].empty() ) q[i].pop();
	}
	for(int i=0; i<n; i++){
		for(int j=0; j<p; j++){
			cin >> x;									
			pair<int,int> temp = make_pair(-1,-1);
			if( f(x,r[i],temp) ){			
				q[i].push({-temp.first, -temp.second} );
			}
		}		
	}
	int res = 0;
	while(true)	{
		bool flag = true;
		for(int i=0; i<n; i++){
			if( q[i].empty() ) flag= false;
		}
		if(!flag) break;
		int mx = 0;
		for(int i=0; i<n; i++){
			mx = max( mx, -q[i].top().first );
		}	
		for(int i=0; i<n; i++){
			if( -q[i].top().second < mx ){
				flag=false;
				while(!q[i].empty() && -q[i].top().second < mx  ) q[i].pop();
			}
		}		
		if(flag){
			res ++;
			for(int i=0; i<n; i++) q[i].pop();
		}
	}
	cout << res << endl;
}


int ntest;
int main(){
	freopen("B-large.in","r",stdin);
	//freopen("","r",stdin);
	freopen("test.out","w",stdout);
	cin >> ntest;
	for(int test=0; test<ntest; test++){
		solve(test);
	}
	return 0;
}
