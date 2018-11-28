#include <bits/stdc++.h>
#define fre freopen("0.in","r",stdin),freopen("0.out","w",stdout)

using namespace std;
 
char a[1024];
 
int main() {
    
	freopen("input.in", "r", stdin);
	freopen("B--attempt0.out", "w", stdout);
	
	int t;
    cin>>t;
    for(int ii=1;ii<=t;ii++){
    	int k;
    	scanf("%s",a+1);
    	cin>>k;
 
    	int l=strlen(a+1);
    	bool poss = true;
    	int ans=0;
 
    	for(int i=1;(i+k-1)<=l;i++){
    		if(a[i]=='-'){
    			ans++;
    			for(int j=i;j<(i+k);j++){
    				if(a[j]=='-')a[j]='+';
    				else a[j]='-';
    			}
    		}
    	}
    	for(int i=1;i<=l;i++)if(a[i]=='-')poss=false;
    	//cout<<"Case #"<<ii<<" :";
    	cout << "Case #" <<++i << ": " << ii << "\n";
		if(poss==true)cout<<ans<<endl;
    	else cout<<"Case #" <<++i << ":"<<"IMPOSSIBLE\n";
    }
	return 0;
}
