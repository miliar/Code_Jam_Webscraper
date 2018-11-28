
#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

struct cmp{

	bool operator()(pair<ll,ll> x, pair<ll,ll> y){

		return x.first<=y.first;

	}

};

double MAX(double x, double y){

	if(x>=y) return x;

	else return y;



}


int main(){

ios_base::sync_with_stdio(0);
cin.tie(NULL);

#ifndef ONLINE_JUDGE
freopen("input.txt", "r", stdin);
freopen("output.txt", "w", stdout);
#endif

int t,T;

cin>>T;

for(t=1;t<=T;++t){

	ll d,n,i,j,pos,speed;

	cin>>d>>n;

	priority_queue< pair<ll,ll> ,vector< pair<ll,ll> >, cmp > q;

	pair<ll,ll> prev,current;


	for(i=0;i<n;++i){

		cin>>pos>>speed;

		q.push({pos,speed});


	}

	double TIME=0,TIMEx=0,TIMEy;

	while(q.size()){		

		if(q.size()!=0) current=q.top();

		q.pop();

		TIME=MAX(TIME,double(d-current.first)/current.second);

	}

	



	cout<<setprecision(6)<<fixed<<"Case #"<<t<<": "<<d/TIME<<"\n";



}


}



	