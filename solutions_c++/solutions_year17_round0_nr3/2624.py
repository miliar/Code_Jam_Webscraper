#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <unordered_map>
#include <map>
#include <stack>
#include <queue>
#include <cmath>
#include <climits>

#define ll long long

using namespace std;

int main(){
	int t;
	cin>>t;
	int a=0;
	while (t--){
		a++;
		cout<<"Case #"<<a<<": ";
		ll n,k;
		cin>>n>>k;
		ll o=0,e=0,oc=0,ec=0;
		ll yet=0;
		if (n%2==0){
			e=n;
			ec=1;
		}
		else{
			o=n;
			oc=1;
		}

		while (yet+oc+ec<k){
			yet+=oc+ec;
			ll neweven,newodd, evencount=0,oddcount=0,new1,new2, new3;

			if (oc!=0){
				new1=o/2;
				if (new1%2==0){
					neweven=new1;
					evencount=2*oc;
				}
				else{
					newodd=new1;
					oddcount=2*oc;
				}
			}
			if (ec!=0){
				new2=e/2-1;
				new3=e/2;
				if (new2%2==0){
					neweven=new2;
					newodd=new3;
					
				}
				else{
					neweven=new3;
					newodd=new2;

				}
				evencount+=ec;
				oddcount+=ec;
			}

			
			ec=evencount;
			oc=oddcount;

			
			o=newodd;
			e=neweven;
			//cout<<ec<<" "<<oc<<" "<<o<<" "<<e<<" "<<yet<<endl;
		}
		if (o>e){
			if (yet+oc>=k){
				cout<<o/2<<" "<<o/2;
			}
			else{
				cout<<e/2<<" "<<e/2-1;
			}
		}
		else{
			if (yet+ec>=k){
				cout<<e/2<<" "<<e/2-1;
			}
			else{
				cout<<o/2<<" "<<o/2;
			}
		}
		cout<<endl;
	}
	
	return 0;
}
