#include <bits/stdc++.h>
using namespace std;
int d,k;
vector< pair<double,double> > v;
vector< pair<double,double> > m;
int main(){
	int t,t1 = 1;
	cout.precision(8);
	scanf("%d",&t);
	while(t--){
		v.clear();
		m.clear();
		scanf("%d %d",&d,&k);
		int i,j;
		for(i = 0 ; i < k ; i++){
			double a,b;
			cin >> a >> b;
			v.push_back(make_pair(a,b));
		}
		sort(v.begin(),v.end());
		double pos,ti;
		for(i = 0 ; i <= k-2 ; i++){	
			if(v[i] < v[i+1]){
				ti = (d-v[i].first)/v[i].second; 
				m.push_back(make_pair(d,ti));
				break;
			}
			pos = (v[i].first*v[i+1].second-v[i].second*v[i+1].first);
			pos = pos/(v[i+1].second-v[i].second);
			ti  = (pos-v[i+1].first)/v[i+1].second;
			//cout << pos << "  " << ti << "\n";
			m.push_back(make_pair(pos,ti));				
		}
		if(m.size() > 0){
			int q = m.size();
			ti = (d-v[q].first)/v[q].second;
			m.push_back(make_pair(d,ti));	
		}
		if(m.size() == 0){
			ti = (d-v[0].first)/v[0].second;
			m.push_back(make_pair(d,ti));	
		}
		
		double min = m[0].first/m[0].second;
		//cout << m[0].first << "  " << m[0].second << "\n";
		for(i = 1 ; i < m.size() ; i++){
			double a = m[i].first/m[i].second;
			//cout << m[i].first << "  " << m[i].second << "\n";
			if(min > a ){
				min = a;
			}
		}
		cout << "Case #" << t1 << ": " << min << "\n";		
		t1++;	
	}

}

