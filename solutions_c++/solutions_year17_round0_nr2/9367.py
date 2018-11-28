#include<bits/stdc++.h>

using namespace std;

#define ll long long

int main() {
	int t;
	cin >> t;
	for(int u=1;u<=t;u++) {
		ll num;
		cin >> num;

		ll digit=0;
		ll x=num;

		while(x) {
			digit++;
			x/=10;
		}

		if(digit==1) {
			cout << "Case #" << u << ": " << num << endl;
			continue;
		}

		ll arr[digit];

		x=num;
		ll id=digit-1;
		while(x) {
			arr[id]=x%10;
			x/=10;
			id--;
		}

		id=-1;
		for(int i=1;i<digit;i++) {
			if(arr[i-1]>arr[i]) {
				id=i-1;
				for(int j=id+1;j<digit;j++)
					arr[j]=arr[id];
				break;
			}
		}

		if(id!=-1) {
			id=0;
			for(int i=1;i<digit;i++) {
				if(arr[i]!=arr[i-1]) {
					id=i;
				}
			}

			ll cool=0;

			for(int i=id+1;i<digit;i++) {
				cool = cool*10 + arr[i];
			}
			cool++;

			ll fool=0;

			for(int i=0;i<digit;i++)
				fool=fool*10+arr[i];

			num=fool-cool;
		} 

		cout << "Case #" << u << ": " << num << endl;
	}
}