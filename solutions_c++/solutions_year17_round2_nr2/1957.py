/*
*	Author: Suparshva Mehta 	Username: suparsh14
*	College: DA-IICT, India
*	GCJ Round 1B
*	Q-B
*/

#include<bits/stdc++.h>

using namespace std;

int n;
int col[6]; // ROYGBV
int ans[1111];

vector<pair<int,int> > color;
char c[]={'R', 'O', 'Y', 'G', 'B', 'V'};

void brute(){

	if(color[0].first>(n)/2 || color[1].first>(n)/2 || color[2].first>(n)/2){
		cout<<"IMPOSSIBLE"<<endl;
		return;
	}	

	int cnt=0;

	int i;
	for(i=0;i<n;i+=2){
		if(cnt==color[0].first)break;
		ans[i]=color[0].second;
		cnt++;
	}

	cnt=0;

	i%=n;
	
	for(;;){

		if(cnt==color[1].first)break;
		
		while(ans[i]!=-1)i=(i+1)%n;
		
		ans[i]=color[1].second;
		cnt++;
		i+=2;
		i%=n;

	}

	int f=0;

	for(int i=0;i<n;i++){
		if(ans[i]==ans[(i+1)%n] || ans[i]==ans[(i-1+n)%n])f|=1;
	}

	if(f)cout<<"IMPOSSIBLE"<<endl;
	else{
		string a="";
		for(int i=0;i<n;i++){
			if(ans[i]==-1)a=a+c[color[2].second];
			else a=a+c[ans[i]];
			//cout<<ans[i]<<"sad";
		}
		cout<<a<<endl;
	}
}

void reset(){

	for(int i=0;i<n;i++){
		ans[i]=-1;
	}

}

int main(){

	int T;
	cin>>T;

	for(int ca=1;ca<=T;ca++)
	{
		cout<<"Case #"<<ca<<": ";

		//logic starts here

		
		cin>>n;

		reset();
		color.resize(0);

		for(int i=0;i<=5;i++){
			cin>>col[i];
			color.push_back(make_pair(col[i],i));
		}
		
		sort(color.begin(),color.end());
		reverse(color.begin(),color.end());
		brute();
	}

	return 0;
}