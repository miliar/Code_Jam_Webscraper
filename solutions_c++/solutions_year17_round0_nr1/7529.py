#include<bits/stdc++.h>
using namespace std;

#define ll long long
#define pb push_back
#define mp make_pair
#define ff first
#define ss second
#define scan(x) scanf("%d",&x)
#define scanll(y) scanf("%lld",&y)
#define print(x) printf("%d\n",x)
#define printll(y) printf("%lld\n",y)

typedef pair<int,int>pii;
const int maxn=2e5+55;

int main() {
	freopen("Task.in","r",stdin);freopen("Task.out","w",stdout);
	int t;
	scan(t);
	for(int j=1 ; j<=t ; j++) {
		string p;
		int s,c=0,f=0;
		cin>>p;
		scan(s);
		for(int i=0 ; i<p.size() ; i++) {
			if(p[i]=='-') {
				c=c+1;
				for(int k=0 ; k<s ; k++) {
					if((i+k)<(p.size())) {
						if(p[i+k]=='-')
                        	p[i+k]='+';
                    	else
                        	p[i+k]='-';
					}
					else if(f==0) {
						cout<<"Case #"<<j<<": IMPOSSIBLE\n";
						f+=1;
					}
				}
			}
		}
		if(f==0) {
			cout<<"Case #"<<j<<": "<<c<<"\n";
		}
	}	
}