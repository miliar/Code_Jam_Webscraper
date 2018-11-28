#include <bits/stdc++.h>

using namespace std;

int main(void){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int chars[] = {'R','O','Y','G','B','V'};
	int test;
	cin>>test;
	for(int t=1;t<=test;t++){
		int n, ary[6];
		cin>>n;
		for(int i=0;i<6;i++)cin>>ary[i];
		bool imsbl = false;
		for(int i=0;i<6;i++)if(ary[i]>(n)/2){imsbl=true;break;}
		if(imsbl)cout<<"Case #"<<t<<": IMPOSSIBLE"<<endl;
		else{
			char ans[n+1];
			ans[n]='\0';
			vector<pair<int,char> > v;
			for(int i=0;i<6;i++)if(ary[i]>0)v.push_back(make_pair(ary[i],chars[i]));
			sort(v.begin(),v.end());
			reverse(v.begin(),v.end());
			int cur = 0;
			for(int i=0;i<n;i+=2){
				ans[i]=v[cur].second;
				v[cur].first--;
				if(v[cur].first==0)cur++;
			}
			for(int i=1;i<n;i+=2){
				ans[i]=v[cur].second;
				v[cur].first--;
				if(v[cur].first==0)cur++;
			}

			cout<<"Case #"<<t<<": "<<ans<<endl;
		}
	}
	return 0;
}
