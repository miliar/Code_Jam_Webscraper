#include <bits/stdc++.h>

using namespace std;
#define pb push_back
#define mp make_pair
typedef long long int ll;

ifstream in("A-large.in");
ofstream out("output");

map<int,vector<int>> myp;
int n,k;
double r[1005][1005];
vector<pair<int,int>> gr;
int fst,lst;

double getA(double ra){
	return (M_PI*ra*ra);
}

double getY(double h, double ra){
	return (2*M_PI*ra*h);
}



int main(){
    int t;
    in>>t;
    
    double a,b;
    for(int indx = 1;indx<=t;indx++){
    	myp.clear();
    	for(int i = 0;i<=1004;i++){
    		for(int j = 0;j<=1004;j++){
    			r[i][j] = 0;
    		}
    	}
    	out<<"Case #"<<indx<<": ";
    	in>>n>>k;
    	lst = 1;
    	gr.clear();
    	for(int i = 0;i<n;i++){
    		in>>a>>b;
    		myp[a].pb(b); 
    	}
    	for(auto it:myp){
    		sort(it.second.begin(),it.second.end());
    	}
    	gr.pb(mp(0,0));
    	for(auto it = myp.rbegin();it!=myp.rend();it++){
    		for(int i = it->second.size()-1;i>=0;i--){
    			gr.pb(mp(it->first,it->second[i]));
    		}
    	}
    	
    	
    	for(int i = 1;i<gr.size();i++){
    		int ra = gr[i].first;
    		double yuk = getY((double)gr[i].second,(double)ra);
    		double alan = getA((double)ra);
    		r[i][1] = max(r[i-1][1],alan+yuk);
    		if(i==1)
    			continue;
    		int j = 2;
    		while(r[i-1][j]!=0&&j<=k){
    			r[i][j] = max(r[i-1][j],r[i-1][j-1]+yuk);
    			j++;
    		}
    		r[i][j] = r[i-1][j-1]+yuk;
    	}

    	out<<fixed<<setprecision(10)<<r[gr.size()-1][k]<<endl;


    }
    return 0;
}