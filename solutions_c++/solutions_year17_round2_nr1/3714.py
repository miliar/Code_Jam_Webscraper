#include<bits/stdc++.h>
using namespace std;
double dest;
int nhourse;

struct data{
	double pos, spd;
}arr[1010];

bool can(double sp){
	for(int i=0;i<nhourse;i++){
		double time1=dest/sp;
		double time2=(dest-arr[i].pos)/arr[i].spd;
		if(time1<time2){
			return false;
		}
	}
	return true;
}

double binser(){
	double ki=0.0, ka=1000000000000000.0, mid;
	for(int i=0;i<100;i++){
		mid=(ki+ka)/2;
		if(can(mid)){
			ki=mid;
		}
		else ka=mid;
	}
	return mid;
}

int main(){
	ios_base::sync_with_stdio(false); cin.tie(NULL);
	int tc;
	ifstream in;
	in.open("A-large.in");
	
	ofstream out;
	out.open("out.out");
	in>>tc;
	for(int h=1;h<=tc;h++){
		in>>dest>>nhourse;
		for(int i=0;i<nhourse;i++){
			in>>arr[i].pos>>arr[i].spd;
		}
		double ans = binser();
		cout<<fixed;
		cout<<"Case #"<<h<<": "<<setprecision(9)<<ans<<endl;
		out<<fixed;
		out<<"Case #"<<h<<": "<<setprecision(9)<<ans<<endl;
	}
	in.close();
	out.close();
	return 0 ;
}
