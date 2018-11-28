#include<bits/stdc++.h>
using namespace std;
int main(){
	int cc=0,t;
	freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    cin>>t;
    while(t--){
    	printf("Case #%d: ",++cc);
    	string a,b;
        cin>>a;
        int n=a.length();
        b+=a[n-1];
        for(int i=n-2;i>=0;i--){
            if(a[i]<=b[0]){
            	b=a[i]+b;
            	continue;
            }
            for(int j=0;j<=b.size();j++) b[j]='9';
			a[i]--;
            b=a[i]+b;
        }
        if(b[0]=='0') b.erase(b.begin());
        cout<<b<<endl;
    }
    return 0;
}
