#include <bits/stdc++.h>
using namespace std;
#define mod 1000000007

typedef long long int ll;

#define pi  3.14159265358979323846264338327950288419716939937510

struct syl{
	double r,h;
};

bool compare(const struct syl& a,const struct syl& b){
	if(a.r>b.r)return 1;
	if(a.r==b.r && a.h> b.h)return 1;
	return 0;
}


bool compare2(const struct syl& a,const struct syl& b){
	return a.r*a.h>=b.r*b.h;
	//if(a.r==b.r && a.h> b.h)return 1;
}

int main(){
	int T;
	int n,i,j,k;
	struct syl s[1004];
	double ans,cnt;
	cin>>T;
	for(int t=1;t<=T;t++){
		ans=cnt=0;
		cin>>n>>k;
		for(i=0;i<n;i++)cin>>s[i].r>>s[i].h;
		sort(s,s+n,compare2);
		int cnt2;
		for(i=0;i<n;i++){
			cnt2=1;
			cnt=s[i].r*s[i].r+2*s[i].h*s[i].r;
			for(j=0;j<n;j++){
				if(i==j)continue;
				if(s[i].r>=s[j].r){
					if(cnt2>=k)break;
					cnt+=2*s[j].r*s[j].h;
					cnt2++;
				}
			}
			//cout<<"cnt="<<cnt<<endl;
			if(cnt2==k && cnt > ans)ans=cnt;
		}
		cout<<"Case #"<<t<<": ";
		//cout.precision(9);
		//cout<<(double)((double)pi*(double)ans)<<endl;
		printf("%0.9lf\n",(double)((double)pi*(double)ans));
		//cout<<"Case #"<<t<<": "<<ans<<endl;
		
	}

}