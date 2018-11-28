#include <bits/stdc++.h>
using namespace std;


int main(){
		#ifndef LOCAL
    ifstream cin("input.in");
    ofstream cout("output.out");
#endif
 int t, r= 0 ;
 cin>>t;
 while(t--){
 	r++;
 	int n, k;
 	cin>>n>>k;
 	int a[n];
 	for(int i = 0;i<n;i++) a[i] = 0;
 	int al = 0 ,ar = 0;
 	while(k--){
      int ls = 0 ,rs = 0 , minv = 0 , maxv = 0, pos = 0;
      for(int i = 0;i<n;i++){
      	if(!a[i]){
      		ls = 0, rs = 0;
      		int j = i-1;
      		while(j>=0 && a[j] != 1){
      			j--;
      			ls++;
      		}
      		j = i+1;
      		while(j<n && a[j] != 1){
      			j++;
      			rs++;
      		}
      		if(min(ls, rs) > minv ){
      			minv = min(ls,rs);
      			maxv = max(ls, rs);
      			pos = i;
      		}
      		else if(min(ls, rs)==minv && max(ls,rs) > maxv) minv = min(ls,rs) , maxv = max(ls,rs), pos = i;
      		al = minv, ar = maxv;
      	}
      }
      a[pos]++;
 	}
    cout<<"Case #"<<r<<": ";
 	cout<<max(al,ar)<< " "<<min(al,ar)<<endl;
 }
 
 


}