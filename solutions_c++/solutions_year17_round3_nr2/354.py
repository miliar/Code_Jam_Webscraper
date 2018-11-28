#include<bits/stdc++.h>
using namespace std;
int test;
int II()
{
int n;
scanf("%d",&n);
return n;
}
int main(){
	ifstream cin("B-large (1).in");
	ofstream cout("B-large (1).out");
cin>>test;
for(int num=0;num<test;num++){
	int n,m;
	cin>>n>>m;
	vector<pair<pair<int,int>,int> > time;
	int worka=720,workb=720;
	for(int i=0;i<n;i++){
		int a,b;
		cin>>a>>b;
		time.push_back({{a,b},1});
		worka-=b-a;
	}
	for(int i=0;i<m;i++){
	int a,b;
		cin>>a>>b;
		time.push_back({{a,b},2});
		workb-=b-a;
	}
	sort(time.begin(),time.end());
	int ans=0;
	vector<int> lefta,leftb;
	for(int i=0;i<time.size();i++){
		if(i==0){
			if(time[time.size()-1].second!=time[i].second)
			ans++;
			else{
				if(time[i].second==1)
				lefta.push_back(1440-time[time.size()-1].first.second+time[i].first.first);
				else
				leftb.push_back(1440-time[time.size()-1].first.second+time[i].first.first);
			}
		}
		else{
				if(time[i-1].second!=time[i].second)
			ans++;
			else{
				if(time[i].second==1)
				lefta.push_back(time[i].first.first-time[i-1].first.second);
				else
				leftb.push_back(time[i].first.first-time[i-1].first.second);
			}
		}
		
	}
	sort(lefta.begin(),lefta.end());
	sort(leftb.begin(),leftb.end());
	/*cout<<"work a-b: "<<worka<<" "<<workb<<endl;
	cout<<"left a:"<<endl;
	for(int i=0;i<lefta.size();i++)
	cout<<lefta[i]<<" ";
	cout<<endl<<"left b: "<<endl;
	for(int i=0;i<leftb.size();i++)
	cout<<leftb[i]<<" ";
	*/
	//cout<<endl;
	for(int i=0;i<lefta.size();i++){
		if(lefta[i]<=worka){
			worka-=lefta[i];
		}
		else
		ans+=2;
	}
	for(int i=0;i<leftb.size();i++){
		if(leftb[i]<=workb){
			workb-=leftb[i];
		}
		else
		ans+=2;
	}
	/*if(n==1&&m==1||n==1&&m==0||n==0&&m==1){
	cout<<"Case #"<<num+1<<": 2"<<endl;	
	}
	else{
	if(n==2){
		if(worka>(1440-time[time.size()-1].first.second+time[0].first.first)||worka>(time[1].first.first-time[0].first.second))
	}
	
	}*/
	cout<<"Case #"<<num+1<<": "<<ans<<endl;
}
return 0;
}

