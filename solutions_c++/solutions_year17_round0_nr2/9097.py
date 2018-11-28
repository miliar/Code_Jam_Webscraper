#include <bits/stdc++.h>
using namespace std;
#define int long long

int chk(int x) {
    int f=0;
    int ctr=0;
    int prev=-1;
    while(x>0) { 
        
        int d=x%10;
        
        if(ctr==0);
        else{
            if(d>prev) {
                f=1; break;
            }
        }
        prev=d;
        x/=10;
        ctr++;
    }
    
    if(f==1) return 0;
    else return 1;
    
}


 main() {
     int arr[]={1,2};
    freopen("inp.txt","r",stdin);
	freopen("outs.txt","w",stdout);
	int t;
	cin>>t;
	for(int z=1;z<=t;z++) {
	string n;
	cin>>n;
	int f=0;
	string ans="";
	int i;
	
	if(chk(atoi(n.c_str()))==1) {
		cout<<"Case #"<<z<<": "<<n<<endl; continue;
	}
	
	for(i=0;i<n.length()-1;i++) {
		if(n[i]>=n[i+1]) { f=1; break; }
		
	}
	
	if(f==0) {
	    cout<<"Case #"<<z<<": "<<n<<endl; continue;
	}
	
	for(int j=0;j<=i-1;j++) ans+=n[j];
	ans+=(n[i]-1);
	
	for(int j=i+1;j<n.length();j++) ans+="9";
	if(n.length()==1) ans=n;
	for(int j=0;j<ans.length();j++) {
	    if(ans[i]=='0')
	        ans.erase(i,1);
	       else break;
	}
	cout<<"Case #"<<z<<": "<<ans<<endl;
	
	
	
	
	}
 
	return 0;
}
