#include <bits/stdc++.h>
#define MAX(a,b) (a>b?a:b)
#define MIN(a,b) (a<b?a:b)
#define UP upper_bound
#define LB lower_bound
#define LL long long 
#define Pi 3.14159265358
#define si size()
#define en end()
#define be begin()
#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define ii set<int>::iterator
#define Tree int ind, int L, int R
#define Left 2*ind,L,(L+R)/2
#define Right 2*ind+1,(L+R)/2+1,R
using namespace std;
main(){
	   freopen("txt.in","r",stdin);
	   freopen("txt.out","w",stdout);
	   int T;
	   cin>>T;
	   for(int t=1;t<=T;t++){
	   		int n, p, a[10], b[10][10];
	   		cin>>n>>p;
	   		for(int i=0;i<n;i++){
	   			cin>>a[i];	
			}
			for(int i=0;i<n;i++){
				for(int j=0;j<p;j++){
					cin>>b[i][j];
				}
			}int res=0;
			for(int j=0;j<p;j++){
				for(int l=1;l<=1000000;l++){
					int x;
					bool bol=true;
					for(x=0;x<n;x++){
						if(!((double)b[x][j]>=0.83*(double)(a[x]*l) && (double)b[x][j]<=1.15*(double)(a[x]*l))){
							bol=false;
							break;
						}
					}
					if(bol){
						cout<<x<<endl;
						for(x=0;x<n;x++){
							cout<<a[x]*l<<endl;
						}
						res++;
						break;
					}
				}
			}
			
			for(int i=1;i<(1<<p);i++){
				int cur=0;
				bool mtavari=true;
				for(int j=0;j<p;j++){
					if(i&(1<<j)){
						int minn=123123123;
						int maxx=0;
						for(int x=0;x<n;x++){
							minn=min(minn,b[x][j]/a[x]);
							maxx=max(maxx,b[x][j]/a[x]);
						}
						bool bll=false;
					//	cout<<minn<<" asenia "<<maxx<<endl;
						for(int l=max(1,minn-2);l<=maxx+10;l++){
							bool bol=true;
							for(int x=0;x<n;x++){
								double k=(100.00*b[x][j]/((double)a[x]*l));
							//	cout<<a[x]*l<<" "<<b[x][j]<<" "<<k<<endl;
								if(!(l*a[x]>=0.9*b[x][j] && l*a[x]<=1.1*b[x][j])){
									bol=false;
									break;
								}	
							}
						//	cout<<"///////////";
							//system("pause");
							if(bol){
								bll=true;
								break;
							}
						}
						if(!bll){
							mtavari=false;
							break;
						}
						cur++;
					}
					if(mtavari){
						res=max(res,cur);
					}
				}
			}*/
	   		cout<<"Case #"<<t<<": "<<res<<endl;
	   	
	   }
	   }	
