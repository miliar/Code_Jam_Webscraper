#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;

int main(){
	ifstream fin("input.txt");
	FILE * fout;
	fout=fopen("output.txt","w");
	int t;
	fin>>t;
	int cnt=1;
	while(t--){
		ll n,d;
		fin>>d>>n;
		double mn=0;
		ll k,s;
		for(int i=0;i<n;i++){
			fin>>k>>s;
			double time=( (d-k)*1.0)/s;
			//cout<<time<<endl;
			mn=time>mn?time:mn;
		}
		
		double ans=(d*1.0)/mn;
		
		fprintf(fout,"Case #%d: %0.7lf\n",cnt,ans);
		cnt++;
		
	}

	
	
fin.close();
fclose(fout);
return 0;	
}
