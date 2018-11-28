#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <set>
#include <string>
#include <cmath>

using namespace std;

typedef long long ll;
int dx[]={1,0,-1,0};
int dy[]={0,1,0,-1};

#define in(x,y) ( (x)>=0 && (y)>=0 && (x)<n && (y)<m )
#define MOD 1000000007
#define INF 2147483647
#define PI 3.1415926535897932384626433832795
#define all(cont) cont.begin(),cont.end()
#define init(a,val) memset(a,val,sizeof(a))
#define F first
#define S second
#define mp make_pair
#define MAX 12000

int main()
{
	freopen("b.in","r",stdin);
	//freopen("b.out","w",stdout);
	int p[4],s[4],b[4];
	char pri[4]="RYB";
	char sec[4]="GVO";
//_______________________________________________
	int test_cases,tesT;

	cin>>test_cases;
	for(tesT=0;tesT<test_cases;tesT++){
		cout<<"Case #"<<tesT+1<<": ";
		cerr<<"Case #"<<tesT+1<<": ";
//_______________________________________________
		int n,tot=0,i,k,maxx,it;
		string ans="";

		cin>>n>>p[0]>>s[2]>>p[1]>>s[0]>>p[2]>>s[1];
		for(i=0;i<3;i++){
			p[i]-=s[i];
			b[i]=p[i];
			tot+=b[i];
		}
		for(i=0;i<3;i++){
			if(p[i]<0){
				cerr<<"p[i]<0>> ";
				cout<<"IMPOSSIBLE";
				goto done;
			}
			else if(p[i]==0 && s[i]!=0){
				cerr<<"p[i]==0>> ";
				//cout<<s[i]<<p[i]<<' ';
				if(n!=s[i]*2){
					cout<<"IMPOSSIBLE";
					goto done;
				}
				else{
					
					for(k=0;k<s[i];k++){
						ans+=pri[i];
						ans+=sec[i];
					}
					cout<<ans;
					goto done;
				}
			}

			else if(p[i]>p[(i+1)%3]+p[(i+2)%3]){
				cout<<"IMPOSSIBLE";
				goto done;
			}
		}
		for(i=0;i<3;i++)if(p[i]>0){
			ans=pri[i];
			p[i]--;
			break;
		}
		for(i=0;i<3;i++)cerr<<p[i]<<' ';
		for(it=1;it<tot;it++){
			maxx=0;
			int maxval=0;
			char preval;
			if(it>0)preval=ans[it-1];
			for(i=0;i<3;i++)if(p[i]>maxval && pri[i]!=preval){
				maxx=i;
				maxval=p[i];
			}
			ans+=pri[maxx];
			p[maxx]--;
		}
		for(i=0;i<3;i++){
			for(it=0;it<tot;it++)if(ans[it]==pri[i] )break;//find compliment
			string ins="";
			for(k=0;k<s[i];k++){
				ins+=pri[i];
				ins+=sec[i];
			}
			//cout<<ins;
			ans.insert(it,ins);
		}
		for(it=0;it<ans.size();it++)if(ans[it]==ans[(it+1)%ans.size()]){
			cerr<<"ERROR "<<tesT+1<<'#';
		}
		cout<<ans;

//_______________________________________________
		done:
		cout<<endl;
		cerr<<endl;
	}

	cerr<<endl;
	return 0;
}