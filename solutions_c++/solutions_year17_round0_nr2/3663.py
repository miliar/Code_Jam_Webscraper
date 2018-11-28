#include <bits/stdc++.h>
using namespace std;

int main() {
    int tcase,tn=1;
    
    FILE *ptr,*o;
    ifstream in("B-large.in");
    ofstream op("output.txt");
   in>>tcase;
    while(tn<=tcase){
        long long int ans=0;
        string s;
        int n,li;
        in>>s;
        n=s.size();
        if(n==1)
        op<<"Case #"<<tn<<": "<<s<<"\n";
        else{
        for(int i=1;i<n;i++){
        	if(i==0)
        	break;
        	if(s[i]<s[i-1]){
        		s[i-1]--;
        		li=i;
        		for(int j=li;j<n;j++)
        		s[j]='9';
        		i=i-2;
			}
       }
       if(s[0]=='0'){
       	for(int i=0;i<n-1;i++)
       	s[i]=s[i+1];
       	 s.resize(n-1);
	   }
	  
      
		op<<"Case #"<<tn<<": "<<s<<"\n";}
	
        //fprintf(o,"Case #%d: %d\n",tn,ans);
       tn++;
    }
    
	return 0;
}

