#include <iostream>
#include <algorithm>
#include <map>
#include <vector>
#include <cstdio>
#include <cstring>
#include <fstream>
#include <unordered_map>
#include <set>
#include <string>
#include <cmath>
#include <iomanip>

using namespace std;

#define IN_FILE "inputlol.in"
#define OUT_FILE "outputlol.txt"

vector< pair<int,char> > l;
vector<int> temp;
int a[10];

int main() {
	ios::sync_with_stdio(0);
	
	ifstream xin(IN_FILE);
	ofstream xout(OUT_FILE);
	cin.rdbuf(xin.rdbuf());
	cout.rdbuf(xout.rdbuf());
	
	int i,j,t1,t2,t3,t4,t,n,r,y,b,cnt=0,ind;
	char ch;
	cin>>t;
	while(t--){
		cin>>n;
		for(i=0;i<6;i++){
			cin>>a[i];
		}
		l.clear();
		temp.clear();
		r=a[0];
		y=a[2];
		b=a[4];
		l.push_back(make_pair(r,'R'));
		l.push_back(make_pair(y,'Y'));
		l.push_back(make_pair(b,'B'));
		sort(l.begin(),l.end());
		t1=l[2].first;
		cnt++;
		if(t1>n/2){
			cout<<"Case #"<<cnt<<": IMPOSSIBLE\n";
			continue;
		}
		cout<<"Case #"<<cnt<<": ";
		for(i=0;i<t1;i++){
			temp.push_back(0);
		}
		for(i=0;i<l[1].first;i++){
			temp[i]++;
		}
		sort(temp.begin(),temp.end());
		for(i=0;i<l[0].first;i++){
			temp[i]++;
		}
		
		t1=0;
		for(i=0;i<temp.size();i++){
			if(temp[i]==2)
				t1++;
		}
		ind=0;
		for(i=1;i<=t1;i++){
			cout<<l[2].second;
			cout<<l[1].second;
			cout<<l[0].second;
		}
		for(i=0;i<3;i++){
			l[i].first-=t1;
		}
		for(i=0;i<l[0].first;i++){
			cout<<l[2].second;
			cout<<l[0].second;
		}
		for(i=0;i<l[1].first;i++){
			cout<<l[2].second;
			cout<<l[1].second;
		}
		cout<<"\n";
		
	}
	return 0;
}

