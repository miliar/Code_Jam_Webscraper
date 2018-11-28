#include <bits/stdc++.h>
using namespace std;

int main() {
    int tcase,tn=1;
    
    FILE *ptr,*o;
    ifstream in("A-large.in");
    ofstream op("output.txt");
   in>>tcase;
    //fscanf(ptr,"%d",&tcase);
    //cin>>tcase;
    while(tn<=tcase){
        long long int ans=0;
        int k,n;
        string s;
        in>>s>>k;
        n=s.size();
        for(int i=0;i<=n-k;i++){
           if(s[i]=='-'){
           	for(int j=i;j<i+k;j++){
           		if(s[j]=='-')
           		s[j]='+';
			   else
			   s[j]='-';
			   
		   }
		   ans++;
        }}
        int f=0;
    	for(int i=0;i<n;i++){
    		if(s[i]=='-'){
    			f=1;break;
			}
		}
		if(f)
		op<<"Case #"<<tn<<": IMPOSSIBLE"<<"\n";
		else
        op<<"Case #"<<tn<<": "<<ans<<"\n";
        //fprintf(o,"Case #%d: %d\n",tn,ans);
       tn++;
    }
    
	return 0;
}

