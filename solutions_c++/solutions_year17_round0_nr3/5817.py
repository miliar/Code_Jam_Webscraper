#include <bits/stdc++.h>
using namespace std;

int left(int a[],int i){
	int cnt = 0;
	for(;i>=0;i--){
		if(a[i]==1)
			return cnt-1;
		cnt+=1;
	}
}


int right(int a[],int i){
	int cnt = 0;
	for(;;i++){
		if(a[i]==1)
			return cnt-1;
		cnt++;
	}
}

int main()
{
	int t;
	cin >> t;
	int l=1;
	while(l<=t){
		int n,k;
		cin >> n >> k;
		int *a = (int*)calloc(n+2,sizeof(int));;
		a[0]=a[n+1]=1;
		int i,j,mn,mx;	
		for(j=1;j<=k;j++){
			mn=0;
			vector <int> ma; 
			for(i=1;i<=n;i++){
				int p = min(left(a,i),right(a,i));
				//cout << p << endl;
				if(mn<p){
					mn = p;
					ma.erase(ma.begin(),ma.end());
					ma.push_back(i);
				}
				else if(mn == p){
					ma.push_back(i);
				}
			}
			vector <int> an;
			mx = 0;
			for(i=0;i<ma.size();i++){
				int q = max(left(a,ma[i]),right(a,ma[i]));
				if(mx<q){
					mx = q;
					an.erase(an.begin(),an.end());
					an.push_back(ma[i]);
				}
				else if(mx==q){
					an.push_back(ma[i]);
				}
					
			}
			/*for(i=0;i<an.size();i++){
				cout << an[i]<< " ";
			}*/
			a[an[0]]=1;
			
		}
		cout << "Case #"<<l<<": "<<mx<< " " <<mn<<endl; 
		l+=1;
	}
}
	