#include<bits/stdc++.h>
#define pi acos(-1)
using namespace std;
int main(){
	           cin.sync_with_stdio(false);
	           int T , tt = 1;
	           cin >> T;
	           while(T--){ 
	           	  int n , k;
	           	  cin >> n >> k;
	           	  	 vector< pair < double , double > > v;           	  
	           	     for(int i = 1 ; i <= n ; ++i ){
                            double r , h;
                            cin >> r >> h;
                            v.push_back({r , h});
	           	     }
	           	     sort(v.begin() , v.end());
	           	     double res = 0.0;
	           	     for(int i = k - 1 ; i < v.size() ; ++i ){
	           	     	  double tot = pi * v[i].first * v[i].first + 2 * pi * v[i].first * v[i].second;
	           	     	  vector< double > temp;
	           	     	  for(int j = 0 ; j < i ; ++j )
	           	     	  	 temp.push_back(2 * pi * v[j].second * v[j].first);
	           	     	  	sort(temp.begin() , temp.end());
	           	     	  	int en = temp.size()-1;
	           	     	  	int ti = k - 1;
	           	     	  	double extra = 0.0;
	           	     	  	while(ti--){
                                 extra += temp[en];
                                 en--;
	           	     	  	}
	           	     	  	res = max(res ,tot + extra);
	           	     }
	           	     printf("Case #%d: %.9lf\n",tt++,res);	           	    

	           }


}