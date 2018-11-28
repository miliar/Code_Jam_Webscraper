#include <bits/stdc++.h>
using namespace std;

int main() {
    int tcase,tn=1;
    
    FILE *ptr,*o;
    ifstream in("C-small-2-attempt1.in");
    ofstream op("output.txt");
   in>>tcase;
 //  tcase=1;
    while(tn<=tcase){
        long long int ans=0,n,k;
        in>>n>>k;
         set <pair <int,int > > S;
         S.insert(make_pair(-n,1));
         long long int f1,f2,c;
         for(long long int i=0;i<k-1;i++){
         	
         	f1=-S.begin()->first;
         	f2=S.begin()->second;
         	S.erase(S.begin());
         	//cout<<(f1/2-1+(f1%2))<<" "<<f2<<" "<<(f1/2)<<" "<<f2+(f1/2-1+(f1%2))+1<<"\n";
         	if(f1&1){
         		if(f1/2){
         	S.insert(make_pair(-(f1/2),f2));
         	S.insert(make_pair(-(f1/2),f2+(f1/2)+1));}}
         	else{
         		if(f1/2-1)
         	S.insert(make_pair(-(f1/2-1),f2));
         	if(f1/2)
         	S.insert(make_pair(-(f1/2),f2+(f1/2)));	
			 }
         	
		 }
      		f1=-S.begin()->first;
         	long long int l,r;
         	l=(f1/2-1+(f1%2));
         	r=(f1/2);
         	
		op<<"Case #"<<tn<<": "<<max(l,r)<<" "<<min(l,r)<<"\n";
	
        //fprintf(o,"Case #%d: %d\n",tn,ans);
       tn++;
    }
    
	return 0;
}

