#include <bits/stdc++.h>

using namespace std;

#define ll long long

int a,b;

int type[1440*2+10];

int sa[111];
int ta[111];

int sb[111];
int tb[111];

int main(){
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);
	int t;
	cin>>t;
	int cas = 0;
	
	while(t--){
		memset(type,-1,sizeof(type));
		
		cas++;
		
		cin>>a>>b;
		
		int Min = 1e9;
		
		for(int i=0;i<a;i++){
			cin>>sa[i]>>ta[i];
			Min = min(Min,sa[i]);
		}
		
		for(int i=0;i<b;i++){
			cin>>sb[i]>>tb[i];
			Min = min(Min,sb[i]);
		}
		
		//
		for(int i=0;i<a;i++){
			sa[i] -= Min;
			ta[i] -= Min;
			ta[i] --;
		}
		
		for(int i=0;i<b;i++){
			sb[i] -= Min;
			tb[i] -= Min;
			tb[i] --;
		}
		
		//
		for(int i=0;i<a;i++){
			for(int j=sa[i];j<=ta[i];j++){
				type[j] = 0;
			}
		}
		
		for(int i=0;i<b;i++){
			for(int j=sb[i];j<=tb[i];j++){
				type[j] = 1;
			}
		}
		
		for(int i=0;i<1440;i++){
			type[i+1440] = type[i];
			
		}
		
		vector<int> empty;
		
		int ans = 0;
		int curtype = type[0];
		
		for(int i=0;i<=1440;i++){
			
			if(type[i]!=-1){
				if(type[i]!=curtype){
					curtype = type[i];
					ans++;
				}
			}
			
			if(type[i] == -1){
				int l = i;
				int r = i;
				while(type[l] == -1){
					l--;
				}
				while(type[r] == -1){
					r++;
				}
				empty.push_back(r-l-1);
				
				if(type[l] == type[r]){
					for(int j=l+1;j<r;j++){
						type[j] = type[l];
					}
				}
				i = r-1;
			}
		}
		
		
		int cnta = 0;
		int cntb = 0;
		for(int i=0;i<1440;i++){
			if(type[i] == 0){
				cnta++;
			}
			if(type[i] == 1){
				cntb++;
			}
		}
		
		int over = 0;
		if(cnta>720){
			over = cnta-720;
		}
		if(cntb>720){
			over = cntb-720;
		}
		
		sort(empty.begin(),empty.end());
		reverse(empty.begin(),empty.end());
		
		
		/*for(int x:empty){
			cout<<x<<" ";
		}
		cout<<endl;
		*/
		
	//	cout<<"ans = "<<ans<<endl;
		for(int i=0;i<empty.size();i++){
			if(over>0){
				over -= empty[i];
				ans+=2;
			}else{
				break;
			}
		}
		
		printf("Case #%d: %d\n",cas,ans);
		//cout<<ans<<endl;
		
	}
	return 0;
}
