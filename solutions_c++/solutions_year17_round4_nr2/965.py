#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define pii pair<int,int>
#define pll pair<ll,ll>
#define pdd pair<double,double>
#define X first
#define Y second
#define rep(i,a) for(int i=0;i<(int)a;i++)
#define repp(i,a,b) for(int i=(int)a;i<(int)b;i++)
#define fill(a,x) memset(a,x,sizeof(a))
#define foreach( gg, itit) for( typeof(gg.begin()) itit=gg.begin();itit!=gg.end();itit++ )
#define mp make_pair
#define pb push_back
#define all(s) s.begin(),s.end()
#define present(c,x) ((c).find(x) != (c).end())
const int mod  = 1e9+7;
const int N = 1e6+10;
const ll INF = 1e18;

#define ld long double
//#define double long double
const ld EPS=1e-12;

int cnt[1005][1005];
int pre[1005][1005];
int seat[1005];
int main(){
	//ios::sync_with_stdio(false);
	//cin.tie(NULL);
	int t;
	cin>>t;
	int ca=0;
	while(t--){
		ca++;
		int n,c,m;
		cin>>n>>c>>m;
		rep(i,n+1){
			seat[i]=0;
		}
		repp(i,1,n+1){
			repp(j,1,c+1){
				cnt[i][j]=0;
				pre[j][i]=0;
			}
		}
		rep(i,m){
			int x,y;
			cin>>x>>y;
			cnt[x][y]++;
			seat[x]++;
			pre[y][x]++;
		}
		repp(i,1,c+1){
			repp(j,2,n+1){
				pre[i][j]+=pre[i][j-1];
			}
		}
		int l=1;
		int r=m;
		repp(i,1,c+1){
			l=max(l,pre[i][n]);
		}
		int ride=m;
		int pro=n*m;
		while(l<=r){
			if(l==r){
				int mid=l;
				int flag=1;
				repp(i,1,c+1){
					if(pre[i][n]>mid){
						flag=0;
						break;
					}
				}
				int pr=0;
				int tot=0;
				repp(i,1,n+1){
					if(flag==0){
						break;
					}
					if(i==1 && seat[i]>mid){
						flag=0;
						break;
					}
					tot+=seat[i];
					if(tot> (i+1)*mid){
						flag=0;
						break;
					}
					if(seat[i]>mid){
						pr+=seat[i]-mid;
					}
				}
				if(flag==1){
					if(ride > mid){
						ride=mid;
						pro=pr;
					}else if(ride == mid){
						pro=min(pro,pr);
					}
				}
				break;
			}
			int mid=(l+r)/2;
			int flag=1;
			repp(i,1,c+1){
				if(pre[i][n]>mid){
					flag=0;
					break;
				}
			}
			int pr=0;
			int tot=0;
			repp(i,1,n+1){
				if(flag==0){
					break;
				}
				if(i==1 && seat[i]>mid){
					flag=0;
					break;
				}
				tot+=seat[i];
				if(tot> (i+1)*mid){
					flag=0;
					break;
				}
				if(seat[i]>mid){
					pr+=seat[i]-mid;
				}
			}
			if(flag==1){
				if(ride > mid){
					ride=mid;
					pro=pr;
					r=mid-1;
				}else if(ride == mid){
					pro=min(pro,pr);
					r=mid-1;
				}
			}else{
				l=mid+1;
			}
		}
		cout<<"Case #"<<ca<<": "<<ride<<" "<<pro<<endl;
	}
	return 0;
}

