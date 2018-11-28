#include <bits/stdc++.h>
#include <math.h>
using namespace std;

int main(){
    int test;
    int n,k;
    double u,p;
    vector<double> cor;
    cin>>test;
	for(int tt=1;tt<=test;tt++){
		cin>>n>>k;
		cor.clear();
		cin>>u;
		for(int i=0;i<n;i++){
			cin>>p;
			cor.emplace_back(p);
		}
		sort(cor.begin(),cor.end());
		double val=cor[0];
		int i;
		for(i=1;i<n;i++){
			if((cor[i]-val)*i<=u){
				u-=(cor[i]-val)*i;
				val=cor[i];
			}else{
				val+=u/i;
				u=0;
				break;
			}
		}
		if(i==n)
			val+=u/i;
		double pra=1;
		for(int j=0;j<n;j++){
			if(j<i)
				pra*=val;
			else
				pra*=cor[j];
		}
		
		cout<<"Case #"<<tt<<": ";
		cout << std::fixed;
  		cout << std::setprecision(9);
		cout<<pra<<endl;
	}
	
    
    
    return 0;
}

