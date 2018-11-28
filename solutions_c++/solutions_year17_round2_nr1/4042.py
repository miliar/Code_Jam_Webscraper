#include<bits/stdc++.h>
using namespace std;
bool compare(const pair<long int , long int>&i, const pair<long int, long int>&j)
{
    return i.first < j.first;
}

int main(){
	long int t;
	cin>>t;
	long int dec=t;
	while(t>0){
		long int d,n;
		cin>>d>>n;
		vector< pair<long int,long int> >v;
		for(int i=0;i<n;i++){
			long int pos,vel;
			cin>>pos>>vel;
			v.push_back(make_pair(pos,vel));
		}
		sort(v.begin(),v.end(),compare);
		double timeprev=float(d - v[n-1].first)/v[n-1].second;
		double maxtime=timeprev;
		for(int i=n-2;i>=0;i--){
			double temptime = float(d - v[i].first)/v[i].second;
			if(temptime >= timeprev){
				maxtime=temptime;
				continue;
			}
			pair<long int,long int>a=v[i+1];
			pair<long int,long int> b=v[i];
			double x = float(b.second*a.first - a.second*b.first)/(b.second - a.second);
			double timereach = float(x-a.first)/a.second + float(d - x)/min(a.second,b.second);
			timeprev=timereach;
			if (timereach > maxtime)
				maxtime=timereach;

		}
		cout << setprecision(6) <<fixed;
		cout<<"Case #"<<dec-t+1<<": "<<double(double(d)/maxtime)<<endl;
		t--;}
}