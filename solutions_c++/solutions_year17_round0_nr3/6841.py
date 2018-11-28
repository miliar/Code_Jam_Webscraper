#include <iostream>
#include <vector>
using namespace std;

void valor(vector <pair <int,int> >& V){
	for (int i=1; i<V.size()-1; i++)
		if (V[i].first!=0) V[i].first=V[i-1].first+1;
	
	 for (int i=V.size()-2; i>=1; i--)
		if (V[i].second!=0) V[i].second=V[i+1].second+1;
}

int posicio (vector <pair <int,int> >& V){
	int p=1;
	for (int j=2; j<V.size()-1; j++){
		if (V[j].first!=0){
			if (min(V[j].first,V[j].second)> min(V[p].first,V[p].second)) p=j;
			else {
				if ((min(V[j].first,V[j].second)== min(V[p].first,V[p].second )and( max(V[j].first,V[j].second)> max(V[p].first,V[p].second) ))) p=j;
				}
	}
}
return p;
}

int main(){
	int t;
	while (cin>>t){
		for (int i=1; i<=t; i++){
			int n,k,p;
			cin>>n>>k;
			
			vector <pair <int,int> > V(n+2, make_pair (-1,-1));
			V[0]=make_pair(0,0);
			V[n+1]=make_pair(0,0);
			
			for (int r=0; r<k-1; r++){
			valor(V);
			p=posicio(V);
			V[p].first =0;
			V[p].second =0;
			
		}
		valor(V);
		p=posicio(V);
		
		cout<<" Case #"<<i<<": "<<max(V[p].first,V[p].second)-1<<" "<<min(V[p].first,V[p].second)-1<<endl;
	}
}
}
