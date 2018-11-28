//anmolarora123
#include<bits/stdc++.h>
#include<iostream>
#define f(i,a,n) for(int i=a;i<n;i++)
#define ll long long
#define si(a) scanf("%d",&a)
#define sl(a) scanf("%lld",&a)
#define ss(s) scanf("%s",s)
#define pi(a) printf("%d\n",a)
#define pl(a) printf("%lld\n",a)
#define pb(a) push_back(a)
#define mp(a,b) make_pair(a,b)
using namespace std;
int main(){
	int t;
	ll n;
	si(t);
	for(int i=1;i<=t;i++) {
		sl(n);
		string str = to_string(n);
		int position = -1;
		for(int j = 0;j<str.length()-1;) {
			if (str[j] > str[j+1]) {
				// cout<<"large "<<str[j] << " "<<str[j+1]<<endl;
				position = j;
				
				str[position] = str[position] - 1;
				
				for (int k=position+1; k< str.length();k++) {
					str[k] = '9';
				}
					
					// cout<< position<<endl;
				j --;
				
				// break;
			} else {
				j++;
			}
			// cout<<"str: "<<str<<endl;
		}
		str.erase(0, min(str.find_first_not_of('0'), str.size()-1));
		
		printf("Case #%d: ",i); 
		
		cout<<str;
		
		printf("\n");
	}
	return 0;
}