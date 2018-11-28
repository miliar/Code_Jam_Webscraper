#include<iostream>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<algorithm>
#include<utility>
#define PB push_back
#define pii pair<int,int>
#define MP make_pair
#define sz size()
#define fi first
#define se second
using namespace std;
typedef long long ll;
int main()
{
	int t,i,j,k,cs,css;
	cin>>css;
	for(cs=1;cs<=css;cs++)
	{
		int HD,AD,HK,AK,B,D;
		cin>>HD>>AD>>HK>>AK>>B>>D;
		int ans=-1;
		int dl=101,bl=101;
		if(B==0)bl=0;
		if(D==0)dl=0;
		for(i=0;i<=dl;i++) {
			if(AK-(i-1)*D < 0 && i>0)break;
			for(j=0;j<=bl;j++) {
				if(AD+(j-1)*B > HK && j>0)break;
				int hd=HD,ad=AD,hk=HK,ak=AK,t1=i,t2=j;
				int p=0;
				for(k=1;;k++) {
//					cout<<k<<" "<<hd<<" "<<ad<<" "<<hk<<" "<<ak<<" "<<t1<<" "<<t2<<endl;
					if(hk-ad <=0) {
						p=0;
						break;
					}
					if(hd-ak <= 0) {
						if(t1>0 && hd-ak+D > 0) {
							ak-=D;
							t1--;
							hd-=ak;
							p=0;
							continue;
						}
						if(p==1)break;
						p=1;
						hd=HD;
						hd-=ak;
						continue;
					}
					if(t1>0) {
						ak-=D;
						t1--;
						hd-=ak;
						p=0;
						continue;
					}
					if(t2>0) {
						ad+=B;
						t2--;
						hd-=ak;
						p=0;
						continue;
					}
					hk-=ad;
					hd-=ak;
					p=0;
				}
				if(p==0) {
					if(ans==-1 || ans>k)ans=k;
				}
			}
		}
		cout<<"Case #"<<cs<<": ";
		if(ans>0) {
			cout<<ans<<endl;
		} else {
			cout<<"IMPOSSIBLE\n";
		}
	}
	return 0;
}
