#include <bits/stdc++.h>
using namespace std;

bool cmp(double a[2] , double b[2]){
	if(a[0] == b[0]) return a[1] < b[1] ;
	else return a[0] < b[0] ;
}

int main (int argc, char const* argv[])
{
	int t;
	cin>>t ;
	
	for(int tc = 1 ; tc <= t ; tc++){
		double dist ;
		int n ;
		cin>>dist>>n ;
		
		double x1 , s1 , d ;
		bool check = true ;
		
		map<double , double> arr ;
		
		for(int i = 0 ; i < n ; i++){
			double x , s ;
			cin>>x>>s ;
			if(arr.find(x) == arr.end()) { arr.insert(make_pair(x,s)); }
			else if(arr[x] > s) arr[x] = s;
		}
		
		int count = 0 ;
		double t_time = 0 ;
		
		for(auto i = arr.begin() ; i != arr.end() ; i++){
			double x2 , s2 ;
			s2 = i->second ;
			x2 = i->first ;
			
			if(count == 0){
				x1 = i->first , s1 = i->second ;
			}
			
			else if(s1 < s2 || !check) {  break ; }
			
			if(count != 0 && check){
				d = (x2*s1 - x1*s2)/(s1 - s2) ;
				if(d >= dist) check = false ;
				if(d < dist){
					t_time += (d - x2)/s2 ;
					x1 = d , s1 = s2 ;
				}
			}
			
			count++;
		}
		
		t_time += (dist - x1)/s1 ;
		
		double ans = (dist)/(t_time) ;
		cout<<"Case #"<<tc<<": " ;
		printf("%.6lf\n" , ans);
	}
	
	return 0;
}
