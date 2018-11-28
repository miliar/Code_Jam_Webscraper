#include<bits/stdc++.h>
using namespace std;

#define fast ios_base::sync_with_stdio(0);cin.tie(0);
#define ff first
#define ss second
#define ll long long
#define ull unsigned long long
#define mp make_pair
#define pb push_back
#define PI 3.14159265
#define all(x) (x).begin(), (x).end()
#define fileinput(name) freopen((name),"r",stdin);
#define filewrite(name) freopen((name),"w",stdout);

bool cmp(const pair<int,int> &p1,const pair<int,int> &p2){
	return  p1.ss < p2.ss;
}
int main(){
	fileinput("B-small-attempt0.in");
	filewrite("output1.txt");
	int t;
	cin>>t;
	long long int num;
	for(int tt=1;tt<=t;tt++){
		cin>>num;
		vector <int> digits;
		while(num){
			digits.pb(num%10);
			num=num/10;
		}
		reverse(digits.begin(),digits.end());
		int check=0;
		while(1){
			check=0;
			for(int i=digits.size()-1;i>0;i--){
				if(digits[i]<digits[i-1]){
					digits[i-1]--;
					for(int k=i;k<digits.size();k++){
						digits[k]=9;
					}
					check++;
				}
			}
			if(check == 0){
				break;
			}
		}
		ll ans=0;

		for(int i=0;i<digits.size();i++){
			ans=ans*10+digits[i];
		}
		cout<<"Case #"<<tt<<": "<<ans<<endl; 
	}
	
	return 0;
}
