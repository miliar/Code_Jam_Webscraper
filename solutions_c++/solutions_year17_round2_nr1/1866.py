#include<bits/stdc++.h>
using namespace std;
int main(){
int t;
scanf("%d",&t);
for(int j=1;j<=t;j++)
{
	int d,n;
	scanf("%d %d",&d,&n);
	vector<pair<int,int> > v;
	for(int i=0;i<n;i++){
	int a,b;
	scanf("%d %d",&a,&b);
	v.push_back(make_pair(a,b));
	}
sort(v.begin(),v.end());
 double T=( double)0;
T=((double)d-v[n-1].first)/v[n-1].second;
for(int i=n-2;i>=0;i--){
 double cat=(((double)d-v[i].first)/v[i].second);
if(cat>T) T=cat;

}
printf("CASE #%d: %.6lf\n",j,d/T);

}	


}