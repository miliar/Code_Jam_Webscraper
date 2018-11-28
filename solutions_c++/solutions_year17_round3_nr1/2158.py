#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define li long
#define INF 0.00000000000000
#define pb push_back
#define mp make_pair
#define pi 3.141592653589
int n,k;
li r[100000],h[100000];

double fans=0.00000000000000;

double calc(vector < pair <li,li>  > v){
	sort(v.begin(),v.end());
	double ans=0.00000000000000;
	for(int i=0;i<v.size();i++){
		if(i==0){
			ans+=((double)pi*v[i].first*v[i].first);
			ans+=((double)2*pi*v[i].first*v[i].second);
			}
		else{
			ans+=((double)2*pi*v[i].first*v[i].second);
			ans+=(((double)pi*v[i].first*v[i].first)-((double)pi*v[i-1].first*v[i-1].first));	
			} 
		}
	return ans;
	}



void comb(){
	string bitmask(k,1);
	bitmask.resize(n,0);
	do{
		vector <pair<li,li> > g;
		for(int i=0;i<n;i++){
			if(bitmask[i]) g.pb(mp(r[i],h[i]));
			}
			fans=max(fans,calc(g));
			g.clear();
		}while(prev_permutation(bitmask.begin(), bitmask.end()));		
		cout<<setprecision(8)<<fixed<<fans<<endl;

	}

int main(){
	int T;
	cin>>T;
	for(int t=1;t<=T;t++){
		cin>>n>>k;
				
		for(int i=0;i<n;i++){
			cin>>r[i]>>h[i];
			}
		for(int i=n;i<n+k;i++){
			r[i]=r[i-n];
			h[i]=h[i-n];
			}
		/*double res=INF;
		for(int i=0;i<n;i++){
			vector <pair <li,li> > v;
			for(int j=i;j<i+k;j++){
				v.pb(mp(r[j],h[j]));
				}
			res=max(res,calc(v));
			}*/
		cout<<"Case #"<<t<<": ";
		fans=0.000000000000000;
		comb();
		}
	return 0;
	}
