#include<iostream>
#include<queue>
#include<vector>

typedef long long ll;

using namespace std;

int main() {

	int T;
	cin>>T;

	ll N,K;

	for(int i=1;i<=T;i++) {
		cin>>N>>K;
		priority_queue<ll> slots;
		slots.push(N);

		ll useSlot;
		ll y,z;
		while (K--)
		{
			useSlot=slots.top(); slots.pop();
			//cout<<"popped : "<<useSlot<<endl;
			useSlot--;
			z=useSlot/2;
			y=z;
			if(useSlot%2)
				y++;
			if(y)
				slots.push(y);
			if(z)
				slots.push(z);
			//cout<<"inserted : "<<y<<":"<<z<<endl;
		}
		cout<<"Case #"<<i<<": "<<y<<" "<<z<<endl;
	}


}