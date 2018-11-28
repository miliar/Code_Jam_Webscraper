#include <bits/stdc++.h>
#define ll long long int
using namespace std;
typedef struct{
	ll num1;
	ll po;
}st;
int main(){
	ios::sync_with_stdio(false);
	int t;cin>>t;
	for(int y=0;y<t;y++){
		ll n,k;cin>>n>>k;
		if(n%2==0){
			ll sum=1,pro=1;
			ll level=1;
			ll po[64]={0};
			po[1]=1;
			while(1){
				po[level]=sum;
				if(sum>=k)
					break;
				sum+=(2*pro);
				pro*=2;
				level++;
			}
			ll x=pow(2,level-1);
			ll temp_num=n;
			ll temp_level=level-1;
			ll ser=k-po[level-1];
			while(temp_level--){
				temp_num/=2;
			}
			//cout<<ser<<endl;
			if(temp_num%2==0){
				ll even=(n-po[level-1])+x-(temp_num*x);
				ll odd=pow(2,level-1)-even;
				if(ser<=even){
					cout<<"Case #"<<y+1<<": "<<(temp_num/2)<<" "<<max((ll)0,(temp_num/2)-1)<<endl;
				}
				if(ser>even){
					cout<<"Case #"<<y+1<<": "<<max((ll)0,((temp_num-1)/2))<<" "<<max((ll)0,((temp_num-1)/2))<<endl;
				}
			}
			if(temp_num%2!=0){
				ll odd=(n-po[level-1])+x-(temp_num*x);
				ll even=pow(2,level-1)-even;
				if(ser<=odd){
					cout<<"Case #"<<y+1<<": "<<(temp_num/2)<<" "<<(temp_num/2)<<endl;
				}
				if(ser>odd){
					cout<<"Case #"<<y+1<<": "<<max((ll)0,((temp_num-1)/2))<<" "<<max((ll)0,((temp_num-1)/2)-1)<<endl;
				}
			}
		}
		if(n%2!=0){
			ll sum=1,pro=1;
			ll level=1;
			ll po[64]={0};
			while(1){
				po[level]=sum;
				if(sum>=k)
					break;
				sum+=(2*pro);
				pro*=2;
				level++;
			}
			ll x=pow(2,level-1);
			/*ll even=a[level];
			ll odd=pow(2,level-1)-even;*/
			//cout<<level<<" "<<even<<" "<<odd<<" ";
			ll temp_num=n;
			ll temp_level=level-1;
			ll ser=k-po[level-1];
			while(temp_level--){
				temp_num/=2;
			}//cout<<ser<<endl;
			if(temp_num%2==0){
				ll even=(n-po[level-1])+x-(temp_num*x);
				ll odd=pow(2,level-1)-even;
				if(ser<=even){
					cout<<"Case #"<<y+1<<": "<<(temp_num/2)<<" "<<max((ll)0,(temp_num/2)-1)<<endl;
				}
				if(ser>even){
					cout<<"Case #"<<y+1<<": "<<max((ll)0,((temp_num-1)/2))<<" "<<max((ll)0,((temp_num-1)/2))<<endl;
				}
			}
			if(temp_num%2!=0){
				ll odd=(n-po[level-1])+x-(temp_num*x);
				ll even=pow(2,level-1)-even;
				if(ser<=odd){
					cout<<"Case #"<<y+1<<": "<<(temp_num/2)<<" "<<(temp_num/2)<<endl;
				}
				if(ser>odd){
					cout<<"Case #"<<y+1<<": "<<max((ll)0,((temp_num-1)/2))<<" "<<max((ll)0,((temp_num-1)/2)-1)<<endl;
				}
			}
		}
	}
	return 0;
}